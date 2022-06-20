# Puzzle creater and anagram solver

## How to deploy in Kubernetes

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

## How to deploy in Docker

run `docker build . -t pslytestcode`
run `docker run -dp 80:5000 pslytestcode`
Then goto the URL where the docker-machine is ran. You can figure that out by running `docker-machine env` if you setup docker in a VM. For me it is http://192.168.99.100/ by default
Then you can use the above endpoints with this URL.
