import pytest
from faker import Faker

from django_dynamic_fixture import G
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

from app.models import Ad, UserAd

faker = Faker()


@pytest.fixture(scope='function')
def setup_data():
    user = G(User)
    ad1 = G(Ad)
    ad2 = G(Ad)
    G(UserAd, user=user, ad=ad1, ad_type=UserAd.MANUAL_SAVE)
    G(UserAd, user=user, ad=ad2, ad_type=UserAd.AUTO_SAVE)
    return {'user': user, 'ad1': ad1, 'ad2': ad2}


@pytest.mark.django_db
@pytest.mark.urls('project.urls')
def test_get_list_ads_by_type(rest_client, setup_data):
    user = setup_data['user']
    rest_client.force_authenticate(user=user)
    response = rest_client.get(reverse('ads-management-detail', kwargs={'pk': 'current'}))
    assert response.status_code == status.HTTP_200_OK

    data = response.json()['list_ads']
    assert response.json()
    assert len(data['auto_ads']) == user.userad_set.filter(ad_type=UserAd.AUTO_SAVE).count()
    assert len(data['manual_ads']) == user.userad_set.filter(ad_type=UserAd.MANUAL_SAVE).count()


@pytest.mark.django_db
@pytest.mark.urls('project.urls')
def test_save_add(rest_client, setup_data):
    ad3 = G(Ad)
    ad4 = G(Ad)
    user = setup_data['user']
    rest_client.force_authenticate(user=user)

    response = rest_client.post(reverse('ads-management-list'), {'ad_type': 'auto', 'ad_id': ''})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'No ad found with provided id!' in str(response.content)

    response = rest_client.post(reverse('ads-management-list'), {'ad_type': 'auto', 'ad_id': ad3.id})
    assert response.status_code == status.HTTP_201_CREATED

    response = rest_client.post(reverse('ads-management-list'), {'ad_type': 'manual', 'ad_id': ad4.id})
    assert response.status_code == status.HTTP_201_CREATED

    response = rest_client.get(reverse('ads-management-detail', kwargs={'pk': 'current'}))
    assert response.status_code == status.HTTP_200_OK

    data = response.json()['list_ads']
    assert response.json()

    assert len(data['auto_ads']) == 2
    assert len(data['manual_ads']) == 2


@pytest.mark.django_db
@pytest.mark.urls('project.urls')
def test_destroy(rest_client, setup_data):
    user = setup_data['user']
    ad2=setup_data['ad2']
    rest_client.force_authenticate(user=user)

    response = rest_client.delete(reverse('ads-management-detail', kwargs={'pk': '676'}))
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'No ad found with provided id!' in str(response.content)

    response = rest_client.delete(reverse('ads-management-detail', kwargs={'pk':ad2.id}))
    assert response.status_code == status.HTTP_200_OK

    response = rest_client.get(reverse('ads-management-detail', kwargs={'pk': 'current'}))
    assert response.status_code == status.HTTP_200_OK

    data = response.json()['list_ads']
    assert response.json()

    assert len(data['auto_ads']) == 0
    assert len(data['manual_ads']) == 1



