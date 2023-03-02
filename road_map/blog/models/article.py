from ckeditor.fields import RichTextField
from django.db import models


class Article(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='слаг'
    )
    body = RichTextField(
        verbose_name='текст'
    )
    category = models.ForeignKey(
        'blog.ArticleCategory',
        verbose_name='категория',
        on_delete=models.CASCADE,
        related_name='articles'
    )

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return self.name

