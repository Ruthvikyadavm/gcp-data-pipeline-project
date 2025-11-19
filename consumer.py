from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "taxi_trips",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("🚀 Listening for messages on taxi_trips...\n")

for msg in consumer:
    print("Received:", msg.value)
