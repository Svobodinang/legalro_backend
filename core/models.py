from django.db import models


class GeneralInfo(models.Model):
    logo = models.CharField(max_length=30, default='')
    slogan = models.CharField(max_length=30, default='')
    aboutUs = models.TextField(default='')
    servicesText = models.CharField(max_length=500, default='')
    garantiesText = models.CharField(max_length=100, default='')
    formTitle = models.CharField(max_length=30, default='')
    formText = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Основная информация'
        verbose_name_plural = 'Основная информация'

    def __str_(self):
        return self.logo


class RunTitle(models.Model):
    text = models.CharField(max_length=30, default='')

    class Meta:
        verbose_name = 'Заголовки'
        verbose_name_plural = 'Заголовки'

    def __str_(self):
        return self.text


class Garanty(models.Model):
    title = models.CharField(max_length=50, default='')
    text = models.TextField(default='')

    class Meta:
        verbose_name = 'Гарантии'
        verbose_name_plural = 'Гарантии'

    def __str_(self):
        return self.title


class Benefit(models.Model):
    picture = models.FileField()
    text = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'

    def __str_(self):
        return self.text


class Services(models.Model):
    title = models.CharField(max_length=50, default='')
    picture = models.FileField()
    text = models.TextField(default='')
    button = models.BooleanField(default=None)

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str_(self):
        return self.title
