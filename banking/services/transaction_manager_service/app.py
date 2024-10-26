from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    transaction = {
        'amount': data['amount'],
        'currency': data['currency'],
    }
    producer.send('transactions', transaction)
    return jsonify({'status': 'Transaction sent to Kafka'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)