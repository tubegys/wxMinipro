import os
from django.http import JsonResponse, HttpResponse, FileResponse, Http404
from django.views import View
from djangostart import settings
import utils
import hashlib


def image(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGE_DIR, md5 + '.jpg')
        print(imgfile)
        if not os.path.exists(imgfile):
            return Http404()
        else:
            data = open(imgfile, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpeg')


def image_text(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGE_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return utils.response.wrap_json_response(code=utils.response.ReturnCode.FAILED)
        else:
            response_data = {'name': md5 + '.jpg', 'url': '/service/image?md5={}'.format(md5)}
            response = utils.response.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe=False)


class ImageView(View, utils.response.CommonResponseMixin):
    def get(self, request):
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGE_DIR, md5 + '.jpg')
        print(imgfile)
        if not os.path.exists(imgfile):
            return Http404()
        else:
            # data = open(imgfile, 'rb').read()
            # return HttpResponse(content=data, content_type='image/jpg')
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpeg')

    def post(self, request):  # 图片上传，并保存到本地
        print("enter POST")
        files = request.FILES
        print(files)
        response = []
        for key, value in files.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(settings.IMAGE_DIR, md5 + '.jpg')
            print(path)
            with open(path, 'wb') as f:
                f.write(content)
            response.append({'name': key, 'md5': md5})
        message = 'POST method success'
        res = self.wrap_json_response(data=response, code=utils.response.ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=res, safe=False)
        pass

    def put(self, request):
        message = "PUT Method success"
        # response = utils.response.wrap_json_response(message=message)
        response = self.wrap_json_response(message=message)
        return JsonResponse(data=response, safe=False)
        pass

    def delete(self, request):  # 文件删除
        md5 = request.GET.get('md5')
        img_name = md5 + '.jpg'
        path = os.path.join(settings.IMAGE_DIR, img_name)
        if os.path.exists():
            os.remove(path)
            message = "remove file: {} success".format(img_name)
        else:
            message = 'File: {} not found'.format(img_name)

        response = self.wrap_json_response(code=utils.response.ReturnCode.SUCCESS, message=message)
        return JsonResponse(data=response, safe=False)
        pass
