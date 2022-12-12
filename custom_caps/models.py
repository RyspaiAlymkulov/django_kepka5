from user.models import CustomUser
from django.db import models



class Magazine(models.Model):
    title = models.TextField(default='default')
    name = models.CharField(max_length=60)
    description = models.TextField(default='default')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class Category(models.Model):
    title = models.CharField(max_length=255, null=False)
    category_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'ID {self.id}: {self.title}'


#Модель производителя, определил имя производителя уникальныым
class Manufacturer(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


#Модель кепок-товара, определил стоимость, написал прайс,
# имя кепок может быть уникальным? определил в каком магазине будет, определил производителя
class Caps(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'DOLLAR'),
        ('KGS', 'SOM'),
        ('TENGE', 'TENGE'),
    )
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    magazine = models.ForeignKey(Magazine,
                                 related_name='Shops',
                                 on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer,
                                     related_name='Shops',
                                     on_delete=models.CASCADE,
                                     )
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES,
                                default='kgz')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class UserCapsRelation(models.Model):
    RATING_CHOICES = (
        (1,  'Нормально'),
        (2, 'Хорошо'),
        (3, 'Отлично'),
        (4, 'Прекрасно'),
        (5, 'Изумительно')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    caps = models.ForeignKey(Caps, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    favorites = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES, null=True)

    def __str__(self):
        return f'ID {self.id}: {self.user}: {self.caps.name}'

