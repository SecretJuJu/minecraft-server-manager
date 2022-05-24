from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from minecraft_server_manager.apps.server_manager.forms import MapUploadForm
from minecraft_server_manager.apps.server_manager.models import ServerManager


@login_required
def index(request):
    servers = ServerManager.objects.all()

    context = {
        'servers': servers,
    }

    return render(request=request, template_name='server_manager/list.html', context=context)


@login_required
def create(request):
    if request.method == 'GET':
        map_upload_form = MapUploadForm
        context = {
            'map_upload_form': map_upload_form,
        }

        return render(request, 'server_manager/create.html', context)

    if request.method == 'POST':
        title = request.POST['title']
        version = request.POST['version']
        map_zip_file = request.FILES["map_zip_file"]
        server_manager = ServerManager(
            title=title,
            version=version,
            map_zip_file=map_zip_file
        )
        server_manager.save()
        return redirect('/server_manager')

    return HttpResponse.status_code(404)
