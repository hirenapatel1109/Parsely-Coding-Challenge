# Puzzle creater and anagram solver

## How to deploy

### Install Minikube (if running locally)

- Follow instructions here: https://minikube.sigs.k8s.io/docs/start/

### Apply Kubernetes deployment file

run `kubectl apply -f deployment_kubernetes.yaml`
This will deploy the kubernetes

- Ingress
- Service
- Deployment
- Pods (3 replicas)

### Access the website

_Keep in mind that the URL depends on how you set it up. If you use minikube and your minikube cluster runs on http://192.168.99.102/ locally, go to this website_

You can try the following endpoints:

- http://192.168.99.102/anagrams?prompt=pots
- http://192.168.99.102/generatePuzzle?difficulty=2
- http://192.168.99.102/verify?puzzle=ENOBOPIHAISM&guess=AMBIOPHONIES
