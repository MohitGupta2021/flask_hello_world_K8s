# Kubernetes Hello World
A Kubernetes Hello World Project for Python Flask.  This project uses [a simple Flask app that returns correct change](https://github.com/noahgift/flask-change-microservice) as the base project and converts it to Kubernetes.
![kubernetes-load-balanced-cluster](https://user-images.githubusercontent.com/58792/111511557-3f45a280-8725-11eb-8e4a-5f5ef787796d.png)

This recipe is in the book Practical MLOps.
(https://user-images.githubusercontent.com/58792/111000927-eb1b7680-8350-11eb-8e24-d41064590fc1.jpeg)


## Assets in Repo

* `Makefile`:  [Builds project](https://github.com/noahgift/kubernetes-hello-world-python-flask/blob/main/Makefile)
* `Dockerfile`:  [Container configuration](https://github.com/noahgift/kubernetes-hello-world-python-flask/blob/main/Dockerfile)
* `app.py`:  [Flask app](https://github.com/noahgift/kubernetes-hello-world-python-flask/blob/main/app.py)
* `kube-hello-change.yaml`: [Kubernetes YAML Config](https://github.com/noahgift/kubernetes-hello-world-python-flask/blob/main/kube-hello-change.yaml)

## Get Started

* Create Python virtual environment `python3 -m venv ~/.kube-hello && source ~/.kube-hello/bin/activate`
* Run `make all` to install python libraries, including `Dockerfile`,Kubernates config file and run tests

## Build and Run Docker Container

* Install [Docker Desktop](https://www.docker.com/products/docker-desktop)

* To build the image locally do the following.

`docker build -t flask-change:latest .` or run `make build` which has the same command.

* To verify container run `docker image ls`

* To run do the following:  `docker run -p 8080:8080 flask-change` or run `make run` which has the same command


`curl http://127.0.0.1:8080/change/1/34`

```bash
[
  {
    "5": "quarters"
  }, 
  {
    "1": "nickels"
  }, 
  {
    "4": "pennies"
  }
]
```

* Stop the running docker container by using `control-c` command

## Running Kubernetes Locally

* Verify Kubernetes is working via docker-desktop context

```bash
* using minikube(local kubernates)

*1. To start minikube(local Kubernates)

(.kube-hello) ➜   minikube start
*2. For working with local kubernates(minikube) load the image docker image 
(.kube-hello) ➜minikube image load flask-change:latest


*3 Run the application in Kubernetes using the following command which tells Kubernetes to setup the different services .
 <!-- for applying the configurations -->
(.kube-hello) ➜ kubectl apply -f deployment.yaml
(.kube-hello) ➜ kubectl apply -f service.yaml


*4 Verify the container is running

`kubectl get pods`
<!-- To check the service details use  -->
(.kube-hello) ➜ kubectl get svc hello-flask-change-service


Here is the output:

NAME                                                READY   STATUS    RESTARTS   AGE

hello-python-58584c84b5-6s4jd                       1/1     Running   0          52m
hello-python-58584c84b5-k4f84                       1/1     Running   0          52m
hello-python-58584c84b5-pbfhb                       1/1     Running   0          52m


*5 To check the minikube services is running or not 

 <!-- minikube service hello-flask-change-service -->
 (.kube-hello) ➜  minikube service hello-flask-change-service

---------------|-------------|---------------------------|
| NAMESPACE |            NAME            | TARGET PORT |            URL            |
|-----------|----------------------------|-------------|---------------------------|
| default   | hello-flask-change-service |        8080 | http://192.168.49.2:31967 |
|-----------|----------------------------|-------------|---------------------------|
* Opening service default/hello-flask-change-service in default browser...
  http://192.168.49.2:3196

*6-- to check the api is working file or not Invoke the endpoint to curl it: 

 (.kube-hello) ➜ curl http://192.168.49.2:31967/change/1/25
[
  {
    "quarters": 5
  }
]


*7 -- To test the api  --
`(.kube-hello) ➜ python test_app.py
<!-- output will be like this ---->

Make Change for 1.25
.I am inside hello world
.
----------------------------------------------------------------------
Ran 2 tests in 0.015s

*8 -- To test the load using locust 

`(.kube-hello) ➜locust -f locustfile.py
<!-- open the running server  and calculate the load or do analyis  -->

*9 For Graphicals tools 
<!-- To use with Graffana or prothemous  -->
<!-- install the helm use these below commands for both   -->

`(.kube-hello) ➜helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
`(.kube-hello) ➜helm repo add grafana https://grafana.github.io/helm-charts
`(.kube-hello) ➜helm repo update
<!-- To run these  -->
(.kube-hello) ➜kubectl port-forward svc/prometheus-server 9090:80
(.kube-hello) ➜kubectl port-forward svc/grafana 3003:80 
  


*10 To cleanup the deployment do the following: 
(.kube-hello) ➜kubectl delete deployment hello-python`

## References

* Azure [Kubernetes deployment strategy](https://azure.microsoft.com/en-us/overview/kubernetes-deployment-strategy/)
* Service [Cluster Config](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/) YAML file
* [Kubernetes.io Hello World](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)
