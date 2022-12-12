from rest_framework import views, response, exceptions, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import serializers as user_serializer
from . import services, authentication
from .models import CustomUser
from .serializers import ProfileSerializer


class RegisterApi(views.APIView):
    def post(self, request):
        serializer = user_serializer.CustomUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)
        return response.Response(data=serializer.data)


class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = services.user_email_selector(email=email)
        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        token = services.create_token(user_id=user.id)
        resp = response.Response()
        resp.set_cookie(key="jwt", value=token, httponly=True)
        return resp


class UserApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = user_serializer.CustomUserSerializers(user)
        return response.Response(serializer.data)


class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "Пользователь вышел из приложения"}
        return resp


class ProfileCreateListAPIview(views.APIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = user_serializer.CustomUserSerializers(data=request.data)
        serializer.user = request.user
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        return Response(ProfileSerializer(profile))