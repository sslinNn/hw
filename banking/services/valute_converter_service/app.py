import redis
import json
from kafka import KafkaConsumer, KafkaProducer

r = redis.Redis(host='localhost', port=6379, db=0)
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    transaction = message.value
    currency = transaction['currency']
    amount = transaction['amount']

    exchange_rate = float(r.get(currency) or 1.0)
    converted_amount = amount * exchange_rate

    print(f"Converted {amount} {currency} to {converted_amount} USD")
    transaction['converted_amount'] = converted_amount

    producer.send('converted_transactions', transaction)