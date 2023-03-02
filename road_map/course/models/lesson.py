from django.core.validators import MinValueValidator
from django.db import models


class Lesson(models.Model):
    name = models.CharField(
        verbose_name='Имя урока',
        max_length=255,
    )
    video_url = models.URLField(
        verbose_name='ссылка на видео',
        max_length=255,
        blank=True,
        null=True,
    )
    methodical_url = models.URLField(
        verbose_name='ссылка на методические материалы',
        max_length=255,
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        'course.Course',
        verbose_name='курс',
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    order_num = models.PositiveIntegerField(
        verbose_name='порядковый номер',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    models.Q(methodical_url__isnull=False) |
                    models.Q(video_url__isnull=False)
                ),
                name='field_fullness'),
        ]
        unique_together = ['course_id', 'order_num']
        ordering = ['course_id', 'order_num']

    def __str__(self):
        return self.name
