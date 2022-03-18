
from django.urls import path
from Restauracja_app.views import CategoryView, Menu_AddView, \
    Menu_listView, Add_CategoryView, UpdateCategoryView, DeleteCategoryView, \
    UpdateMenuView, DeleteMenuView, Menu_Details

urlpatterns = [
    path('add_category/', Add_CategoryView.as_view(), name='add_category'),
    path('category/', CategoryView.as_view(), name='category'),
    path('update_category/<int:pk>/', UpdateCategoryView.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', DeleteCategoryView.as_view(), name='delete_category'),
    path('add_menu/', Menu_AddView.as_view(), name='add_menu'),
    path('menu_list/<slug>/', Menu_listView.as_view(), name='menu_list'),
    path('menu_details/<int:id>/', Menu_Details.as_view(), name='menu_details'),
    path('update_menu/<int:pk>/', UpdateMenuView.as_view(), name='update_menu'),
    path('delete_menu/<int:pk>/', DeleteMenuView.as_view(), name='delete_menu')


]