from kafka import KafkaProducer
import json


KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']
KAFKA_RETRIES = 3
KAFKA_LINGER_MS = 1000

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         retries=KAFKA_RETRIES,
                         linger_ms=KAFKA_LINGER_MS,
                         api_version=(2, 5, 0),
                         )

producer.send(
    'fibonacci',
    { 'number': 10,}
)
producer.send(
    'fibonacci',
    { 'number': 100,}
)
producer.send(
    'fibonacci',
    { 'number': 56,}
)