from rest_framework import generics
from .models import MagazineCoupon, MagazineDiscount
from .serializers import MagazineDiscountSerializer, MagazineCouponSerializer


class MagazineDiscountListAPIview(generics.ListCreateAPIView):
    queryset = MagazineDiscount.objects.all().order_by('id')
    serializer_class = MagazineDiscountSerializer


class MagazineCouponListAPIview(generics.ListCreateAPIView):
    queryset = MagazineCoupon.objects.all().order_by('id')
    serializer_class = MagazineCouponSerializer