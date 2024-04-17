from rstream import Producer, AMQPMessage

# Create a producer
producer = Producer(
  host='localhost',
  port=5552,
  username='guest',
  password='guest'
)

# Create a Stream named 'mystream'
producer.create_stream('mystream')

# Construct the message
message = AMQPMessage(
  body='hello world'
)

# Publish the message
producer.publish('mystream', amqp_message)