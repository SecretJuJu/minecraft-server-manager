from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request=request, template_name='server_manager/list.html')


def create(request):
    if request.method == 'GET':
        return render(request=request, template_name='server_manager/create.html')

    if request.method == 'POST':
        return HttpResponse('you are welcome')

    return HttpResponse.status_code(404)

