import json
import time
from kafka import KafkaProducer

# Load sample JSON
with open("sample_data.json", "r") as f:
    data = json.load(f)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Streaming messages to Kafka topic: taxi_trips")

for record in data:
    producer.send("taxi_trips", record)
    print("Sent:", record)
    time.sleep(1)  # 1 message per second

producer.flush()
print("✅ Finished sending sample events.")
