from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='listings_index'),
    #path('mineDjango', include('listings.urls')),
    # ajoutez vos autres URLs ici
]