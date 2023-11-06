from django.db import models
from django.contrib.auth.models import User




class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    author = models.CharField(max_length=20, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
