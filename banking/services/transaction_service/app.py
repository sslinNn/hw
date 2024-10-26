import json
from kafka import KafkaConsumer
import psycopg2

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

conn = psycopg2.connect(database="banking_db", user="user", password="password", host="localhost", port="5432")
cursor = conn.cursor()

for message in consumer:
    transaction = message.value
    cursor.execute("INSERT INTO transactions (amount, currency) VALUES (%s, %s)", (transaction['amount'], transaction['currency']))
    conn.commit()
    print(f"Processed transaction: {transaction}")