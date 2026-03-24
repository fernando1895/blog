from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Asistencia
from .forms import AsistenciaForm


def dashboard(request):
    asistencias = Asistencia.objects.all()

    total = asistencias.count()
    total_am = asistencias.filter(culto=Asistencia.AM).count()
    total_pm = asistencias.filter(culto=Asistencia.PM).count()
    total_devocional = asistencias.filter(participo_devocional=True).count()

    recientes = asistencias.order_by('-fecha', '-id')[:10]

    return render(request, 'consolidacion/dashboard.html', {
        'total': total,
        'total_am': total_am,
        'total_pm': total_pm,
        'total_devocional': total_devocional,
        'recientes': recientes,
    })


def asistencia_list(request):
    asistencias = Asistencia.objects.all()

    culto = request.GET.get('culto')
    convocado = request.GET.get('convocado')
    color = request.GET.get('color')

    if culto:
        asistencias = asistencias.filter(culto=culto)
    if convocado:
        asistencias = asistencias.filter(convocado_para=convocado)
    if color:
        asistencias = asistencias.filter(color_equipo=color)

    return render(request, 'consolidacion/asistencia_list.html', {
        'asistencias': asistencias,
        'selected_culto': culto,
        'selected_convocado': convocado,
        'selected_color': color,
        'culto_choices': Asistencia.CULTO_CHOICES,
        'convocado_choices': Asistencia.CONVOCADO_CHOICES,
        'color_choices': Asistencia.COLOR_CHOICES,
    })


@login_required
def asistencia_new(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consolidacion_list')
    else:
        form = AsistenciaForm(initial={'fecha': timezone.now().date()})
    return render(request, 'consolidacion/asistencia_form.html', {
        'form': form,
        'title': 'Nueva Asistencia',
    })


@login_required
def asistencia_edit(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return redirect('consolidacion_list')
    else:
        form = AsistenciaForm(instance=asistencia)
    return render(request, 'consolidacion/asistencia_form.html', {
        'form': form,
        'title': 'Editar Asistencia',
        'asistencia': asistencia,
    })


@login_required
def asistencia_delete(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        asistencia.delete()
        return redirect('consolidacion_list')
    return render(request, 'consolidacion/asistencia_confirm_delete.html', {
        'object': asistencia,
    })
