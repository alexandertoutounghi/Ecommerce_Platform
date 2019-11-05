from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'User Manage'

    def ready(self):
        import users.signals

