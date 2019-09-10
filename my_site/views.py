#my_site/views.py
from django.http import HttpResponse
from django.shortcuts import render



def home_page_view(request):
    """
    Une vue simple qui renvoie une Reponse HTTP "Hello World".
    """
    return HttpResponse('Hello World')


def home_page_view_with_render(request):
    """
    Une vue légèrement plus élaborée qui renvoie un template html
    Django sait où chercher ce template grâce à l'objet TEMPLATES
    du fichier settings.py.
    La navbar est générée en partie à l'aide de la variable sections

    """
    return render(request, "home_page.html",
                  {"sections": ["Section 1",
                                "Section 2",
                                "Section 3"]})



def form(request):
    if request.method == "POST":
        print(request.POST)
        alpha = request.POST["data"]
        print(alpha)
    return render(request, "form_page.html",{"value1":"Valeur envoyé depuis views.py"})

def graphique(request):
    return render(request, "graphique_page.html")