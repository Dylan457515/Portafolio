from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Dylan'
        context['titulo'] = 'Esta es una platilla de ejemplo en Django'
        context['titulo'] = 'Esta es una platilla de ejemplo en Django'
        return context