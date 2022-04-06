
from django.urls import path
from Restauracja_app.views import CategoryView, Menu_AddView, \
    Menu_listView, Add_CategoryView, UpdateCategoryView, DeleteCategoryView, \
    UpdateMenuView, DeleteMenuView, Menu_Details, TableListView, ReserveView, \
    ReserveList, UpdateTableView, DeleteTableView, AboutView, Order_Details_View, ReserveDelete, Contact_View
from Restauracja_app.cart import add_to_cart, remove_from_cart

urlpatterns = [
    path('add_category/', Add_CategoryView.as_view(), name='add_category'),
    path('category/', CategoryView.as_view(), name='category'),
    path('update_category/<int:pk>/', UpdateCategoryView.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', DeleteCategoryView.as_view(), name='delete_category'),
    path('add_menu/', Menu_AddView.as_view(), name='add_menu'),
    path('menu_list/<slug>/', Menu_listView.as_view(), name='menu_list'),
    path('menu_details/<int:id>/', Menu_Details.as_view(), name='menu_details'),
    path('update_menu/<int:pk>/', UpdateMenuView.as_view(), name='update_menu'),
    path('delete_menu/<int:pk>/', DeleteMenuView.as_view(), name='delete_menu'),
    path('table_list/', TableListView.as_view(), name='table_list'),
    path('reserve/<int:id>/', ReserveView.as_view(), name='reserve'),
    path('reserve_list/', ReserveList.as_view(), name='reserve_list'),
    path('delete_reserve/<int:pk>/', ReserveDelete.as_view(), name='delete_reserve'),
    path('update_table/<int:pk>/', UpdateTableView.as_view(), name='update_table'),
    path('delete_table/<int:pk>/', DeleteTableView.as_view(), name='delete_table'),
    path('about/', AboutView.as_view(), name='about'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('order-details/', Order_Details_View.as_view(), name='order-details'),
    path("contact", Contact_View.as_view(), name="contact"),


]