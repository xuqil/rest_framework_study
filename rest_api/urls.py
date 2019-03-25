from django.urls import path
from rest_api import views
from django.contrib.auth.models import User
from rest_api.serializers import UserSerializer

app_name = 'rest_api'

urlpatterns = [
    path('list_users/', views.ListUsers.as_view()),
    path('hello/', views.hello_world),
    path('users/', views.UserList.as_view(queryset=User.objects.all(),
                                          serializer_class=UserSerializer), name='user-list'),
    path('user_set/', views.UserViewSet.as_view({'get': 'list'})),
]

