from django.db import models


class LessonLink(models.Model):
    name = models.CharField(
        verbose_name='текст ссылки',
        max_length=120,
    )
    link = models.URLField(
        verbose_name='ссылка',
    )
    lesson = models.ForeignKey(
        'course.Lesson',
        verbose_name='урок',
        on_delete=models.CASCADE,
        related_name='links'
    )

    class Meta:
        verbose_name = 'полезная ссылка'
        verbose_name_plural = 'полезные ссылки'

    def __str__(self):
        return self.name
