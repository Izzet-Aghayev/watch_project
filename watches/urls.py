from django.urls import path
# views import edilir
from watches import views as watches_views


# urls.py views.py fayillari elaqelendirilir
urlpatterns = [
    path('', watches_views.all_watches, name='all_watch'),    # 127.0.0.1:8000/watches/
    path('create', watches_views.create_watch, name='watch_create'),    # 127.0.0.1:8000/create/
    path('my_watch', watches_views.my_watches, name='my_watch'),    # 127.0.0.1:8000/my_watches/
    path('detail/<int:pk>/', watches_views.detail_watch, name='watch_detail'),    # 127.0.0.1:8000/detail/<int:pk>/
    path('update/<int:pk>/', watches_views.update_watch, name='watch_update'),    # 127.0.0.1:8000/update/<int:pk>/
    path('delete/<int:pk>/', watches_views.delete_watch, name='watch_delete'),    # 127.0.0.1:8000/delete/<int:pk>/
]
