from rstream import Consumer, amqp_decoder, AMQPMessage

# Create a consumer
consumer = Consumer(
      host='localhost',
      port=5552,
      username='guest',
      password='guest',
)

# More like a callback
def on_message(msg: AMQPMessage):
  print('Got message: {}'.format(msg.body))

consumer.start()
consumer.subscribe('mystream', on_message, decoder=amqp_decoder)
consumer.run()