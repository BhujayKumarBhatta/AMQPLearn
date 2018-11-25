import pika
import time

def callback(ch, method, properties, body):
  print(" [X] Received %r" %body)
  time.sleep(body.count(b'.'))
  print('[x] Done')

crdn = pika.PlainCredentials('rabbit', 'welcome@123')
connection = pika.BlockingConnection(pika.ConnectionParameters('uvm3', credentials=crdn))
chnnel = connection.channel()
chnnel.queue_declare(queue='hello')
chnnel.basic_consume(callback, queue='hello', no_ack=True)
chnnel.start_consuming()