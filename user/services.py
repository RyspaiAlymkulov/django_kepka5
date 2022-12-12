import dataclasses
import datetime
import jwt
from typing import TYPE_CHECKING
from django.conf import settings
from . import models
if TYPE_CHECKING:
    from .models import CustomUser


@dataclasses.dataclass
class CustomUserDataClass:
    first_name: str
    last_name: str
    email: str
    regions: str
    password: str = None
    id: int = None
    phone_number: int = None
    image: int = None

    @classmethod
    def from_instance(cls, user: "CustomUser") -> "CustomUserDataClass":
        return cls(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            id=user.id,
            phone_number=user.phone_number,
            regions=user.regions,
            image=user.image,
        )


def create_user(user_dc: "CustomUserDataClass") -> "CustomUserDataClass":
    instance = models.CustomUser(
        first_name=user_dc.first_name, last_name=user_dc.last_name,
        email=user_dc.email, phone_number=user_dc.phone_number,
        regions=user_dc.regions, image=user_dc.image



    )
    if user_dc.password is not None:
        instance.set_password(user_dc.password)

    instance.save()

    return CustomUserDataClass.from_instance(instance)


def user_email_selector(email: str) -> "CustomUser":
    user = models.CustomUser.objects.filter(email=email).first()

    return user


def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=36 ),
        iat=datetime.datetime.utcnow(),
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

    return token