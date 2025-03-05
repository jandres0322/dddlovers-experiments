import pulsar

def consume_messages():
    client = pulsar.Client(f'pulsar://localhost:6650', operation_timeout_seconds=10)
    consumer = client.subscribe('my-topic', subscription_name='my-subscription')
    while True:
        msg = consumer.receive()
        try:
            print(f'Recibido: {msg.data().decode("utf-8")}')
            consumer.acknowledge(msg)
        except Exception as e:
            consumer.negative_acknowledge(msg)
            print(f'Error: {e}')
    client.close()

if __name__ == '__main__':
    consume_messages()
