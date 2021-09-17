#
# (C) Copyright Cloudlab URV 2021
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys
import json
import queue
import lithops
import logging
import shutil
import threading
import subprocess as sp
from shutil import copyfile

from lithops.constants import TEMP, LITHOPS_TEMP_DIR, COMPUTE_CLI_MSG, RN_LOG_FILE, JOBS_PREFIX
from lithops.utils import is_lithops_worker

logger = logging.getLogger(__name__)

RUNNER = os.path.join(LITHOPS_TEMP_DIR, 'runner.py')
LITHOPS_LOCATION = os.path.dirname(os.path.abspath(lithops.__file__))


class LocalhostHandler:
    """
    A localhostHandler object is used by invokers and other components to access
    underlying localhost backend without exposing the implementation details.
    """

    def __init__(self, localhost_config):
        logger.debug('Creating Localhost compute client')
        self.config = localhost_config

        self.jobs = {}  # dict to store executed jobs (job_keys) and PIDs
        self.env = {}  # dict to store environments
        self.job_queue = queue.Queue()
        self.job_manager = None
        self.should_run = True

        msg = COMPUTE_CLI_MSG.format('Localhost compute')
        logger.info("{}".format(msg))

    def init(self):
        """
        Init tasks for localhost
        """
        pass

    def start_manager(self):
        """
        Starts manager thread to keep order in tasks
        """
        def job_manager():
            logger.debug('Staring localhost job manager')
            self.should_run = True

            while self.should_run:
                job_payload, job_filename = self.job_queue.get()
                if job_payload is None and job_filename is None:
                    break
                executor_id = job_payload['executor_id']
                job_id = job_payload['job_id']
                job_key = job_payload['job_key']
                runtime_name = job_payload['runtime_name']
                env = self.get_env(runtime_name)
                process = env.run(job_payload, job_filename)
                self.jobs[job_key] = process
                process.communicate()  # blocks until the process finishes
                logger.debug(f'ExecutorID {executor_id} | JobID {job_id} - Execution finished')
                if self.job_queue.empty():
                    break

            self.job_manager = None
            logger.debug("Localhost job manager stopped")

        if not self.job_manager:
            self.job_manager = threading.Thread(target=job_manager)
            self.job_manager.start()

    def _get_env_type(self, runtime_name):
        """
        Gets the environment type based on the runtime name
        """
        return 'default' if '/' not in runtime_name else 'docker'

    def get_env(self, runtime_name):
        """
        Generates the proper runtime environment based on the runtime name
        """
        if runtime_name not in self.env:
            if '/' not in runtime_name:
                env = DefaultEnv()
            else:
                pull_runtime = self.config.get('pull_runtime', False)
                env = DockerEnv(runtime_name, pull_runtime)
            env.setup()
            self.env[runtime_name] = env

        return self.env[runtime_name]

    def create_runtime(self, runtime_name, *args):
        """
        Extract the runtime metadata and preinstalled modules
        """
        logger.info(f"Extracting preinstalled Python modules from {runtime_name}")

        env = self.get_env(runtime_name)

        runtime_metadata = env.preinstalls()

        return runtime_metadata

    def invoke(self, job_payload):
        """
        Run the job description against the selected environment
        """
        executor_id = job_payload['executor_id']
        job_id = job_payload['job_id']
        runtime_name = job_payload['runtime_name']
        logger.debug(f'ExecutorID {executor_id} | JobID {job_id} - Putting job into localhost queue')

        self.start_manager()
        env = self.get_env(runtime_name)
        job_filename = env._prepare_job_file(job_payload)

        self.job_queue.put((job_payload, job_filename))

    def get_runtime_key(self, runtime_name, *args):
        """
        Generate the runtime key that identifies the runtime
        """
        env_type = self._get_env_type(runtime_name)
        runtime_key = os.path.join('localhost', env_type, runtime_name.strip("/"))

        return runtime_key

    def get_backend_type(self):
        """
        Wrapper method that returns the type of the backend (Batch or FaaS)
        """
        return 'batch'

    def clean(self):
        """
        Deletes all local runtimes
        """
        pass

    def clear(self, job_keys=None):
        """
        Kills all running jobs processes
        """
        self.should_run = False

        while not self.job_queue.empty():
            try:
                self.job_queue.get(False)
            except Exception:
                pass

        if job_keys:
            for job_key in job_keys:
                try:
                    # None means alive
                    if job_key not in self.jobs or \
                       self.jobs[job_key].poll() is not None:
                        continue
                    logger.debug(f'Killing job {job_key} with '
                                 f'PID {self.jobs[job_key].pid}')
                    self.jobs[job_key].kill()
                except Exception:
                    pass
        else:
            for job_key in self.jobs:
                try:
                    if self.jobs[job_key].poll() is not None:
                        continue
                    logger.debug(f'Killing job {job_key} with '
                                 f'PID {self.jobs[job_key].pid}')
                    self.jobs[job_key].kill()
                except Exception:
                    pass

        if self.job_manager:
            self.job_queue.put((None, None))


class BaseEnv():
    """
    Base environment class for shared methods
    """
    def __init__(self, runtime):
        self.runtime = runtime

    def _copy_lithops_to_tmp(self):
        if is_lithops_worker() and os.path.isfile(RUNNER):
            return
        os.makedirs(LITHOPS_TEMP_DIR, exist_ok=True)
        try:
            shutil.rmtree(os.path.join(LITHOPS_TEMP_DIR, 'lithops'))
        except FileNotFoundError:
            pass
        shutil.copytree(LITHOPS_LOCATION, os.path.join(LITHOPS_TEMP_DIR, 'lithops'))
        src_handler = os.path.join(LITHOPS_LOCATION, 'localhost', 'runner.py')
        copyfile(src_handler, RUNNER)

    def _prepare_job_file(self, job_payload):
        """
        Creates the job file that contains the job payload to be executed
        """
        job_key = job_payload['job_key']
        storage_bucket = job_payload['config']['lithops']['storage_bucket']

        local_job_dir = os.path.join(LITHOPS_TEMP_DIR, storage_bucket, JOBS_PREFIX)
        docker_job_dir = f'/tmp/lithops/{storage_bucket}/{JOBS_PREFIX}'
        job_file = f'{job_key}-job.json'

        os.makedirs(local_job_dir, exist_ok=True)
        local_job_filename = os.path.join(local_job_dir, job_file)

        with open(local_job_filename, 'w') as jl:
            json.dump(job_payload, jl, default=str)

        if isinstance(self, DockerEnv):
            job_filename = '{}/{}'.format(docker_job_dir, job_file)
        else:
            job_filename = local_job_filename

        return job_filename


class DockerEnv(BaseEnv):
    """
    Docker environment uses a docker runtime image
    """
    def __init__(self, docker_image, pull_runtime):
        logger.debug(f'Starting Docker Environment for {docker_image}')
        super().__init__(runtime=docker_image)
        self.pull_runtime = pull_runtime

    def setup(self):
        logger.debug(f'Setting up Docker environment')
        self._copy_lithops_to_tmp()
        if self.pull_runtime:
            logger.debug('Pulling Docker runtime {}'.format(self.runtime))
            sp.run('docker pull {}'.format(self.runtime), shell=True, check=True,
                   stdout=sp.PIPE, universal_newlines=True)

    def preinstalls(self):
        if not os.path.isfile(RUNNER):
            self.setup()

        cmd = (f'docker run --rm -v {TEMP}:/tmp --entrypoint "python3" '
               f'{self.runtime} /tmp/lithops/runner.py preinstalls')

        process = sp.run(cmd, shell=True, check=True, stdout=sp.PIPE, universal_newlines=True)
        runtime_meta = json.loads(process.stdout.strip())
        return runtime_meta

    def run(self, job_payload, job_filename):
        """
        Runs a job
        """
        executor_id = job_payload['executor_id']
        job_id = job_payload['job_id']
        total_calls = len(job_payload['call_ids'])

        logger.debug(f'ExecutorID {executor_id} | JobID {job_id} - Going to '
                     f'run {total_calls} activations in the localhost worker')

        if not os.path.isfile(RUNNER):
            self.setup()

        cmd = (f'docker run --rm -v {TEMP}:/tmp --entrypoint "python3" '
               f'{self.runtime} /tmp/lithops/runner.py run {job_filename}')

        log = open(RN_LOG_FILE, 'a')
        process = sp.Popen(cmd, shell=True, stdout=log, stderr=log)
        return process


class DefaultEnv(BaseEnv):
    """
    Default environment uses current python3 installation
    """
    def __init__(self):
        logger.debug(f'Starting Default Environment for {sys.executable}')
        super().__init__(runtime=sys.executable)

    def setup(self):
        logger.debug(f'Setting up Default environment')
        self._copy_lithops_to_tmp()

    def preinstalls(self):
        if not os.path.isfile(RUNNER):
            self.setup()
        cmd = f'"{self.runtime}" "{RUNNER}" preinstalls'
        process = sp.run(cmd, shell=True, check=True, stdout=sp.PIPE, universal_newlines=True)
        runtime_meta = json.loads(process.stdout.strip())
        return runtime_meta

    def run(self, job_payload, job_filename):
        """
        Runs a job
        """
        executor_id = job_payload['executor_id']
        job_id = job_payload['job_id']
        total_calls = len(job_payload['call_ids'])

        logger.debug(f'ExecutorID {executor_id} | JobID {job_id} - Going to '
                     f'run {total_calls} activations in the localhost worker')

        if not os.path.isfile(RUNNER):
            self.setup()

        cmd = f'"{self.runtime}" "{RUNNER}" run {job_filename}'
        log = open(RN_LOG_FILE, 'a')
        process = sp.Popen(cmd, shell=True, stdout=log, stderr=log)
        return process
