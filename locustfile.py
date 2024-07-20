from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello(self):
        self.client.get("/")

    @task
    def change(self):
        self.client.get("/change/1/25")
