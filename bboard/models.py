from django.db import models


class Bb(models.Model):

    title = models.CharField(max_length=50, verbose_name='Товар', help_text='*Название товара', default='Какой-то товар')
    # slug = models.SlugField(max_length=50, unique_for_date='publish')
    content = models.TextField(null=True, blank=True, verbose_name='Описание', help_text='Описание товара')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена', help_text='Цена товара')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано', help_text='Дата и время публикации товара')

    rubric=models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика', help_text='*Выбор категории товара')

    class Meta:
        verbose_name_plural='Объявления'
        verbose_name='Объявление'
        ordering=['-published']
        # indexes=[
        #     models.Index(fields=['-published', 'title'], name='bb_partial', condition=models.Q(price__lte=10))
        # ]

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Рубрики'
        verbose_name='Рубрика'
        ordering=['name']