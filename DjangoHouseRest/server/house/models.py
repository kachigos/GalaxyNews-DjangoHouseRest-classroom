from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class House(models.Model):
    reg_number = models.CharField(
        'Регистрационный номер',
        db_index=True,
        unique=True,
        max_length=10
    )
    aria = models.CharField(
        'Площадь',
        max_length=5
    )
    types_house = (
        (1,'Монсард'),
        (2, 'Частный'),
        (3, 'Балконские'),
        (4, 'Элитки'),
    )
    types = models.CharField(
        'Тип дома',
        choices=types_house,
        max_length=50
    )
    builder = models.CharField(
        'Подрядчик',
        max_length=60
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.PROTECT
    )