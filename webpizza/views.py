from django.shortcuts import render

from webpizza.forms import IngredientForm, PizzaForm, CompositionForm
from webpizza.models import Pizza, Ingredient, Composition


# Create your views here.

def pizzas(request):
    lesPizzas = Pizza.objects.all()

    return render(
        request,
        'applipizza/pizzas.html',
        {'pizzas': lesPizzas}
    )


def ingredients(request):
    lesIngredients = Ingredient.objects.all()

    return render(
        request,
        'applipizza/ingredients.html',
        {'ingredients': lesIngredients}
    )


def pizza(request, pizza_id):
    if request.method == "POST":
        return addIngredient(request, pizza_id)
    laPizza = Pizza.objects.get(idPizza=pizza_id)
    IngredientsOfPiz = Composition.objects.filter(pizza_id=laPizza)
    Ingredients = Ingredient.objects.exclude(idIngredient__in=IngredientsOfPiz.values_list('ingredient_id'))

    return render(
        request,
        'applipizza/pizza.html',
        {
            'pizza': laPizza,
            'ingredients': IngredientsOfPiz,
            'IngredientsM': Ingredients,
        }
    )


def addIngredient(request, pizza_id):
    global ingredient
    form = CompositionForm(request.POST)
    if form.is_valid():
        ingredient = form.cleaned_data['ingredient']
        composition = Composition()
        composition.ingredient = ingredient
        composition.pizza = Pizza.objects.get(idPizza=pizza_id)
        composition.quantity = form.cleaned_data['quantity']
        composition.save()
    else:
        laPizza = Pizza.objects.get(idPizza=pizza_id)
        IngredientsOfPiz = Composition.objects.filter(pizza_id=laPizza)
        Ingredients = Ingredient.objects.exclude(idIngredient__in=IngredientsOfPiz.values_list('ingredient_id'))

        return render(
            request,
            'applipizza/pizza.html',
            {
                'pizza': laPizza,
                'ingredients': IngredientsOfPiz,
                'IngredientsM': Ingredients,
                'error': 'Erreur dans le formulaire'
            }
        )

    return render(
        request,
        'applipizza/TraitementFormulaireAjoutIngredient.html',
        {
            'pizza': Pizza.objects.get(idPizza=pizza_id),
            'ingredient': ingredient
         }
    )





def FormulaireCreationIngredient(request):
    if request.method == "POST":
        return creeIngredient(request)
    return render(
        request,
        'applipizza/FormulaireCreationIngredient.html',
    )

def creeIngredient(request):
    form = IngredientForm(request.POST)
    monIngredient = None
    if form.is_valid():
        monIngredient = form.cleaned_data['nomIngredient']
    myIngredient = Ingredient.objects.get(nomIngredient=monIngredient)
    composition = Composition()
    composition.ingredient = myIngredient

def creePizza(request):
    form = PizzaForm(request.POST)
    maPizza = None
    if form.is_valid():
        maPizza = form.cleaned_data['nomPizza']
        prix = form.cleaned_data['prix']
        piz = Pizza()
        piz.nomPizza = maPizza
        piz.prix = prix
        piz.save()

    return render(
        request,
        'applipizza/TraitementFormulaireCreationPizza.html',
        {'nom': maPizza}
    )


def FormulaireCreationPizza(request):
    if request.method == "POST":
        return creePizza(request)
    return render(
        request,
        'applipizza/FormulaireCreationPizza.html',
    )


def supprimerPizza(request, pizza_id):
    piz = Pizza.objects.get(idPizza=pizza_id)
    piz.delete()
    return pizzas(request)


def afficherFormulaireModificationPizza(request, pizza_id):
    if request.method == "POST":
        return updatePizza(request, pizza_id)
    piz = Pizza.objects.get(idPizza=pizza_id)
    name = piz.nomPizza
    prix = piz.prix
    print(prix)
    return render(
        request,
        'applipizza/FormulaireModificationPizza.html',
        {'pizza': name,
         'prix': prix,}
    )

def updatePizza(request, pizza_id):
    form = PizzaForm(request.POST)
    maPizza = None
    if form.is_valid():
        maPizza = form.cleaned_data['nomPizza']
        prix = form.cleaned_data['prix']
        piz = Pizza.objects.get(idPizza=pizza_id)
        piz.nomPizza = maPizza
        piz.prix = prix
        piz.save()
    return render(None, 'applipizza/pizzas.html', {'pizzas': Pizza.objects.all()})


def deleteIngredient(request, ingredient_id):
    ing = Ingredient.objects.get(idIngredient=ingredient_id)
    ing.delete()
    return ingredients(request)


def home(request):
    return render(
        request,
        'applipizza/home.html',
        {'t' : 'test'}
    )