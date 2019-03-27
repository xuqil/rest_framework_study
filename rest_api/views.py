from django.shortcuts import HttpResponse
from django.views import View


class StudentsView(View):
    """
    View视图会根据请求识别meth方法，自动分配执行函数
    最先执行的是dispatch方法
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse("GET")

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('DELETE')


