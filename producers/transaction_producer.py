from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    key_serializer=str.encode,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    compression_type='gzip',
    batch_size=16384,
    linger_ms=10
)

# Send simulated transaction events
transaction_data = {
    "user_id": "user_123",
    "transaction_id": "txn_456",
    "amount": 5000,
    "transaction_type": "withdrawal",
    "location": "ATM_123",
    "time": "2025-01-01T10:15:00Z"
}
producer.send('transaction-events', key=transaction_data["user_id"], value=transaction_data)
producer.flush()
