from django.contrib import admin
from django.urls import path, include
from custom_caps import views

#все урлы касательно магазина, производителя, кепок. Урлы юзера в приложении users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/magazine/', views.MagazineListAPIview.as_view()),
    path('api/v1/magazine/<int:id>/', views.MagazineItemUpdateDeleteAPIview.as_view()),
    path('api/v1/manufacturer/', views.ManufacturerListAPIview.as_view()),
    path('api/v1/manufacturer/<int:id>/', views.ManufacturerItemUpdateDeleteAPIview.as_view()),
    path('api/v1/caps/', views.CapsListAPIview.as_view()),
    path('api/v1/caps/<int:id>/', views.CapsItemUpdateDeleteAPIview.as_view()),
    path('api/v1/category/', views.CategoryListAPIview.as_view()),
    path('api/v1/users/', include('user.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/discounts/', include('discounts.urls'))
]
