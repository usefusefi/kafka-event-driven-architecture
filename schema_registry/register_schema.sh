curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
  --data '{"schema": "{\"type\":\"record\",\"name\":\"Transaction\",\"fields\":[{\"name\":\"user_id\",\"type\":\"string\"},{\"name\":\"transaction_id\",\"type\":\"string\"},{\"name\":\"amount\",\"type\":\"double\"},{\"name\":\"transaction_type\",\"type\":\"string\"},{\"name\":\"location\",\"type\":\"string\"},{\"name\":\"time\",\"type\":\"string\"}]}"}' \
  http://localhost:8081/subjects/transaction-events-value/versions
