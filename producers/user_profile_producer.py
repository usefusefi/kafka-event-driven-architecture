from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

user_profile = {
    "user_id": "user_123",
    "account_age_days": 365,
    "risk_score": 2  # 1 = Low, 5 = High
}
producer.send('user-profile-events', value=user_profile)
producer.flush()
