from django.shortcuts import HttpResponse
from rest_framework.views import APIView  # APIView视图继承View视图
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions


class MyAuthentication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed("用户认证失败")
        return ('alex', None)
    def authenticate_header(self, args):
        pass


class StudentsView(APIView):
    """
    APIView视图会根据请求识别meth方法，自动分配执行函数
    最先执行的是dispatch方法
    """
    authentication_classes = [MyAuthentication, ]  # 自定义配置文件

    def get(self, request, *args, **kwargs):
        self.dispatch
        print(request)  # 该request不是原request
        ret = {
            'code': 1000,  # code可以任意设置
            'msg': 'xxx'
        }
        return HttpResponse("GET")

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('DELETE')


