# Kafka-embedding-service  
  
Kafka service to embed any new files in a folder with SBERT.  
  
## Embedding Pipeline: Kafka Producer & Consumer  
  
This project uses a Kafka-based pipeline to process text files:  
  
- **Producer:** Watches a directory, sends new files to Kafka    
- **Consumer:** Reads messages from Kafka, encodes with SentenceTransformer, saves embeddings  
  
### Project Structure  
  

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


Start minikube 
`
minikube start  
`

Build docker images
`
docker build -t consumer:latest .
docker build -t producer:latest .
`

Enable the Docker Environment in Minikube

`eval $(minikube docker-env)`

Deploy Kafka to Minikube

`kubectl apply -f k8s/kafka-deployment.yaml`
Wait for Kafka to be running: `kubectl get pods`

Deploy Producer and Consumer

`kubectl apply -f k8s/app-deployments.yaml`

Add a file to the producer's watched directory:
`kubectl exec -it $(kubectl get pods -l app=producer -o jsonpath="{.items[0].metadata.name}") -- touch /watched/testfile.txt` 

Check for output in the consumer's output directory:
`kubectl exec -it $(kubectl get pods -l app=consumer -o jsonpath="{.items[0].metadata.name}") -- ls /rm-embeddings`

View consumer logs
`kubectl logs $(kubectl get pods -l app=consumer -o jsonpath="{.items[0].metadata.name}")  `

Clean Up
`minikube delete `
