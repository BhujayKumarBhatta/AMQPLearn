#!/usr/bin/env python
import pika
import sys

crdn = pika.PlainCredentials('rabbit', 'welcome@123')
connection = pika.BlockingConnection(pika.ConnectionParameters('uvm3', credentials=crdn))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()