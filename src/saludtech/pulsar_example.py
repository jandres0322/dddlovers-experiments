import pulsar

def main():
    # Conectar al broker Pulsar (asegúrate de haber levantado el clúster con docker-compose)
    client = pulsar.Client('pulsar://localhost:6650')
    
    # Crear un productor para el tópico 'my-topic'
    producer = client.create_producer('my-topic')
    
    # Crear un consumidor que se suscribe al mismo tópico con la suscripción 'my-subscription'
    consumer = client.subscribe('my-topic', subscription_name='my-subscription')
    
    # Enviar un mensaje
    mensaje = "Hola, Apache Pulsar en modo distribuido!"
    producer.send(mensaje.encode('utf-8'))
    print("Mensaje enviado:", mensaje)
    
    # Recibir el mensaje (timeout de 5 segundos)
    try:
        msg = consumer.receive(timeout_millis=5000)
        print("Mensaje recibido:", msg.data().decode('utf-8'))
        consumer.acknowledge(msg)
    except Exception as e:
        print("No se recibió ningún mensaje:", e)
    
    # Cerrar la conexión
    client.close()

if __name__ == '__main__':
    main()
