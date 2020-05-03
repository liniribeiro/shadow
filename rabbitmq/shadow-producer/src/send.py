import pika
from pika.credentials import PlainCredentials


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=PlainCredentials('user', 'password', erase_on_connect=False)))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Oi Alecio!')

print(" [x] Sent 'Hello World!'")
connection.close()