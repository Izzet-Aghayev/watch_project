from django.urls import path
# views import edilir
from accounts import views as accounts_views


# urls.py views.py fayillari elaqelendirilir
urlpatterns = [
    path('', accounts_views.account)
]
