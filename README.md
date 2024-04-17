# Rabbitmq pub/sub example

Project example of pub/sub pattern and streams using RabbitMQ and Python.

## Description

A publisher python process produces a message that is received by a consumer python process and prints the message.

## Environment 

It uses a local RabbitMQ server. A different remote server could be used by providing the corresponding environment variable.

The python application uses pika as AMQP 0.9.1 protocol client library to connect with RabbitMQ server.
Rstream library is used for streams examples.

## QUEUE Example

**pubsub/publisher.py**
```bash
$ python3 publisher.py "this is a test"
 Message sent.
```

**pubsub/consumer.py**
```bash
$ python3 consumer.py 
 [*] Waiting for messages:
 [x] Received b'this is a test'
```