from django.forms import ModelForm
from .models import ServerManager


class MapUploadForm(ModelForm):
    class Meta:
        model = ServerManager
        fields = ['title', 'version', 'map_zip_file']
