from django.db import models


class ArticleCategory(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=150,
    )
    slug = models.SlugField(
        verbose_name='слаг'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name
