from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #agregando datos para el portafolio

        #agregando informacion basica
        context['nombre'] = ' Dylan'
        context['apellido'] = ' Quispe Huallpa'
        context['gmail'] = ' dylanquispehuallpa80@gmail.com'
        context['numero'] = '+591 67046908'
        context['ubicacion'] = 'El Alto · La Paz · Bolivia ·'




        #contenido interno
        context['presentacion'] = 'Mi formación académica me ha equipado con un conocimiento profundo de los principios de la programación y las últimas tecnologías. A través de proyectos universitarios y colaboraciones en equipo, he desarrollado una sólida comprensión de los marcos de desarrollo ágil y las metodologías de programación estructurada. Estoy preparado para aplicar estas habilidades en un entorno profesional, contribuyendo con ideas innovadoras y soluciones eficientes a los desafíos técnicos.'



        return context