"""
    Delphix API Gateway

    Delphix API Gateway API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from delphix.api.gateway.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from delphix.api.gateway.model.base_provision_vdb_parameters import BaseProvisionVDBParameters
    from delphix.api.gateway.model.data_point_by_timestamp_parameters import DataPointByTimestampParameters
    from delphix.api.gateway.model.hook import Hook
    from delphix.api.gateway.model.provision_vdbby_timestamp_parameters_all_of import ProvisionVDBByTimestampParametersAllOf
    globals()['BaseProvisionVDBParameters'] = BaseProvisionVDBParameters
    globals()['DataPointByTimestampParameters'] = DataPointByTimestampParameters
    globals()['Hook'] = Hook
    globals()['ProvisionVDBByTimestampParametersAllOf'] = ProvisionVDBByTimestampParametersAllOf


class ProvisionVDBByTimestampParameters(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('recovery_model',): {
            'FULL': "FULL",
            'SIMPLE': "SIMPLE",
            'BULK_LOGGED': "BULK_LOGGED",
        },
    }

    validations = {
        ('source_data_id',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('engine_id',): {
        },
        ('target_group_id',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('vdb_name',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('database_name',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('username',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('password',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('environment_id',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('environment_user_id',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('repository_id',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('pre_refresh',): {
            'max_items': 100,
        },
        ('post_refresh',): {
            'max_items': 100,
        },
        ('pre_rollback',): {
            'max_items': 100,
        },
        ('post_rollback',): {
            'max_items': 100,
        },
        ('configure_clone',): {
            'max_items': 100,
        },
        ('pre_snapshot',): {
            'max_items': 100,
        },
        ('post_snapshot',): {
            'max_items': 100,
        },
        ('pre_start',): {
            'max_items': 100,
        },
        ('post_start',): {
            'max_items': 100,
        },
        ('pre_stop',): {
            'max_items': 100,
        },
        ('post_stop',): {
            'max_items': 100,
        },
        ('template_id',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('file_mapping_rules',): {
            'max_length': 131072,
            'min_length': 1,
        },
        ('oracle_instance_name',): {
            'max_length': 15,
            'min_length': 1,
            'regex': {
                'pattern': r'^[a-zA-Z0-9_]+$',  # noqa: E501
            },
        },
        ('unique_name',): {
            'max_length': 30,
            'min_length': 1,
            'regex': {
                'pattern': r'^[a-zA-Z0-9_\$#]+$',  # noqa: E501
            },
        },
        ('mount_point',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('snapshot_policy_id',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('retention_policy_id',): {
            'max_length': 256,
            'min_length': 1,
        },
        ('pre_script',): {
            'max_length': 1024,
            'min_length': 1,
        },
        ('post_script',): {
            'max_length': 1024,
            'min_length': 1,
        },
        ('online_log_size',): {
            'inclusive_minimum': 4,
        },
        ('online_log_groups',): {
            'inclusive_minimum': 2,
        },
        ('timestamp_in_database_timezone',): {
            'regex': {
                'pattern': r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(.[0-9]{0,3})?',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'source_data_id': (str,),  # noqa: E501
            'engine_id': (int,),  # noqa: E501
            'target_group_id': (str,),  # noqa: E501
            'vdb_name': (str,),  # noqa: E501
            'database_name': (str,),  # noqa: E501
            'truncate_log_on_checkpoint': (bool,),  # noqa: E501
            'username': (str,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'environment_id': (str,),  # noqa: E501
            'environment_user_id': (str,),  # noqa: E501
            'repository_id': (str,),  # noqa: E501
            'auto_select_repository': (bool,),  # noqa: E501
            'pre_refresh': ([Hook],),  # noqa: E501
            'post_refresh': ([Hook],),  # noqa: E501
            'pre_rollback': ([Hook],),  # noqa: E501
            'post_rollback': ([Hook],),  # noqa: E501
            'configure_clone': ([Hook],),  # noqa: E501
            'pre_snapshot': ([Hook],),  # noqa: E501
            'post_snapshot': ([Hook],),  # noqa: E501
            'pre_start': ([Hook],),  # noqa: E501
            'post_start': ([Hook],),  # noqa: E501
            'pre_stop': ([Hook],),  # noqa: E501
            'post_stop': ([Hook],),  # noqa: E501
            'vdb_restart': (bool,),  # noqa: E501
            'template_id': (str,),  # noqa: E501
            'file_mapping_rules': (str,),  # noqa: E501
            'oracle_instance_name': (str,),  # noqa: E501
            'unique_name': (str,),  # noqa: E501
            'mount_point': (str,),  # noqa: E501
            'open_reset_logs': (bool,),  # noqa: E501
            'snapshot_policy_id': (str,),  # noqa: E501
            'retention_policy_id': (str,),  # noqa: E501
            'recovery_model': (str,),  # noqa: E501
            'pre_script': (str,),  # noqa: E501
            'post_script': (str,),  # noqa: E501
            'cdc_on_provision': (bool,),  # noqa: E501
            'online_log_size': (int,),  # noqa: E501
            'online_log_groups': (int,),  # noqa: E501
            'archive_log': (bool,),  # noqa: E501
            'new_dbid': (bool,),  # noqa: E501
            'listener_ids': ([str],),  # noqa: E501
            'custom_env_vars': ({str: (str,)},),  # noqa: E501
            'custom_env_files': ([str],),  # noqa: E501
            'timestamp': (datetime,),  # noqa: E501
            'timestamp_in_database_timezone': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'source_data_id': 'source_data_id',  # noqa: E501
        'engine_id': 'engine_id',  # noqa: E501
        'target_group_id': 'target_group_id',  # noqa: E501
        'vdb_name': 'vdb_name',  # noqa: E501
        'database_name': 'database_name',  # noqa: E501
        'truncate_log_on_checkpoint': 'truncate_log_on_checkpoint',  # noqa: E501
        'username': 'username',  # noqa: E501
        'password': 'password',  # noqa: E501
        'environment_id': 'environment_id',  # noqa: E501
        'environment_user_id': 'environment_user_id',  # noqa: E501
        'repository_id': 'repository_id',  # noqa: E501
        'auto_select_repository': 'auto_select_repository',  # noqa: E501
        'pre_refresh': 'pre_refresh',  # noqa: E501
        'post_refresh': 'post_refresh',  # noqa: E501
        'pre_rollback': 'pre_rollback',  # noqa: E501
        'post_rollback': 'post_rollback',  # noqa: E501
        'configure_clone': 'configure_clone',  # noqa: E501
        'pre_snapshot': 'pre_snapshot',  # noqa: E501
        'post_snapshot': 'post_snapshot',  # noqa: E501
        'pre_start': 'pre_start',  # noqa: E501
        'post_start': 'post_start',  # noqa: E501
        'pre_stop': 'pre_stop',  # noqa: E501
        'post_stop': 'post_stop',  # noqa: E501
        'vdb_restart': 'vdb_restart',  # noqa: E501
        'template_id': 'template_id',  # noqa: E501
        'file_mapping_rules': 'file_mapping_rules',  # noqa: E501
        'oracle_instance_name': 'oracle_instance_name',  # noqa: E501
        'unique_name': 'unique_name',  # noqa: E501
        'mount_point': 'mount_point',  # noqa: E501
        'open_reset_logs': 'open_reset_logs',  # noqa: E501
        'snapshot_policy_id': 'snapshot_policy_id',  # noqa: E501
        'retention_policy_id': 'retention_policy_id',  # noqa: E501
        'recovery_model': 'recovery_model',  # noqa: E501
        'pre_script': 'pre_script',  # noqa: E501
        'post_script': 'post_script',  # noqa: E501
        'cdc_on_provision': 'cdc_on_provision',  # noqa: E501
        'online_log_size': 'online_log_size',  # noqa: E501
        'online_log_groups': 'online_log_groups',  # noqa: E501
        'archive_log': 'archive_log',  # noqa: E501
        'new_dbid': 'new_dbid',  # noqa: E501
        'listener_ids': 'listener_ids',  # noqa: E501
        'custom_env_vars': 'custom_env_vars',  # noqa: E501
        'custom_env_files': 'custom_env_files',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'timestamp_in_database_timezone': 'timestamp_in_database_timezone',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, source_data_id, *args, **kwargs):  # noqa: E501
        """ProvisionVDBByTimestampParameters - a model defined in OpenAPI

        Args:
            source_data_id (str): The ID of the source object (dSource or VDB) to provision from. All other objects referenced by the parameters must live on the same engine as the source.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            engine_id (int): The ID of the Engine onto which to provision. If the source ID unambiguously identifies a source object, this parameter is unnecessary and ignored.. [optional]  # noqa: E501
            target_group_id (str): The ID of the group into which the VDB will be provisioned. If unset, a group is selected randomly on the Engine.. [optional]  # noqa: E501
            vdb_name (str): The unique name of the provisioned VDB within a group. If unset, a name is randomly generated.. [optional]  # noqa: E501
            database_name (str): The name of the database on the target environment. Defaults to vdb_name.. [optional]  # noqa: E501
            truncate_log_on_checkpoint (bool): Whether to truncate log on checkpoint (ASE only).. [optional]  # noqa: E501
            username (str): The name of the privileged user to run the provision operation (Oracle Only).. [optional]  # noqa: E501
            password (str): The password of the privileged user to run the provision operation (Oracle Only).. [optional]  # noqa: E501
            environment_id (str): The ID of the target environment where to provision the VDB. If repository_id unambigously identifies a repository, this is unnecessary and ignored. Otherwise, a compatible repository is randomly selected on the environment.. [optional]  # noqa: E501
            environment_user_id (str): The environment user ID to use to connect to the target environment.. [optional]  # noqa: E501
            repository_id (str): The ID of the target repository where to provision the VDB. A repository typically corresponds to a database installation (Oracle home, database instance, ...). Setting this attribute implicitly determines the environment where to provision the VDB.. [optional]  # noqa: E501
            auto_select_repository (bool): Option to automatically select a compatible environment and repository. Mutually exclusive with repository_id.. [optional]  # noqa: E501
            pre_refresh ([Hook]): The commands to execute on the target environment before refreshing the VDB.. [optional]  # noqa: E501
            post_refresh ([Hook]): The commands to execute on the target environment after refreshing the VDB.. [optional]  # noqa: E501
            pre_rollback ([Hook]): The commands to execute on the target environment before rewinding the VDB.. [optional]  # noqa: E501
            post_rollback ([Hook]): The commands to execute on the target environment after rewinding the VDB.. [optional]  # noqa: E501
            configure_clone ([Hook]): The commands to execute on the target environment when the VDB is created or refreshed.. [optional]  # noqa: E501
            pre_snapshot ([Hook]): The commands to execute on the target environment before snapshotting a virtual source. These commands can quiesce any data prior to snapshotting.. [optional]  # noqa: E501
            post_snapshot ([Hook]): The commands to execute on the target environment after snapshotting a virtual source.. [optional]  # noqa: E501
            pre_start ([Hook]): The commands to execute on the target environment before starting a virtual source.. [optional]  # noqa: E501
            post_start ([Hook]): The commands to execute on the target environment after starting a virtual source.. [optional]  # noqa: E501
            pre_stop ([Hook]): The commands to execute on the target environment before stopping a virtual source.. [optional]  # noqa: E501
            post_stop ([Hook]): The commands to execute on the target environment after stopping a virtual source.. [optional]  # noqa: E501
            vdb_restart (bool): Indicates whether the Engine should automatically restart this virtual source when target host reboot is detected.. [optional]  # noqa: E501
            template_id (str): The ID of the target VDB Template (Oracle Only).. [optional]  # noqa: E501
            file_mapping_rules (str): Target VDB file mapping rules (Oracle Only). Rules must be line separated (\\n or \\r) and each line must have the format \"pattern:replacement\". Lines are applied in order.. [optional]  # noqa: E501
            oracle_instance_name (str): Target VDB SID name (Oracle Only).. [optional]  # noqa: E501
            unique_name (str): Target VDB db_unique_name (Oracle Only).. [optional]  # noqa: E501
            mount_point (str): Mount point for the VDB (Oracle, ASE Only).. [optional]  # noqa: E501
            open_reset_logs (bool): Whether to open the database after provision (Oracle Only).. [optional]  # noqa: E501
            snapshot_policy_id (str): The ID of the snapshot policy for the VDB.. [optional]  # noqa: E501
            retention_policy_id (str): The ID of the retention policy for the VDB.. [optional]  # noqa: E501
            recovery_model (str): Recovery model of the source database (MSSql Only).. [optional]  # noqa: E501
            pre_script (str): PowerShell script or executable to run prior to provisioning (MSSql Only).. [optional]  # noqa: E501
            post_script (str): PowerShell script or executable to run after provisioning (MSSql Only).. [optional]  # noqa: E501
            cdc_on_provision (bool): Option to enable change data capture (CDC) on both the provisioned VDB and subsequent snapshot-related operations (e.g. refresh, rewind) (MSSql Only).. [optional]  # noqa: E501
            online_log_size (int): Online log size in MB (Oracle Only).. [optional]  # noqa: E501
            online_log_groups (int): Number of online log groups (Oracle Only).. [optional]  # noqa: E501
            archive_log (bool): Option to create a VDB in archivelog mode (Oracle Only).. [optional]  # noqa: E501
            new_dbid (bool): Option to generate a new DB ID for the created VDB (Oracle Only).. [optional]  # noqa: E501
            listener_ids ([str]): The listener IDs for this provision operation (Oracle Only).. [optional]  # noqa: E501
            custom_env_vars ({str: (str,)}): Environment variable to be set when the engine creates a VDB. See the Engine documentation for the list of allowed/denied environment variables and rules about substitution.. [optional]  # noqa: E501
            custom_env_files ([str]): Environment files to be sourced when the Engine creates a VDB. This path can be followed by parameters. Paths and parameters are separated by spaces.. [optional]  # noqa: E501
            timestamp (datetime): The point in time from which to execute the operation. Mutually exclusive with timestamp_in_database_timezone. If the timestamp is not set, selects the latest point.. [optional]  # noqa: E501
            timestamp_in_database_timezone (str): The point in time from which to execute the operation, expressed as a date-time in the timezone of the source database. Mutually exclusive with timestamp.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'source_data_id': source_data_id,
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              BaseProvisionVDBParameters,
              DataPointByTimestampParameters,
              ProvisionVDBByTimestampParametersAllOf,
          ],
          'oneOf': [
          ],
        }
