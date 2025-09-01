from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def hello(request):
    bands = Band.objects.all()
    return HttpResponse('<h1>Hello Dante!</h1>')

def index(request):
    return HttpResponse("Bienvenue dans la section listings!")

from django.http import HttpResponse
from .models import Band

def index(request):
    bands = Band.objects.all()
    
    # Créer une réponse HTML simple pour afficher les groupes
    response_html = "<h1>Mes Groupes de Musique</h1>"
    
    if bands:
        response_html += "<ul>"
        for band in bands:
            response_html += f"<li>{band.name}</li>"
        response_html += "</ul>"
    else:
        response_html += "<p>Aucun groupe trouvé. Ajoutez-en via l'admin Django !</p>"
    
    return HttpResponse(response_html)