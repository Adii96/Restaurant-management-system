import datetime
import pytest
from django.test import Client
from django.urls import reverse
from Restauracja_app.forms import Add_CategoryModelForm, Add_MenuModelForm
from Restauracja_app.models import Category, Menu, Reserve, Table


@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


# Test to Category View

@pytest.mark.django_db
def test_category_view():
    client = Client()
    url = reverse('category')
    response = client.get(url)
    assert  response.status_code == 200


@pytest.mark.django_db
def test_add_category_get():
    client = Client()
    url = reverse('add_category')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], Add_CategoryModelForm)

@pytest.mark.django_db
def test_add_category_post():
    client = Client()
    url = reverse('add_category')
    date = {
        'name': 'Desery',
        'description': 'Opis',
        'slug': 'desery',

    }
    response = client.post(url, date)
    assert response.status_code == 302
    new_url = reverse('category')
    assert response.url.startswith(new_url)
    Category.objects.get(**date)

@pytest.mark.django_db
def test_update_category_view(category):
    category = category[0]
    client = Client()
    url = reverse('update_category', args=(category.id,))
    data = {
        'name': 'Desery',
        'description': 'Opis',
        'slug': 'desery'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    new_url = reverse('category')
    assert response.url.startswith(new_url)
    Category.objects.get(name='Desery')

@pytest.mark.django_db
def test_delete_Category_view(category):
    category = category[0]
    client = Client()
    url = reverse('delete_category', args=(category.id,))
    response = client.get(url)
    assert response.status_code == 200



# Test to Menu View

@pytest.mark.django_db
def test_Menu_view(category):
    category = category[0]
    client = Client()
    url = reverse('menu_list', args=(category.slug,))
    response = client.get(url)
    assert  response.status_code == 200


@pytest.mark.django_db
def test_add_Menu_get():
    client = Client()
    url = reverse('add_menu')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], Add_MenuModelForm)

@pytest.mark.django_db
def test_add_Menu_post(category):
    category = category[0]
    client = Client()
    url = reverse('add_menu')
    date = {
        'name': 'Zupa ogórkowa',
        'ingredients': 'Składniki',
        'description': 'Opis',
        'price': 10,
        'votes': 0,
        'category': category.id


    }
    response = client.post(url, date)
    assert response.status_code == 302
    new_url = reverse('menu_list', args=(category.slug,))
    assert response.url.startswith(new_url)
    Menu.objects.get(**date)


@pytest.mark.django_db
def test_Menu_Details_get(menu):
    menu = menu[0]
    client = Client()
    url = reverse('menu_details', args=(menu.id,))
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_Menu_Details_post(comment, menu):
    menu = menu[0]
    client = Client()
    url = reverse('menu_details', args=(menu.id,))
    date = {
        'title': 't',
        'meal': menu.id,
        'text': 't',
        'author': 't'
    }
    response = client.post(url, date)
    assert response.status_code == 200



@pytest.mark.django_db
def test_update_Menu_view(category, menu):
    category = category[0]
    menu = menu[0]
    client = Client()
    url = reverse('update_menu', args=(menu.id,))
    data = {
        'name': 'Zupa ogórkowa',
        'ingredients': 'Składniki',
        'description': 'Opis',
        'price': 10,
        'votes': 0,
        'category': category.id
    }
    response = client.post(url, data)
    assert response.status_code == 302
    new_url = reverse('menu_list', args=(category.slug,))
    assert response.url.startswith(new_url)
    Menu.objects.get(name='Zupa ogórkowa')


@pytest.mark.django_db
def test_delete_Menu_view(menu):
    menu = menu[0]
    client = Client()
    url = reverse('delete_menu', args=(menu.id,))
    response = client.get(url)
    assert response.status_code == 200


# Test to Order_Details_View


@pytest.mark.django_db
def test_Order_Details_View_not_login():
    client = Client()
    url = reverse('order-details')
    response = client.get(url)
    assert response.status_code == 302
    url = reverse('login')
    assert response.url.startswith(url)


@pytest.mark.django_db
def test_Order_Details_View_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('order-details')
    response = client.get(url)
    assert response.status_code == 302


# Test to About_View

@pytest.mark.django_db
def test_about_View():
    client = Client()
    url = reverse('about')
    response = client.get(url)
    assert response.status_code == 200

# Test to Reserve and Table

@pytest.mark.django_db
def test_Table_View():
    client = Client()
    url = reverse('table_list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_Reserve_get(table):
    table = table[0]
    client = Client()
    url = reverse('reserve', args=(table.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_Reserve_post(table):
    table = table[0]
    client = Client()
    url = reverse('reserve', args=(table.id,))
    date = {
        'date': datetime.date.today(),
        'time': datetime.time(),
        'last_name': 'name',
        'tables': table.id
    }
    response = client.post(url, date)
    assert response.status_code == 302
    new_url = reverse('table_list')
    assert response.url.startswith(new_url)
    Reserve.objects.get(**date)

@pytest.mark.django_db
def test_Reserve_list_View():
    client = Client()
    url = reverse('reserve_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_Table_view(table):
    table = table[0]
    client = Client()
    url = reverse('update_table', args=(table.id,))
    data = {
        'name': 'Table',
        'number_of_seats': 1,
        'availability': True
    }
    response = client.post(url, data)
    assert response.status_code == 302
    new_url = reverse('table_list')
    assert response.url.startswith(new_url)
    Table.objects.get(name='Table')

@pytest.mark.django_db
def test_delete_Table_view(table):
    table = table[0]
    client = Client()
    url = reverse('delete_table', args=(table.id,))
    response = client.get(url)
    assert response.status_code == 200

# Test to Contact

@pytest.mark.django_db
def test_contact_get():
    client = Client()
    url = reverse('contact')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_contact_post():
    client = Client()
    url = reverse('contact')
    date = {
        'first_name': 'Adrian',
        'last_name': 'Kujawa',
        'email_address': 'Adrian@wp.pl',
        'message': 'Wiadomość'
    }
    response = client.post(url, date)
    assert response.status_code == 302
    new_url = reverse('index')
    assert response.url.startswith(new_url)