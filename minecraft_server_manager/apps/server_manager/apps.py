from django.apps import AppConfig

from minecraft_server_manager.commons.utils.generate_app_name import generate_app_name


class ServerManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = generate_app_name('server_manager')
