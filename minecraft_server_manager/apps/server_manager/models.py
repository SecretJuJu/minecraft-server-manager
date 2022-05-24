from django.db import models


# Create your models here.

class ServerManager(models.Model):
    title = models.CharField(max_length=40)
    version = models.CharField(max_length=10)
    map_zip_file = models.FileField(upload_to="uploads/map/origins", blank=True)
    is_server_running = models.BooleanField(default=False)

    def __str__(self):
        return self.title
