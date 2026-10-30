from kafka import KafkaProducer
import json
import time
import random

# Configuración del productor de Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Iniciando productor de sensores...")
while True:
    data = {
        "sensor_id": random.randint(1, 10),
        "temperature": round(random.uniform(15.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "timestamp": int(time.time())
    }
    producer.send('sensor_data', value=data)
    print(f"Sent: {data}")
    time.sleep(2)
