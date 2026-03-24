from django.db import models
from django.utils import timezone


class Asistencia(models.Model):
    CONSOLIDAR = 'consolidar'
    MINISTRAR = 'ministrar'
    AMBOS = 'ambos'
    CONVOCADO_CHOICES = [
        (CONSOLIDAR, 'Consolidar'),
        (MINISTRAR, 'Ministrar'),
        (AMBOS, 'Ambos'),
    ]

    ROJO = 'Rojo'
    AZUL = 'Azul'
    VERDE = 'Verde'
    AMARILLO = 'Amarillo'
    NARANJA = 'Naranja'
    MORADO = 'Morado'
    COLOR_CHOICES = [
        (ROJO, 'Rojo'),
        (AZUL, 'Azul'),
        (VERDE, 'Verde'),
        (AMARILLO, 'Amarillo'),
        (NARANJA, 'Naranja'),
        (MORADO, 'Morado'),
    ]

    AM = 'AM'
    PM = 'PM'
    CULTO_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    fecha = models.DateField(default=timezone.now, verbose_name='Fecha')
    participo_devocional = models.BooleanField(
        default=False,
        verbose_name='Participó del devocional'
    )
    convocado_para = models.CharField(
        max_length=20,
        choices=CONVOCADO_CHOICES,
        verbose_name='Convocado para'
    )
    color_equipo = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        verbose_name='Color de equipo'
    )
    culto = models.CharField(
        max_length=2,
        choices=CULTO_CHOICES,
        verbose_name='Culto AM o PM'
    )
    nombre_apellido = models.CharField(
        max_length=200,
        verbose_name='Nombre y Apellido'
    )
    lider_celula = models.CharField(
        max_length=200,
        verbose_name='Líder de Célula'
    )
    linea = models.CharField(
        max_length=200,
        verbose_name='Línea a la que pertenece'
    )

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['-fecha', '-id']

    def __str__(self):
        return '{} - {} ({})'.format(self.fecha, self.nombre_apellido, self.culto)
