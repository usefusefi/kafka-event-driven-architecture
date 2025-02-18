from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'transaction-events',
    group_id='fraud-detection-group',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    transaction = message.value
    fraud_status = detect_fraud(transaction)  # Machine learning model or predefined rules
    
    if fraud_status:
        alert_data = {
            "transaction_id": transaction['transaction_id'],
            "user_id": transaction['user_id'],
            "alert": "Suspicious transaction detected"
        }
        producer.send('fraud-alerts', value=alert_data)
