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

        #experiencia
        context['titulo_experiencia_1']='DESARROLLADORA WEB SENIOR '
        context['subtitulo_experiencia_1'] = 'Proyecto Semestral'
        context['contenido_experiencia_1'] = 'En el marco de mi formación académica, lideré con éxito el desarrollo de un sistema de historial clínico con base de datos para un proyecto semestral. Este sistema no solo facilitó la gestión eficiente de los datos clínicos, sino que también sirvió como un modelo para futuras implementaciones tecnológicas en el sector de la salud.'

        
        #educasion
        context['lugar_estudios']= 'Universidad Saleciana de Bolivia'
        context['carrera'] = 'Ingenieria de Sistemas'
        context['seguimiento'] = 'August 2006 - Presente'

        #contenido interno
        context['presentacion'] = 'Mi formación académica me ha equipado con un conocimiento profundo de los principios de la programación y las últimas tecnologías. A través de proyectos universitarios y colaboraciones en equipo, he desarrollado una sólida comprensión de los marcos de desarrollo ágil y las metodologías de programación estructurada. Estoy preparado para aplicar estas habilidades en un entorno profesional, contribuyendo con ideas innovadoras y soluciones eficientes a los desafíos técnicos.'



        return context