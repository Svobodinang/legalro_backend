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
    title2 = models.CharField(max_length=100, default='')
    pageName = models.CharField(max_length=100, default='')
    text = models.TextField()
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
        verbose_name = 'Секция услуг'
        verbose_name_plural = 'Секция услуг'

    def __str__(self):
        return self.title


# class services(serviceSection)
