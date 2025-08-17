import os
import time
from kafka import KafkaProducer

WATCH_DIR = os.environ.get('WATCH_DIR', '/watched')  # Mount as a volume
KAFKA_BOOTSTRAP = os.environ.get('KAFKA_BOOTSTRAP', 'kafka:9092')
TOPIC = os.environ.get('KAFKA_TOPIC', 'new-files')

producer = KafkaProducer(bootstrap_servers=[KAFKA_BOOTSTRAP])
seen = set()

while True:
    for fname in os.listdir(WATCH_DIR):
        fpath = os.path.join(WATCH_DIR, fname)
        if fname not in seen and os.path.isfile(fpath):
            with open(fpath, 'r') as f:
                content = f.read()
            producer.send(TOPIC, value=content.encode('utf-8'), key=fname.encode('utf-8'))
            print(f"Sent {fname}")
            seen.add(fname)
    time.sleep(2)