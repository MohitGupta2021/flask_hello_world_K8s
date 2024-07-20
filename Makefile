install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt



test:
	python test_app.py

build:
	docker build -t flask-change:latest .

run:
	docker run -p 8080:8080 flask-change

invoke:

	curl http://192.168.49.2:31967/change/1/25

run-kube:
	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml

run-locust:
	locust -f locustfile.py


all: install lint test