from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterApi.as_view()),
    path('login/', views.LoginApi.as_view()),
    path('user/', views.UserApi.as_view()),
    path("logout/", views.LogoutApi.as_view()),
    path('userprofile/', views.ProfileCreateListAPIview.as_view())

]