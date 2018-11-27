# NOTE(changzhi): We are using eventlet executor and
# time.sleep(1), therefore, the server code needs to be
# monkey-patched.

import eventlet
eventlet.monkey_patch()

from oslo_config import cfg
import oslo_messaging
import time

class ServerControlEndpoint(object):

    target = oslo_messaging.Target(namespace='control',
                                   version='2.0')

    def __init__(self, server):
        self.server = server

    def stop(self, ctx):
        if self.server:
            self.server.stop()

class TestEndpoint(object):

    def test(self, ctx, arg):
        return arg

transport = oslo_messaging.get_rpc_transport(cfg.CONF)
target = oslo_messaging.Target(topic='test', server='server1')
endpoints = [
    ServerControlEndpoint(None),
    TestEndpoint(),
]
server = oslo_messaging.get_rpc_server(transport, target, endpoints,
                                       executor='eventlet')
try:
    server.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping server")

server.stop()
server.wait()