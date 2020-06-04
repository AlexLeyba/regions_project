from django.db import models


class IndustryModel(models.Model):
    """Отросли"""

    name = models.CharField('Название отросли', max_length=500, )
    value_one = models.CharField('Рынок', max_length=500, blank=True, null=True)
    value_two = models.CharField('Инвестиции', max_length=500, blank=True, null=True)
    value_three = models.CharField('IRR', max_length=500, blank=True, null=True)
    value_four = models.CharField('Проекты', max_length=500, blank=True, null=True)
    slug = models.SlugField('en', default='ru', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отрaсль'
        verbose_name_plural = 'Отрасли'


class IndustryMetaModel(models.Model):
    """Общая информация по отросли в ЦФО"""

    name = models.CharField('Заголовок', max_length=1000, blank=True, null=True)
    value_one = models.CharField('Строка 1', max_length=1000, blank=True, null=True)
    value_two = models.CharField('Строка 2', max_length=1000, blank=True, null=True)
    value_three = models.CharField('Строка 3', max_length=1000, blank=True, null=True)
    value_four = models.CharField('Строка 4', max_length=1000, blank=True, null=True)
    maps = models.ImageField('Карта', upload_to='images/', blank=True, null=True)
    parent = models.ForeignKey(IndustryModel, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Общую информацию по отросли в ЦФО'
        verbose_name_plural = 'Общая информация по отросли в ЦФО'


class RegionModel(models.Model):
    """Регионы"""

    name = models.CharField('Название региона', max_length=500)
    region_code = models.CharField('Код региона', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Интерактивная карта'


class RegionMetaModel(models.Model):
    """Подробная информация по региону"""

    name = models.CharField('Статистика', max_length=1000, blank=True, null=True)
    parent = models.ForeignKey(RegionModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подробная информация по региону'
        verbose_name_plural = 'Подробная информация по региону'


class RegionCityModel(models.Model):
    """Крупные города и населенные пункты в регионе"""
    name = models.CharField('Название населенного пункта', max_length=1000, blank=True, null=True)
    parent = models.ForeignKey(RegionModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'


class StoriesModel(models.Model):
    """Проекты"""

    name = models.CharField('Заголовок', max_length=500, blank=True, null=True)
    value_one = models.CharField('Подзаголовок', max_length=500, blank=True, null=True)
    value_two = models.CharField('Регион', max_length=500, blank=True, null=True)
    value_three = models.CharField('Инвестиции', max_length=500, blank=True, null=True)
    value_four = models.CharField('IRR', max_length=500, blank=True, null=True)
    parent = models.ForeignKey(IndustryModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
