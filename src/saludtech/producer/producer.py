import time
import pulsar

def produce_messages():
    # Conexión al broker utilizando el hostname 'broker'
    client = pulsar.Client(f'pulsar://broker:6650', operation_timeout_seconds=10)
    producer = client.create_producer('my-topic')
    count = 0
    while True:
        message = f'Mensaje {count} desde Producer'
        producer.send(message.encode('utf-8'))
        print(f'Enviado: {message}')
        count += 1
        time.sleep(2)
    client.close()

if __name__ == '__main__':
    produce_messages()
