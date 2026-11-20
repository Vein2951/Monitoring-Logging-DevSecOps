from locust import HttpUser, task, between

class WebsiteUser(HttpUser):

    wait_time = between(1, 3)

    @task
    def visit_home(self):
        self.client.get("/")

    @task
    def check_health(self):
        self.client.get("/health")
