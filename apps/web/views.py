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

        #intereses
        context['intereses_1'] = 'Como estudiante universitario apasionado por el desarrollo web, aprovecho cada oportunidad para expandir mis conocimientos tanto dentro como fuera del aula. Fuera de la programación, me encanta estar al aire libre; ya sea esquiando en las montañas nevadas o escalando las formaciones rocosas de Colorado, cada estación me ofrece una nueva aventura.'
        context['intereses_2'] = 'En invierno, me deslizo por las pendientes y practico la escalada en hielo, desafiando tanto mi cuerpo como mi mente. Con la llegada del verano, cambio los esquís por una bicicleta de montaña, me sumerjo en la escalada en roca y me relajo remando en kayak.'
        context['intereses_3'] = 'Cuando los estudios me reclaman en casa, me sumerjo en el universo de la ciencia ficción y la fantasía a través de películas y series, lo que alimenta mi creatividad y me inspira en mis proyectos de desarrollo. Además, experimento con recetas en la cocina, lo que me ha convertido en un aspirante a chef entre mis amigos y familiares. Y, por supuesto, siempre estoy al tanto de las últimas tendencias y tecnologías en el mundo del desarrollo web, lo que me permite estar a la vanguardia en mi campo de estudio.'

        return context