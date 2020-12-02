from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    
    # 판별기

    percentage = 36.36
    if percentage < 50:
        result = 0
    result = {'result':'0', 'percentage': percentage, 'time':'2020-11-14'}

    return JsonResponse(result)
