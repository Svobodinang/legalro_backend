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

    class Meta:
        verbose_name = 'Основная информация'
        verbose_name_plural = 'Основная информация'

    def __str_(self):
        return self.mainTitle

class Garanty(models.Model):
    picture = models.FileField()
    title = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Гарантии'
        verbose_name_plural = 'Гарантии'

    def __str_(self):
        return self.title