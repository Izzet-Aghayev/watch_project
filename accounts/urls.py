from django.urls import path
# views import edilir
from accounts import views as accounts_views


# urls.py views.py fayillari elaqelendirilir
urlpatterns = [
    path('login/', accounts_views.sign_in, name='login'),
    path('logout/', accounts_views.sign_out, name='logout'),
    path('register/', accounts_views.register, name='register'),
    path('profile/', accounts_views.profile, name='profile'),
    path('delete_seller/', accounts_views.delete_seller, name='delete_seller'),
]
