import json
from kafka import KafkaConsumer

# Consume transactions from Kafka in Jupyter Notebook
consumer = KafkaConsumer(
    'transaction-events',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(f"Received transaction: {message.value}")
