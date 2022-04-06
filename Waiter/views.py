from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from Restauracja_app.models import Menu, Category, Order


class Index_Waiter(View):
    def get(self, request):
        category = Category.objects.all()

        return render(request, 'waiter_order.html', {'category': category})

class Menu_View(View):
    def get(self, request, slug):
        menu = Menu.objects.filter(category__slug=slug)
        category = Category.objects.all()
        order = Order.objects.get(user=request.user, ordered=False)
        return render(request, 'weiter_menu.html', {'category': category, 'menu': menu, 'order': order})

