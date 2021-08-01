from django.db import models


class UserProfile(models.Model):
    user_id = models.PositiveIntegerField(
        verbose_name='ID пользователя'
    )
    name = models.TextField(
        verbose_name='Имя пользователя'
    )
    surname = models.TextField(
        verbose_name='Фамилия пользователя'
    )
    first_start = models.DateTimeField(
        auto_now_add=True,
        verbose_name = 'Дата создания аккаунта'

    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'