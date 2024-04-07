from django.db import models

# Create your models here.
class Partners(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Партнер')

class Contracts(models.Model):
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE, verbose_name='Партнер')
    numbers = models.CharField(max_length=20, verbose_name="Номер договора")
    date = models.DateField(verbose_name="Дата договора")
    total = models.IntegerField(verbose_name="Сумма договора")
    status = models.BooleanField(default=True, verbose_name="Договор действует")

class Service(models.Model):
    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE, verbose_name="Договор")
    service = models.CharField(max_length=200, verbose_name="Наименование услуги")
    amount = models.IntegerField(verbose_name="Количество")
    price = models.IntegerField(verbose_name="Цена")
    total = models.GeneratedField(expression=models.F('amount')*models.F('price'), db_persist=True, output_field=models.IntegerField(), verbose_name="Сумма")