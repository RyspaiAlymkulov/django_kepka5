from rest_framework import serializers
from . import services
from .models import CustomUser


class CustomUserSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    phone_number = serializers.CharField()
    regions = serializers.CharField()
    image = serializers.ImageField()

    class Meta:
        model = CustomUser
        fields = [
            'id', 'last_name', 'first_name', 'email', 'password', 'phone_number', 'regions', 'image'
        ]

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.CustomUserDataClass(**data)


#Сериализатор профиля юзера
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = [
            'user', 'id', 'last_name', 'first_name', 'email', 'password', 'phone_number', 'regions', 'image'
        ]

        def create(self, validated_data):
            profile = CustomUser.objects.create(user=self.context['request'].user, **validated_data)
            return profile