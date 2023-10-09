from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestCreatePackage:
    def test_if_user_is_anonymous_returns_401(self):
        client = APIClient()
        response = client.post('/clinic/packages/', {'title': 'a', 'package_type': 'A', 'price': 20000})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/clinic/packages/', {'title': 'a', 'package_type': 'A', 'price': 20000})

        assert response.status_code == status.HTTP_403_FORBIDDEN

