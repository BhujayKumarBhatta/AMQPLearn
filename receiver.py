import pika

def callback(ch, method, properties, body):
  print(" [X] Received %r" %body)


crdn = pika.PlainCredentials('rabbit', 'welcome@123')

connection = pika.BlockingConnection(pika.ConnectionParameters('uvm3', credentials=crdn))

chnnel = connection.channel()

chnnel.queue_declare(queue='hello')

channel.basic_consume(callback, queue='hello', no_ack=true)

chnnel.start_consuming()
