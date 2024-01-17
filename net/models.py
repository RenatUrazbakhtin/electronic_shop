from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}

choices = {
    "factory": "factory",
    "net": "net",
    "entrepreneur": "entrepreneur"
}

class Organization(models.Model):
    """
    Модель Организации
    """

    name = models.CharField(max_length=100, verbose_name='название')
    organization_type = models.CharField(max_length=100, choices=choices, verbose_name='тип организации')
    supplier = models.ForeignKey('Organization', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность', **NULLABLE)
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'Организация {self.name}'
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Product(models.Model):
    """
    Модель продукта
    """

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='организация', related_name='products')

    name = models.CharField(max_length=100, verbose_name='название продукта')
    model = models.CharField(max_length=100, verbose_name='модель продукта')
    launch_date = models.DateField(verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return f'Продукт {self.name} организации {self.organization}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Contact(models.Model):
    """
    Модель Контактов
    """

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='организация', related_name='contacts')

    email = models.EmailField(unique=True, verbose_name='почта')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street_name = models.CharField(max_length=100, verbose_name='улица')
    number = models.CharField(max_length=5, verbose_name='номер дома')

    def __str__(self):
        return f'Контакты организации {self.organization}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

