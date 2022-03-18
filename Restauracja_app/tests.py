from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from Restauracja_app.forms import Add_CategoryModelForm

@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_category_get():
    client = Client()
    url = reverse('add_category')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], Add_CategoryModelForm)