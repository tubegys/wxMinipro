from django.http import HttpResponse, JsonResponse, FileResponse
from thirdparty import juhe
import json


def helloworld(request):
    print("request method: ", request.method)
    print("request meta:", request.META)
    print("request cookies: ", request.COOKIES)
    print('request QueryDict: ', request.GET)
    # return HttpResponse(content='OK', status=201)
    m = {
        "message": "hello json response"
    }
    return JsonResponse(data=m, status=200, safe=False)  # safe 为 false 不检查是否为json，任何类型都会转换为json
    pass


def weather(request):
    if request.method == "GET":
        city = request.GET.get('city')
        data = juhe.weather(city)
        return JsonResponse(data=data, status=200)
    elif request.method == "POST":
        received_body = request.body
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        response_data = []
        for city in cities:
            result = juhe.weather(city)
            result['city'] = city
            response_data.append(result)
        return JsonResponse(data=response_data, status=200, safe=False)
