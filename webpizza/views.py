from django.shortcuts import render

from webpizza.forms import IngredientForm, PizzaForm
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
    laPizza = Pizza.objects.get(idPizza=pizza_id)
    Ingredients = Composition.objects.filter(pizza_id=laPizza)

    Ingredients = Ingredients.values_list('ingredient_id', flat=True)
    AllIngredients = Ingredient.objects.all()

    print([i for i in Ingredients.values_list()])
    ingredients_restants = ["ddd"]
    return render(
        request,
        'applipizza/pizza.html',
        {
            'pizza': laPizza,
            'ingredients': Ingredients,
            'IngredientsM': ingredients_restants,
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
    monIng = None
    if form.is_valid():

        monIng = form.cleaned_data['nomIngredient']
        print(monIng)
        ingredient = Ingredient()
        ingredient.nomIngredient = monIng
        ingredient.save()

    return render(
        request,
        'applipizza/TraitementFormulaireCreationIngredient.html',
        {'nom': monIng}
    )

def creePizza(request):
    form = PizzaForm(request.POST)
    maPizza = None
    if form.is_valid():
        maPizza = form.cleaned_data[' ']
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

