from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse('<h1>Bienvenidos a mi pagina de Django</h1>')

def plantilla(request):

    template = loader.get_template('plantilla.html')
    
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Juancho',
        'apellido': 'Juancho'
    }
    
    plantilla_generada = template.render(datos)   #pasar datos con el template
    
    return HttpResponse(plantilla_generada)