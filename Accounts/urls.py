from django.urls import path
from Accounts.views import RegistrationView, LoginView, LogOutView


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout')

]