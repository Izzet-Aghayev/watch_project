from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # signals faylını bu method daxilində import edirik 
    def ready(self):
        from accounts import signals


