from django.urls import path
from . import views as watches_views


# urls.py views.py fayillari elaqelendirilir
urlpatterns = [
    path('', watches_views.all_watches, name='all_watch'),    # 127.0.0.1:8000/watches/
    path('create/', watches_views.create_watch, name='watch_create'),    # 127.0.0.1:8000/watches/watch_create/
    path('detail/<int:pk>', watches_views.detail_watch, name='watch_detail'),    # 127.0.0.1:8000/watches/watch_detail/
    path('update/<int:pk>', watches_views.update_watch, name='watch_update'),    # 127.0.0.1:8000/watches/watch_update/
    path('delete/<int:pk>', watches_views.delete_watch, name='watch_delete'),    # 127.0.0.1:8000/watches/watch_delete/
]