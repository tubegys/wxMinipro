import os
from djangostart import settings
import yaml
from utils import response
from django.http import JsonResponse


def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps


def get_menu(request):
    global_app_data = init_app_data()
    publish_app_data = global_app_data.get('published')
    res = response.wrap_json_response(data=publish_app_data, code=response.ReturnCode.SUCCESS)
    return JsonResponse(data=res, safe=False)


if __name__ == "__main__":
    apps = init_app_data()
    print(apps)
