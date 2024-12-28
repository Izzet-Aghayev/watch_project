from django.urls import path

from . import views as accounts_views



urlpatterns = [
    # path('login/', accounts_views.sign_in, name='login'),   # 127.0.0.1:8000/api/v1/accounts/login
    path('login/', accounts_views.LoginView.as_view(), name='login'),   # 127.0.0.1:8000/api/v1/accounts/login

    # path('logout/', accounts_views.sign_out, name='logout'),    # 127.0.0.1:8000/api/v1/accounts/logout
    path('logout/', accounts_views.LogoutView.as_view(), name='logout'),   # 127.0.0.1:8000/api/v1/accounts/logout


    # path('register/', accounts_views.register, name='register'),    # 127.0.0.1:8000/api/v1/accounts/register
    path('register/', accounts_views.RegisterView.as_view(), name='register'),    # 127.0.0.1:8000/api/v1/accounts/register
]
