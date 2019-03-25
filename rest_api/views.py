from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


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
