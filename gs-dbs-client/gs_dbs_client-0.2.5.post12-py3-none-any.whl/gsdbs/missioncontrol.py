import http.client as httplib
import random
from datetime import datetime
import websocket
import string
from threading import Thread
import json
import requests
import asyncio
from multiprocessing.dummy import Pool
import zlib
from twisted.internet import task, reactor
import uuid
""" SockJS Client class  """


def fire_and_forget(f):
    def wrapped(*args, **kwargs):
        if asyncio.get_event_loop().is_closed():
            asyncio.set_event_loop(asyncio.new_event_loop())
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)

    return wrapped


class MissionControl(Thread):
    _wait_thread = 0
    _prefix = ""
    _host = ""
    _port = 80

    def __init__(self, cnode, prefix, gsdbs, userInfoURL, execute, heartbeat, heartbeatintervall=10, host="localhost",
                 port=8081):
        self._mandantname = ""
        self.counter = 0
        self._host = host
        self._port = port
        self.cnode = cnode
        self._gsdbs = gsdbs
        self._prefix = prefix
        self.execute = execute
        self.heartbeat = heartbeat
        self.userInfoURL = userInfoURL
        self.heartbeatintervall = heartbeatintervall * 1000
        self.loop = self.getEventLoop()
        Thread.__init__(self)
        self.connect()

    def connect(self):
        self.get_socket_info()
        self.start()

    def disconnect(self):
        pass

    def run(self):

        self._r1 = str(random.randint(0, 1000))
        self._conn_id = self.random_str(8)
        websocket.enableTrace(False)
        self._ws = websocket.WebSocketApp(
            ("ws://" if "localhost" in self._host else "wss://")
            + self._host + ":" + str(self._port) +
            self._prefix +
            "/" +
            self._r1 +
            "/" +
            self._conn_id +
            "/websocket?access_token=" +
            self._gsdbs.accessToken['access_token'],

            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close)

        self._ws.run_forever()

    def get_socket_info(self):
        conn = 0
        try:
            if self._port == 8081:
                conn = httplib.HTTPConnection(self._host, self._port)
            else:
                conn = httplib.HTTPSConnection(self._host, self._port)

            print(" Getting info from ", self._host)
            conn.request('GET', self._prefix + '/info',
                         headers={"Authorization": "Bearer " + self._gsdbs.accessToken['access_token']
                                  # , "Origin": "https://glass-sphere-ai.de"
                                  }
                         )
            response = conn.getresponse()
            print("INFO", response.status, response.reason, response.read())

        except  Exception as e:
            print(e)
        finally:
            if not conn: conn.close()

    def on_message(self, ws, message):
        self.processMessage(message)

    def getEventLoop(self):
        if asyncio.get_event_loop().is_closed():
            asyncio.set_event_loop(asyncio.new_event_loop())
        return asyncio.get_event_loop()

    @fire_and_forget
    def processMessage(self, message):
        if message == 'a["\\n"]':
            print("beat:" + datetime.now().strftime("%H:%M:%S"))
            self._ws.send('["\\n"]')
            self.counter = self.counter + 1
            # if self.counter % self.heartbeatintervall == 0:
            self.ETHome()
            # self.counter = 0

        if message == "o":
            pass
        if message.startswith("a"):
            if "{" in message:
                try:
                    print("Received")
                    mssgbdy = json.loads(
                        message[message.find("{"):message.find("\\u0000")].replace("\\\"", "\"").replace("\\n",
                                                                                                         " ").replace(
                            "\\r", " ").replace("\\t", " "))
                    self.execute(self._gsdbs, mssgbdy, self.onNext)
                    if self.str2bool(mssgbdy["isComputingStep"]) and mssgbdy["computingstep"] != '':
                        self.markJobAsDone(mssgbdy["jobid"], mssgbdy["computingstep"])
                except Exception as e:
                    print("JobFailed")
                    self.markJobAsFailed(mssgbdy["jobid"])
                    print(e)
        else:
            pass

    def str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")

    def call_api(self, transactionid, send):

        # requests.post("http://" + self._host + ":" + str(self._port) + "/missioncontrol/onnext",
        #               json={"jobid": json["jobid"], "cnode": self.cnode, "data": data},
        #               headers={"Content-Type": "application/json",
        #                        "Authorization": "Bearer " + self._gsdbs.accessToken["access_token"]})



        self._ws.send("[\"BEGIN\\ntransaction:"+transactionid+"\\n\\n\\u0000\"]")

        x = 16388
        res = [send[y - x:y] for y in range(x, len(send) + x, x)]
        for x in res:
            self._ws.send("[\"" + x + "\"]")
        self._ws.send("[\"COMMIT\\ntransaction:"+transactionid+"\\n\\n\\u0000\"]")

    def on_success(self, r):
        print('Post succeed')

    def on_errorPost(self, error):
        print('Post requests failed')

    def onNext(self, pool, json1, data):
        try:
            data["mandantname"] = self._mandantname
            data["streamkey"] = json1["streamkey"]

            # rq = requests.post("http://" + self._host + ":" + str(self._port) + "/missioncontrol/onnext",
            #                    json={"jobid": json["jobid"], "cnode": self.cnode, "data": data},
            #                    headers={"Content-Type": "application/json",
            #                             "Authorization": "Bearer " + self._gsdbs.accessToken["access_token"]})

            url = "http://" + self._host + ":" + str(self._port) + "/missioncontrol/onnext"
            json2 = {"jobid": json1["jobid"], "computingstep": json1["computingstep"], "cnode": self.cnode,
                     "data": data}
            headers = {"Content-Type": "application/json",
                       "Authorization": "Bearer " + self._gsdbs.accessToken["access_token"]}

            datastring = json.dumps(json2).replace("\"", "\\\"")




            # send = '\"SEND\\ndestination:/queue/onnext\\ncontent-length:56\\n\\n{\\"jobid\\":\\"1\\",\\"computingstep\\":\\"1\\",\\"cnode\\":\\"1\\",\\"data\\":\\"1\\"}\\u0000\"'

            # transactionid = self.random_str(8)
            transactionid = 'tx-'+self.random_str(8)
            send = 'SEND\\ndestination:/queue/onnext\\ndurable:false\\nexclusive:false\\nauto-delete:false\\n\\n' + datastring + '\\u0000'
            # self._ws.send("[\"" + x + "\"]")
            self.call_api(transactionid,send)
            # pool.apply_async(self.call_api, args=[transactionid,send],
            #                  callback=self.on_success, error_callback=self.on_errorPost)

            # if rq.status_code == 401:
            #     self._gsdbs.refreshToken()
            #     self.onNext(json, data)
        except Exception as e:
            return e

    def utf8len(self, s):

        encoded_string = s.encode('utf-8')
        byte_array = bytearray(s)

        return len(s.encode('utf-8'))

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):

        print("### closed:" + datetime.now().strftime("%H:%M:%S") + "###")

    def on_open(self, ws):
        connect = '\"CONNECT\\naccept-version:1.2,1.0\\nheart-beat:' + str(self.heartbeatintervall) + ',' + str(
            self.heartbeatintervall) + '\\nauto-delete:true\\nexclusive:true\\n\\n\\u0000\"'
        self._ws.send("[" + connect + "]")
        sub = f'\"SUBSCRIBE\\nid:{self.random_str(4)}\\ndestination:/queue/{self.getQueue()}\\n\\n\\u0000\"'
        # sub = f'\"SUBSCRIBE\\nid:{self.random_str(4)}\\ndestination:/queue/detector\\n\\n\\u0000\"'
        self._ws.send("[" + sub + "]")
        self.ETHome()
        print("open:" + datetime.now().strftime("%H:%M:%S"))

    def ETHome(self):
        self.heartbeat(self._gsdbs, self.cnode)

    def getQueue(self):
        headers = {'Authorization': 'Bearer ' + self._gsdbs.accessToken['access_token']}
        try:
            resp = requests.get(self.userInfoURL, headers=headers)
            resp.raise_for_status()
            userinfo = resp.json()
            self._mandantname = userinfo["mandant"]["mandantName"]
            return userinfo["mandant"]["mandantName"] + "-" + self.cnode + "-" + self._conn_id
        except:
            return ""

    def random_str(self, length):
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for c in range(length))

    def random_char(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for c in range(length))

    def random_number(self, length):
        letters = string.digits
        return ''.join(random.choice(letters) for c in range(length))

    def markJobAsDone(self, jobid, computingstep):
        self._gsdbs.executeStatement(f"""
                mutation{{
                        updateDTable(
                  dtablename: gsasyncjob,
                   where: [
                      {{connective: BLANK, column: gsasyncjob_jobid, operator: EQUAL, value: "{jobid}"}}
                        {{connective: AND, column: gsasyncjob_computingstep, operator: EQUAL, value: "{computingstep}"}}
                  ],
                  updatelist:[
                    {{datalink:gsasyncjob_jobstatus,value:"finished"}}
                  ]
                )
                }}
            """)

        requests.post("http://" + self._host + ":" + str(self._port) + "/missioncontrol/job",
                      json={"jobid": jobid, "cnode": computingstep},
                      headers={"Content-Type": "application/json",
                               "Authorization": "Bearer " + self._gsdbs.accessToken["access_token"]})
        print("job done")

    def markJobAsFailed(self, jobid):
        self._gsdbs.executeStatement(f"""
                mutation{{
                        updateDTable(
                  dtablename:"gsasyncjob",
                   where: [
                      {{connective: BLANK, column: gsasyncjob_jobid, operator: EQUAL, value: "{jobid}"}}
                        {{connective: AND, column: gsasyncjob_cnode, operator: EQUAL, value: "{self.cnode}"}}
                  ],
                  updatelist:[
                    {{datalink:gsasyncjob_jobstatus,value:"failed"}}
                  ]
                )
                }}
            """)


class MissionControlClient:

    def __init__(self, cnode, execute, heartBeat, gsdbs):
        self.cnode = cnode
        self.execute = execute
        self.gsdbs = gsdbs
        self.client = None
        self.heartBeat = heartBeat
        self.init()

    def createClient(self):
        self.client = MissionControl(self.cnode,
                                     '/gs-guide-websocket',
                                     self.gsdbs,
                                     "https://ens-fiti.de/user/info",
                                     self.execute,
                                     self.heartBeat,
                                     60
                                     )
        # , "glass-sphere-ai.de", 443)

    def checkThreadRunning(self):
        if self.client is None or not self.client.is_alive():
            self.gsdbs.refreshToken()
            reactor.callFromThread(self.createClient)

    def init(self):
        l = task.LoopingCall(self.checkThreadRunning)
        l.start(1.0)
        reactor.run()
