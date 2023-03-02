from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator
from django.db import models
from sorl.thumbnail import ImageField


class RoadMap(models.Model):
    name = models.CharField(
        verbose_name='имя дорожной карты',
        max_length=150,
    )
    description = RichTextField(
        verbose_name='описание',
        blank=True,
        null=True,
    )
    courses = models.ManyToManyField(
        'course.Course',
        verbose_name='курсы',
        related_name='road_maps',
        through='course.OrderRoadMapCourse'
    )
    image = ImageField(
        verbose_name='фото',
        blank=True,
        null=True,
        upload_to='road_map',
        help_text='Добавьте фото',
    )

    class Meta:
        verbose_name = 'дорожная карта'
        verbose_name_plural = 'дорожные карты'

    def __str__(self):
        return self.name


class OrderRoadMapCourse(models.Model):
    course = models.ForeignKey(
        'course.Course',
        verbose_name='курс',
        on_delete=models.CASCADE,
        related_name='order_road_map',
    )
    road_map = models.ForeignKey(
        'course.RoadMap',
        verbose_name='дорожная карта',
        on_delete=models.CASCADE,
        related_name='order_course',
    )
    order_num = models.PositiveIntegerField(
        verbose_name='порядковый номер',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        unique_together = ['course_id', 'road_map_id', 'order_num']

    def __str__(self):
        return self.course.__str__()
