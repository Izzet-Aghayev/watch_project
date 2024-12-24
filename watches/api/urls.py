from django.urls import path
from . import views as watches_views


# urls.py views.py fayillari elaqelendirilir
urlpatterns = [
    path('', watches_views.all_watches, name='all_watch'),    # 127.0.0.1:8000/watches/
]