from oslo_config import cfg
import oslo_messaging as om
from pprint import pprint
import logging

logging.basicConfig()
log = logging.getLogger()

log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)


rabbit_group = cfg.OptGroup(name='rabbit',
                            title='RabbitMQ options')

opts = [
    cfg.StrOpt('rpc_backend'),
    cfg.StrOpt('rabbit_host'),
    cfg.PortOpt('rabbit_port'),
    cfg.StrOpt('rabbit_virtual_host'),
    cfg.StrOpt('rabbita_login_method'),
    cfg.StrOpt('rabbit_userid'),
    cfg.StrOpt('rabbit_password'),       
    ]
# 
#CONF = cfg.ConfigOpts()
CONF = cfg.CONF
CONF(['--config-file', 'rabbit.conf'])
CONF.register_opts(opts)
#CONF.register_opts(opts, group=rabbit_group) # or
#CONF.register_opts(opts, group='rabbit'))


cfg.CONF.set_override('rpc_backend', 'rabbit')
cfg.CONF.set_override('rabbit_host', '192.168.111.39')
cfg.CONF.set_override('rabbit_port', 5672)
cfg.CONF.set_override('rabbit_virtual_host', '/')
cfg.CONF.set_override('rabbita_login_method', 'AMQPLAIN')
cfg.CONF.set_override('rabbit_userid', 'user1')
cfg.CONF.set_override('rabbit_password', 'welcome123')

res = [{k:v} for k,v in cfg.CONF.items()]
pprint(res)

#################RPCClient
transport = om.get_transport(cfg.CONF)
target = om.Target(topic = 'testme')
client = om.RPCClient(transport, target)

# Invoke remote method and wait for reply
arg = "Bhujay"
ctxt = {}
client.call(ctxt, 'test_method1', arg = arg)

#invoke remote method and return immediately
client.cast(ctxt, 'test_method1', arg = arg)



