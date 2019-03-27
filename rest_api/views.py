from django.shortcuts import HttpResponse
from django.views import View
from rest_framework.views import APIView  # APIView视图继承View视图


class StudentsView(APIView):
    """
    APIView视图会根据请求识别meth方法，自动分配执行函数
    最先执行的是dispatch方法
    """
    def dispatch(self, request, *args, **kwargs):
        # 访问该class时必须先执行该函数，可以充当修饰器
        ret = super(StudentsView, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        return HttpResponse("GET")

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('DELETE')


