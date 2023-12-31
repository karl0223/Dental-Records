from rest_framework import status
import pytest
from model_bakery import baker

from clinic.models import Package
from clinic.serializers import PackageSerializer

@pytest.fixture
def create_package(api_client):
    def do_create_package(package):
        return api_client.post('/clinic/packages/', package)
    return do_create_package

@pytest.mark.django_db
class TestCreatePackage:
    def test_if_user_is_anonymous_returns_401(self, create_package):
        response = create_package({'title': 'a', 'package_type': 'A', 'price': 20000})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_package):
        authenticate()

        response = create_package({'title': 'a', 'package_type': 'A', 'price': 20000})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate, create_package):
        authenticate(is_staff=True)

        response = create_package({'title': '', 'package_type': 'A', 'price': 20000})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_package):
        authenticate(is_staff=True)

        response = create_package({'title': 'a', 'package_type': 'A', 'price': 20000})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

@pytest.mark.django_db
class TestRetrievePackage:
    def test_if_collection_exists_returns_200(self, api_client):
        package = baker.make(Package)

        serializer = PackageSerializer(package)
    
        response = api_client.get(f'/clinic/packages/{package.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serializer.data