from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class News(models.Model):
    title = models.CharField(
        'Описание',
        db_index=True,
        unique=True,
        max_length=200
    )
    description = models.TextField(
        'Содержание',
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )
    image = models.ImageField(
        'Изоброжение',
        upload_to='image/',
        blank=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'