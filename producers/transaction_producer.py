from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transaction_data = {
    "user_id": "user_123",
    "transaction_id": "txn_456",
    "amount": 5000,
    "transaction_type": "withdrawal",
    "location": "ATM_123",
    "time": "2025-01-01T10:15:00Z"
}

# Send the transaction event to Kafka
producer.send('transaction-events', value=transaction_data)
