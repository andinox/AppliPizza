from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from applicompte.models import PizzaUser
from webpizza.models import Pizza


# Create your views here.


def deconnexion(request):
    logout(request)
    return render(
        request,
        'applicompte/login.html'
    )


def connexion(request):
    usr = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=usr, password=pwd)
    if user is not None:
        login(request, user)
        lesPizzas = Pizza.objects.all()
        return render(
            request,
            'applipizza/debasepizzas.html',
            {'pizzas': lesPizzas, 'user': user}
        )
    else:
        return render(
            request,
            'applicompte/login.html'
        )


def formulaireInscription(request):
    return render(
        request,
        'applicompte/register.html'
    )


def traitementFormulaireInscription(request):
    # récupération des champs du formulaire

    fst = request.POST['first_name']
    lst = request.POST['last_name']

    usr = request.POST['username']
    eml = request.POST['email']

    pwd = request.POST['password']
    img = request.FILES['image']

    # création d'un PizzaUser
    user = PizzaUser()

    # affectation des champs récupérés aux attributs du PizzaUser
    user.first_name = fst
    user.last_name = lst
    user.username = usr
    user.email = eml
    user.set_password(pwd)
    user.image = img

    # sauvegarde du PizzaUser dans la base de données
    user.save()

    # connexion du PizzaUser
    login(request, user)

    # récupération des pizzas
    lesPizzas = Pizza.objects.all()

    # on renvoie l'appel du template, avec les pizzas et le PizzaUser
    return render(
        request,
        'applipizza/debasepizzas.html',
        {
            "pizzas": lesPizzas,
            "user": user,
        },
    )