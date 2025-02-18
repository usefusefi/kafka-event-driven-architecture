from kafka import KafkaConsumer
import json
from smtplib import SMTP

consumer = KafkaConsumer(
    'fraud-alerts',
    group_id='fraud-notifications',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def send_email_alert(alert):
    with SMTP('smtp.example.com') as smtp:
        smtp.sendmail(
            'fraud-detection@example.com',
            'fraud-team@example.com',
            f"Subject: 🚨 Fraud Alert\n\nSuspicious activity detected:\n{alert['alert']}"
        )

for message in consumer:
    alert = message.value
    send_email_alert(alert)
