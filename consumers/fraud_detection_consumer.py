from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    'transaction-events',
    group_id='fraud-detection-group',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def detect_fraud(transaction):
    # Example fraud rule: Large transactions in different locations within minutes
    if transaction["amount"] > 5000:
        return True
    return False

for message in consumer:
    transaction = message.value
    if detect_fraud(transaction):
        alert_data = {
            "transaction_id": transaction["transaction_id"],
            "user_id": transaction["user_id"],
            "alert": "Suspicious transaction detected"
        }
        producer.send('fraud-alerts', value=alert_data)
