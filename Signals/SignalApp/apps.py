from django.apps import AppConfig


class SignalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SignalApp'

    def ready(self):
        import SignalApp.signals