from django.db import models


# Create your models here.

class ServerManager(models.Model):
    title = models.TextField(max_length=40)
    version = models.TextField(max_length=10)
    map_zip_file = models.FileField(upload_to="uploads/map/origins", blank=True)

    def __str__(self):
        return self.title
