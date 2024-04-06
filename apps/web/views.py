from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #agregando datos para el portafolio

        #agregando informacion basica
        context['nombre'] = 'Dylan'
        context['apellido'] = ' Quispe Huallpa'
        context['gmail'] = ' dylanquispehuallpa80@gmail.com'
        context['numero'] = '+591 67046908'
        return context