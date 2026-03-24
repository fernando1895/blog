from django.contrib import admin
from .models import Asistencia


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = (
        'fecha', 'nombre_apellido', 'culto', 'convocado_para',
        'color_equipo', 'lider_celula', 'linea', 'participo_devocional'
    )
    list_filter = ('culto', 'convocado_para', 'color_equipo', 'participo_devocional', 'fecha')
    search_fields = ('nombre_apellido', 'lider_celula', 'linea')
    date_hierarchy = 'fecha'
