from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from custom_caps.models import Magazine, Manufacturer, Caps, UserCapsRelation, Category
from custom_caps.serializers import MagazineSerializer, ManufacturerSerializer, CapsSerializer, \
    UserCapsRelationSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet


#вьюшка Магазина
class MagazineListAPIview(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    pagination_class = PageNumberPagination
    name = 'magazine-list'


class MagazineItemUpdateDeleteAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    name = 'magazine-detail'
    lookup_field = 'id'


class ManufacturerListAPIview(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    pagination_class = PageNumberPagination
    name = 'manufacturer-list'


class ManufacturerItemUpdateDeleteAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    name = 'manufacturer-detail'
    lookup_field = 'id'


class CapsListAPIview(generics.ListCreateAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer
    pagination_class = PageNumberPagination
    name = 'caps-list'


class CapsItemUpdateDeleteAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer
    name = 'caps-detail'
    lookup_field = 'id'


class UserCapsRelationAPIview(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserCapsRelation.objects.all()
    serializer_class = UserCapsRelationSerializer
    lookup_field = 'Caps'

    def get_object(self):
        obj, _ = UserCapsRelation.objects.get_or_create(user=self.request.user,
                                                        book_id=self.kwargs['Caps'])
        return obj


class CategoryListAPIview(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

