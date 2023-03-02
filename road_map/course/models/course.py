from django.db import models
from sorl.thumbnail import ImageField


class Course(models.Model):
    name = models.CharField(
        verbose_name='имя курса',
        max_length=150,
    )
    image = ImageField(
        verbose_name='фото',
        blank=False,
        upload_to='course',
        help_text='Добавьте фото',
    )
    description = models.TextField(
        verbose_name='описание'
    )

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.name
