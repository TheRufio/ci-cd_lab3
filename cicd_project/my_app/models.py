from django.db import models

class MyUser(models.Model):
    name = models.CharField('Ім\'я',max_length=100)
    surname = models.CharField('Прізвище',max_length=100)
    email = models.EmailField('Пошта')
    adress = models.TextField('Адреса')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'