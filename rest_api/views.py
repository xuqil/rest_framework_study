from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class ListUsers(APIView):
    """
    展示系统中所有的用户
    * 需要令牌认证。
    * 只有admin用户能够访问这一个视图
    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        返回一个用户列表
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


@api_view(['GET', 'POST'])
def hello_world(request):
    """
    这个视图将使用默认渲染器、解析器、身份验证设置中指定的类等。通常默认只有GET方法，其他请求方法会报405错误，
    我们可以手动添加方法为这装饰器指定request方法
    :param request:
    :return:
    """
    if request.method == 'POST':
        return Response({"message": "Got some data", "data": request.data})
    return Response({"message": "hello world"})


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
