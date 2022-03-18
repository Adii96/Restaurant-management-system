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
    image = models.ImageField(blank=True, upload_to='menu_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = 'Menu'

    def get_update_menu(self):
        return reverse('update_menu', args=(self.pk,))

    def get_delete_menu(self):
        return reverse('delete_menu', args=(self.pk,))


class Comments(models.Model):
    title = models.CharField(max_length=120)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    data_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'
