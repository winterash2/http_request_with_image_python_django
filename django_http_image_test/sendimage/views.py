from django.shortcuts import render
from django.http import HttpResponse

from django.core.files.storage import default_storage


def get_image(request):
    print(request)
    print(request.POST)
    print(request.FILES)

    for files in request.FILES:
        file_obj = request.FILES[files]
        filename = str(file_obj)
        # file_obj = request.data['file']
        # print(files)
        print(filename)
        with default_storage.open(filename, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
    
    return HttpResponse("success")
