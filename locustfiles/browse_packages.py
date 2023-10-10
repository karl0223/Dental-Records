from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_packages(self):
        self.client.get('/clinic/packages/', name='/clinic/packages')

    @task(4)
    def view_package(self):
        package_id = randint(1, 10)
        self.client.get('/clinic/packages/{package_id}', name='/clinic/packages/:id')
