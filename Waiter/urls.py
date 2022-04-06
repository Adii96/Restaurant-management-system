from django.urls import path
from Waiter.views import Index_Waiter, Menu_View
from Waiter.cart_waiter import add_to_cart_waiter, remove_from_cart_waiter
urlpatterns = [
    path('waiter_index/', Index_Waiter.as_view(), name='index_waiter'),
    path('waiter_menu/<slug>/', Menu_View.as_view(), name='waiter_menu'),
    path('add_to_card_waiter/<pk>/', add_to_cart_waiter, name='add_to_card_waiter'),
    path('remove-from-cart/<pk>/', remove_from_cart_waiter, name='remove_from_cart_waiter'),
]