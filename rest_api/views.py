from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import View
from rest_framework.views import APIView


class StudentsView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("GET")

    def post(self, request, *args, **kwargs):
        return HttpResponse('ok')

    def put(self, request):
        return HttpResponse('ok')


