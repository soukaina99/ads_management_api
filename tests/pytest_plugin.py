import pytest
from faker import Faker


@pytest.fixture()
def faker():
    return Faker()



@pytest.fixture()
def rest_client():
    from rest_framework.test import APIClient
    return APIClient()


