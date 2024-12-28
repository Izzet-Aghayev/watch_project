from django.urls import path, include



urlpatterns = [
    path('watches/', include('watches.api.urls')),  # 127.0.0.1:8000/api/v1/watches/
    path('accounts/', include('accounts.api.urls')),  # 127.0.0.1:8000/api/v1/accounts/
]