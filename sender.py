import pika

ccrdn = pika.PlainCredentials('rabbit', 'welcome@123')

connection = pika.BlockingConnection(pika.ConnectionParameters('uvm3', credentials=crdn))

chnnel = connection.channel()

chnnel.queue_declare(queue='hello')

chnnel.basic_publish(exchange='', routing_key='hello', body='hello bhujay')

####################################################################################

def callback(ch, method, properties, body):
  print(" [X] Received %r" %body)

channel.basic_consume(callback, queue='hello', no_ack=true)

chnnel.start_consuming()
