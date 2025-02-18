# Kafka Best Practices for Banking & Finance

## ✅ 1. Use Separate Topics for Different Event Types
- `transaction-events`: Stores financial transactions.
- `fraud-alerts`: Stores alerts flagged by fraud detection.
- `user-profile-events`: Stores user metadata.

## ✅ 2. Enable Log Compaction for Storing Latest State
```bash
bin/kafka-topics.sh --create --topic user-fraud-status \
  --partitions 3 --replication-factor 2 --config cleanup.policy=compact \
  --bootstrap-server localhost:9092
