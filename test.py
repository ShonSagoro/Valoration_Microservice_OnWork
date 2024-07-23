import pika
import os
from dotenv import load_dotenv

def check_rabbitmq_connection():
    load_dotenv()
    hostname = "onwork-rabbit.integrador.xyz"
    user = os.getenv('RABBITMQ_USER')
    password = os.getenv('RABBITMQ_PASS')
    port = int(os.getenv('RABBITMQ_PORT', 5672))  # Default port is 5672 if not specified

    try:
        credentials = pika.PlainCredentials(user, password)
        parameters = pika.ConnectionParameters(hostname,port, '/', credentials)
        print(f"Trying to connect to RabbitMQ at {hostname}:{port}...")
        connection = pika.BlockingConnection(parameters)
        connection.close()
        
        print("Connection to RabbitMQ successful.")
    except Exception as e:
        print(f"Failed to connect to RabbitMQ: {e}")

if __name__ == "__main__":
    check_rabbitmq_connection()