# Kafka-embedding-service
Kafka service to embed any new files in a folder with SBERT


Embedding Pipeline: Kafka Producer & Consumer
This project uses a Kafka-based pipeline to process text files:

Producer: Watches a directory, sends new files to Kafka
Consumer: Reads messages from Kafka, encodes with SentenceTransformer, saves embeddings


embedding_pipeline/  
├── producer/  
│   ├── producer.py  
│   └── requirements.txt  
├── consumer/  
│   ├── consumer.py  
│   └── requirements.txt  
├── Dockerfile.producer  
├── Dockerfile.consumer  
├── README.md  


```
Certainly! Here is your Quick Start in proper Markdown formatting, ready to copy and paste:


## Quick Start  
  
### 1. Build Docker Images  
  
**Producer:**  
```sh  
docker build -t my-producer -f Dockerfile.producer .  
Consumer:


docker build -t my-consumer -f Dockerfile.consumer .  
2. Push Images to Registry (if using Kubernetes)

docker tag my-producer <your-registry>/my-producer:latest  
docker tag my-consumer <your-registry>/my-consumer:latest  
  
docker push <your-registry>/my-producer:latest  
docker push <your-registry>/my-consumer:latest  
3. Deploy to Kubernetes
Update your Kubernetes manifests to use your image names and configure environment variables:

KAFKA_BOOTSTRAP: Kafka server address (e.g., kafka:9092)
KAFKA_TOPIC: Topic to send/read messages (e.g., new-files)
OUT_DIR: Directory to write embeddings (e.g., /rm-embeddings)
Apply manifests:


kubectl apply -f kafka.yaml  
kubectl apply -f producer-deployment.yaml  
kubectl apply -f consumer-deployment.yaml  
4. Test the Pipeline
Add a file to the producer's watched directory:


kubectl exec -it -n rm-embeddings <producer-pod-name> -- touch /watched/testfile.txt  
Check for output in the consumer's output directory:


kubectl exec -it -n rm-embeddings <consumer-pod-name> -- ls /rm-embeddings  
You should see something like testfile.txt.npy.

View consumer logs:


kubectl logs -n rm-embeddings <consumer-pod-name>  

  
--- 

```
