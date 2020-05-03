import sys

import pika
from pika import PlainCredentials

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=PlainCredentials('user', 'password', erase_on_connect=False)))
channel = connection.channel()


channel.queue_declare(queue='hello', durable=True)


message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent %r" % message)