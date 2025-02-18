from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer('transaction-events', group_id='fraud-detection', bootstrap_servers=['localhost:9092'])
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for message in consumer:
    event = message.value
    processed_event = process_event(event)  # Fraud detection logic
    producer.send('fraud-alerts', value=processed_event)
