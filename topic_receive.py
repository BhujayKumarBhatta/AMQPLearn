#!/usr/bin/env pythoni
import pika
import sys

crdn = pika.PlainCredentials('rabbit', 'welcome@123')
connection = pika.BlockingConnection(pika.ConnectionParameters('uvm3', credentials=crdn))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

'''
shell 1: python topic_receive.py '#'
 [x] 'a.b.c.d':b'jjj'
 [x] 'a.b.c':b'jjj'
 [x] 'a.b.c':b'jjj'
 [x] 'a.b':b'jjj'

shell 2: python topic_receive.py '*.*'
[x] 'a.b':b'jjj'


shell 3:
python topic_send.py  "a.b.c.d" jjj
 python topic_send.py  "a.b.c" jjj
 python topic_send.py  a.b.c jjj
  python topic_send.py  a.b jjj
  

'''