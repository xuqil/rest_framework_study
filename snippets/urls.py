from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

app_name = 'snippets'
# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet, base_name='user')

# API URL 现在由路由器自动确定。
urlpatterns = [
    path('', include(router.urls)),
]