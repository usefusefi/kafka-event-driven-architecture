CREATE STREAM transaction_stream (user_id STRING, amount INT, location STRING, time STRING)
    WITH (KAFKA_TOPIC='transaction-events', VALUE_FORMAT='JSON');

CREATE TABLE flagged_transactions AS 
    SELECT user_id, SUM(amount) AS total_spent
    FROM transaction_stream 
    WINDOW TUMBLING (SIZE 10 MINUTES)
    GROUP BY user_id
    HAVING total_spent > 10000;
