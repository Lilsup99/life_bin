from django.http import HttpResponse
from django.shortcuts import render

''' 
PAGINA PRINCIPAL
'''
def home(request):
    
    return render(request, 'esperanza.html',{})

def team(request):
    return render(request,'Plantillas\esperanza.html',{})