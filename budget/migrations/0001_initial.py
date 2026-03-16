from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('icon', models.CharField(blank=True, default='glyphicon-tag', max_length=50, verbose_name='Ícono (glyphicon)')),
                ('color', models.CharField(blank=True, default='#5bc0de', max_length=20, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Descripción')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Monto')),
                ('transaction_type', models.CharField(choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto')], default='gasto', max_length=10, verbose_name='Tipo')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('notes', models.TextField(blank=True, verbose_name='Notas')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='budget.Category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Transacción',
                'verbose_name_plural': 'Transacciones',
                'ordering': ['-date', '-id'],
            },
        ),
    ]
