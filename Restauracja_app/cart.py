from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from Restauracja_app.models import Menu, OrderItem, Order


def add_to_cart(request, pk):

    try:
        meal = get_object_or_404(Menu, pk=pk)
        order_item, created = OrderItem.objects.get_or_create(
            meal=meal,
            user=request.user,
            ordered=False
        )
        order = Order.objects.filter(user=request.user, ordered=False)

        if order.exists():
            order = order[0]

            if order.meals.filter(meal_id=meal.pk).exists():
                order_item.quantity += 1
                order_item.save()
                messages.success(request, "Dodano posiłek do koszyka")
                return redirect(reverse("category"))

            else:
                order.meals.add(order_item)
                messages.success(request, "Dodano posiłek do koszyka")
                return redirect(reverse("category"))
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, order_date=ordered_date)
            order.meals.add(order_item)
            messages.success(request, "Dodano posiłek do koszyka")
            return redirect(reverse("category"))
    except Exception:
        return redirect('login')


def remove_from_cart(request, pk):

    try:
        meal = get_object_or_404(Menu, pk=pk )
        order_item = OrderItem.objects.filter(
                    meal=meal,
                    user=request.user,
                    ordered=False
                )[0]
        if order_item.quantity > 1:
            order_item.quantity -= 1
            order_item.save()
        else:
            order_item.delete()
            messages.info(request, f"Posiłek {order_item.meal.name} został usunięty z koszyka")
        return redirect('order-details')
    except Exception:
        return redirect('login')