from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    icon = models.CharField(max_length=50, blank=True, default='glyphicon-tag',
                            verbose_name='Ícono (glyphicon)')
    color = models.CharField(max_length=20, blank=True, default='#5bc0de',
                             verbose_name='Color')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name


class Transaction(models.Model):
    INCOME = 'ingreso'
    EXPENSE = 'gasto'
    TYPE_CHOICES = [
        (INCOME, 'Ingreso'),
        (EXPENSE, 'Gasto'),
    ]

    description = models.CharField(max_length=200, verbose_name='Descripción')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Monto')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='transactions',
                                 verbose_name='Categoría')
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES,
                                        default=EXPENSE,
                                        verbose_name='Tipo')
    date = models.DateField(default=timezone.now, verbose_name='Fecha')
    notes = models.TextField(blank=True, verbose_name='Notas')

    class Meta:
        verbose_name = 'Transacción'
        verbose_name_plural = 'Transacciones'
        ordering = ['-date', '-id']

    def __str__(self):
        return '{} - {} ({})'.format(self.date, self.description, self.amount)
