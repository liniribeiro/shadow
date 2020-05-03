import pika
from pika import PlainCredentials

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=PlainCredentials('user', 'password', erase_on_connect=False)))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()