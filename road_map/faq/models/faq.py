from django.db import models


class FAQ(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='слаг'
    )
    body = models.TextField(
        verbose_name='текст'
    )
    category = models.ForeignKey(
        'faq.FAQCategory',
        verbose_name='категория',
        on_delete=models.CASCADE,
        related_name='faqs'
    )

    class Meta:
        verbose_name = 'часто задаваемый вопрос'
        verbose_name_plural = 'часто задаваемые вопросы'

    def __str__(self):
        return self.name
