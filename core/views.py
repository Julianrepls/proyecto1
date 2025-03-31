from django.views.generic import View
from django.shortcuts import render



class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request, 'index.html', context) #aquí vamos a retornar el request, luego el templates que es la info en html que por ahora vamos a dejarlo en comillas; y un contexto que va a ser un diccionario
    
