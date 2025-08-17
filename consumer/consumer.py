from kafka import KafkaConsumer
from sentence_transformers import SentenceTransformer
import numpy as np
import os

KAFKA_BOOTSTRAP = os.environ.get('KAFKA_BOOTSTRAP', 'kafka:9092')
TOPIC = os.environ.get('KAFKA_TOPIC', 'new-files')
OUT_DIR = os.environ.get('OUT_DIR', '/rm-embeddings')  # Mount this as a volume

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[KAFKA_BOOTSTRAP],
    group_id='embed-group',
    auto_offset_reset='earliest'
)

model = SentenceTransformer('all-MiniLM-L6-v2')
print("Consumer started and waiting for messages...", flush=True)
for msg in consumer:
    fname = msg.key.decode('utf-8')
    text = msg.value.decode('utf-8')
    emb = model.encode(text)
    np.save(os.path.join(OUT_DIR, fname + '.npy'), emb)
    print(f"Embedded {fname}", flush=True)
