import json
from kafka import TopicPartition, KafkaConsumer

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']

consumer = KafkaConsumer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    enable_auto_commit=False,
    group_id='fibonacci',
    api_version=(2, 5, 0),
)


def fibonacci(n: int) -> int:
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


partition = TopicPartition('fibonacci', 0)
partitions = [partition]
consumer.assign(partitions)
consumer.committed(partition)
for msg in consumer:
    data = json.loads(msg.value)
    number = data['number']
    print(fibonacci(number))
    consumer.commit()
