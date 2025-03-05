import pulsar

def main():
    # Nos conectamos al broker usando la URL interna
    client = pulsar.Client('pulsar://broker:6650', operation_timeout_seconds=10)
    # Nos suscribimos al tópico "my-topic" con la suscripción "my-subscription"
    consumer = client.subscribe('my-topic', subscription_name='my-subscription')

    while True:
        msg = consumer.receive()
        print("Mensaje recibido:", msg.data().decode('utf-8'))
        consumer.acknowledge(msg)

    client.close()

if __name__ == '__main__':
    main()
