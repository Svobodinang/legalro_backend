from django.db import models


class GeneralInfo(models.Model):
    mainTitle = models.CharField(max_length=100, default='')
    slogan = models.CharField(max_length=100, default='')
    about = models.TextField(default='')
    aboutSlogan = models.CharField(max_length=100, default='')
    servicesSlogan = models.CharField(max_length=100, default='')
    formTitle = models.CharField(max_length=100, default='')
    formText = models.CharField(max_length=100, default='')
    footerSlogan = models.CharField(max_length=100, default='')
    companyName = models.CharField(max_length=100, default='')
    adress = models.CharField(max_length=100, default='')
    telephone = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    facebook = models.CharField(max_length=100, default='')
    vk = models.CharField(max_length=100, default='')
    telegram = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Основная информация'
        verbose_name_plural = 'Основная информация'

    def __str__(self):
        return self.mainTitle


class Garanty(models.Model):
    picture = models.FileField()
    title = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Гарантии'
        verbose_name_plural = 'Гарантии'

    def __str__(self):
        return self.title


class Goals(models.Model):
    picture = models.FileField()
    title = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Цели'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.title


class Docs(models.Model):
    document = models.FileField()
    title = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title


class ServiceBlock(models.Model):
    title = models.CharField(max_length=100, default='')
    title2 = models.CharField(max_length=100, default='', blank=True)
    pageName = models.CharField(max_length=100, default='')
    text = models.TextField(blank=True)
    picture = models.FileField()

    class Meta:
        verbose_name = 'Блок услуг'
        verbose_name_plural = 'Блок услуг'

    def __str__(self):
        return self.title


class ServiceSection(models.Model):
    serviceBlock = models.ForeignKey(ServiceBlock, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Секции услуг'
        verbose_name_plural = 'Секции услуг'

    def __str__(self):
        return self.title


class Service(models.Model):
    serviceSection = models.ForeignKey(
        ServiceSection, on_delete=models.CASCADE)
    accent = models.CharField(max_length=5, default='', blank=True)
    title = models.TextField(blank=True)
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class PriceSection(models.Model):
    title = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Секции цен'
        verbose_name_plural = 'Секции цен'

    def __str__(self):
        return self.title


class PriceBlock(models.Model):
    priceSection = models.ForeignKey(
        PriceSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='', blank=True)

    class Meta:
        verbose_name = 'Блоки цен'
        verbose_name_plural = 'Блоки цен'

    def __str__(self):
        return self.priceSection.title + '. ' + self.title


class Price(models.Model):
    priceBlock = models.ForeignKey(
        PriceBlock, on_delete=models.CASCADE)
    title = models.TextField(blank=True)
    price = models.CharField(max_length=100, default='')
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return self.title
