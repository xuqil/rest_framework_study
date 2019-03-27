from django.shortcuts import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.views import APIView  # APIView视图继承View视图
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions


@method_decorator(csrf_exempt, name='dispatch')
class StudentsView(View):
    """
    APIView视图会根据请求识别meth方法，自动分配执行函数
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


