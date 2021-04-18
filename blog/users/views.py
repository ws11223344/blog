from django.shortcuts import render

# Create your views here.
# 注册视图
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request,'register.html')



from django.http.response import HttpResponseBadRequest, HttpResponse
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection



def content_type(args):
    pass


class ImageCodeView(View):
    def get(self,request):
        uuid=request.GET.get('uuid')
        if uuid is None:
            return HttpResponse('没有传递uuid')
        text,image=captcha.generate_captcha()
        redis_conn = get_redis_connection('default')
        redis_conn.setex('img:%s'%uuid,300,text)
        return HttpResponse(image,content_type=='image/jpeg')


