from django.shortcuts import render

# Create your views here.
"""views.py bns app"""
def home(request):
    """docstring for home"""
    return render(request,"uterg/home.html",{})
  
def equipamentos(request):
    """docstring for home"""
    return render(request,"uterg/equipamentos.html",{})
  
def graficos(request):
    """docstring for graficos"""
    return render(request,"uterg/graficos.html",{})
  
def relatorios(request):
    """docstring for graficos"""
    return render(request,"uterg/relatorios-tecnicos.html",{})
  
def dados(request):
    """docstring for graficos"""
    return render(request,"uterg/series-de-dados.html",{})
 