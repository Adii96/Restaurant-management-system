import pytest
from django.contrib.auth.models import User
from Restauracja_app.models import Category, Menu, Table, Comments

@pytest.fixture
def user():
    return User.objects.create_user(username='name', password='password')

@pytest.fixture
def category():
    list = []
    for i in range(10):
        x = Category.objects.create(
            name= i,
            description= i,
            slug= i
        )
        list.append(x)
    return list

@pytest.fixture
def menu(category):
    list = []
    for i in range(10):
        x = Menu.objects.create(
            name= i,
            ingredients= i,
            description= i,
            price= i,
            votes= i,
            category= category[0]
        )
        list.append(x)
    return list

@pytest.fixture
def table():
    list = []
    for i in range(10):
        x = Table.objects.create(
            name= i,
            number_of_seats= i,
            availability= True
        )
        list.append(x)
    return list

@pytest.fixture
def comment(menu):
    list = []
    for i in range(10):
        x = Comments.objects.create(
            title= i,
            meal= menu[0],
            text= i,
            author= i
        )
        list.append(x)
    return list