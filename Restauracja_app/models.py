from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    slug = models.CharField(max_length=64, unique=True)
    image = models.ImageField(blank=True, upload_to='category_images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = 'Kategorie'

    def get_absolute_url(self):
        return reverse('update_category', args=(self.pk,))

    def get_delete_url(self):
        return reverse('delete_category', args=(self.pk,))

class Menu(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    votes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='menu_images')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = 'Menu'

    def get_update_menu(self):
        return reverse('update_menu', args=(self.pk,))

    def get_delete_menu(self):
        return reverse('delete_menu', args=(self.pk,))

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            "pk": self.pk
        })

    def get_add_to_cart_waiter_url(self):
        return reverse("add_to_card_waiter", kwargs={
            "pk": self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            "pk": self.pk
        })

    def get_remove_from_cart_waiter_url(self):
        return reverse("remove_from_cart_waiter", kwargs={
            "pk": self.pk
        })


class Comments(models.Model):
    title = models.CharField(max_length=120)
    meal = models.ForeignKey(Menu, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=64)
    data_create = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'


class Table(models.Model):
    name = models.CharField(max_length=64)
    number_of_seats = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_update_table(self):
        return reverse('update_table', args=(self.pk,))

    def get_delete_table(self):
        return reverse('delete_table', args=(self.pk,))


class Reserve(models.Model):
    date = models.DateField()
    time = models.TimeField()
    last_name = models.CharField(max_length=64)
    tables = models.ForeignKey(Table, on_delete=models.CASCADE)

    def get_delete_reserve(self):
        return reverse('delete_reserve', args=(self.pk,))


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=True)
    meal = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.meal.name}"

    def get_total_item_price(self):
        return self.quantity * self.meal.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meals = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.meals.all():
            total += order_item.get_total_item_price()
        return total
