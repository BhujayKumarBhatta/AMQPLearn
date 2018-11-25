import sys
import pika

crdn = pika.PlainCredentials('rabbit', 'welcome@123')
connection = pika.BlockingConnection(pika.ConnectionParameters('uvm3', credentials=crdn))
chnnel = connection.channel()
chnnel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or 'Hello World!'
chnnel.basic_publish(exchange='',routing_key='hello',body= message)
print('[x] Sent % r' % message)