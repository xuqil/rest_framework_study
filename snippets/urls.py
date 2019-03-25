from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework import renderers

app_name = 'snippets'

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
])

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})
