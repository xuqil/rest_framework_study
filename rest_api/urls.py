from django.urls import path
from rest_api import views

app_name = 'rest_api'

urlpatterns = [
    path('list_users/', views.ListUsers.as_view()),

]

