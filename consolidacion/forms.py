from django import forms
from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = (
            'fecha',
            'participo_devocional',
            'convocado_para',
            'color_equipo',
            'culto',
            'nombre_apellido',
            'lider_celula',
            'linea',
        )
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
