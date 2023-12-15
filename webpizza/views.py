from django.shortcuts import render, redirect

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
    IngredientsOfPizza = []
    for compo in IngredientsOfPiz:
        IngredientsOfPizza.append(
            {'nom': compo.ingredient.nomIngredient, 'quantity': compo.quantity}
        )
    return render(
        request,
        'applipizza/pizza.html',
        {
            'pizza': laPizza,
            'ingredients': IngredientsOfPizza,
            'IngredientsM': Ingredients,
        }
    )


def addIngredient(request, pizza_id):
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
        IngredientsOfPizza = []
        for compo in IngredientsOfPiz:
            IngredientsOfPizza.append(
                {'nom': compo.ingredient.nomIngredient, 'quantity': compo.quantity}
            )
        return render(
            request,
            'applipizza/pizza.html',
            {
                'pizza': laPizza,
                'ingredients': IngredientsOfPizza,
                'IngredientsM': Ingredients,
                'error': 'Erreur dans le formulaire'
            }
        )

    laPizza = Pizza.objects.get(idPizza=pizza_id)
    IngredientsOfPiz = Composition.objects.filter(pizza_id=laPizza)
    Ingredients = Ingredient.objects.exclude(idIngredient__in=IngredientsOfPiz.values_list('ingredient_id'))
    IngredientsOfPizza = []
    for compo in IngredientsOfPiz:
        IngredientsOfPizza.append(
            {'nom': compo.ingredient.nomIngredient, 'quantity': compo.quantity}
        )

    return render(
        request,
        'applipizza/pizza.html',
        {
            'pizza': laPizza,
            'ingredients': IngredientsOfPizza,
            'IngredientsM': Ingredients,
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
    print(form)
    if form.is_valid():
        monIngredient = form.cleaned_data['nomIngredient']
        image = request.FILES['imageIng']
        ing = Ingredient()
        ing.nomIngredient = monIngredient
        ing.imageIng = image
        ing.save()
    return render(
        request,
        'applipizza/TraitementFormulaireCreationIngredient.html',
        {'ingredient': monIngredient}
    )


def creePizza(request):
    form = PizzaForm(request.POST)
    maPizza = None
    if form.is_valid():
        maPizza = form.cleaned_data['nomPizza']
        prix = form.cleaned_data['prix']
        piz = Pizza()
        piz.nomPizza = maPizza
        piz.imagePizza = request.FILES['imagePizza']
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
    return redirect('/pizzas/')


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
         'prix': prix, }
    )


def updatePizza(request, pizza_id):
    form = PizzaForm(request.POST)
    maPizza = None
    if form.is_valid():
        maPizza = form.cleaned_data['nomPizza']
        prix = form.cleaned_data['prix']
        piz = Pizza.objects.get(idPizza=pizza_id)
        piz.nomPizza = maPizza
        if request.FILES:
            image = request.FILES['imagePizza']
            piz.imagePizza = image
        piz.prix = prix
        piz.save()
    return redirect('/pizzas/')


def deleteIngredient(request, ingredient_id):
    ing = Ingredient.objects.get(idIngredient=ingredient_id)
    ing.delete()
    return ingredients(request)


def home(request):
    return render(
        request,
        'applipizza/home.html',
        {'t': 'test'}
    )


def updateIngredientPOST(request, ingredient_id):
    form = IngredientForm(request.POST)
    monIngredient = None
    if form.is_valid():
        ing = Ingredient.objects.get(idIngredient=ingredient_id)
        monIngredient = form.cleaned_data['nomIngredient']
        if request.FILES:
            image = request.FILES['imageIng']
            ing.imageIng = image
        ing.nomIngredient = monIngredient
        ing.save()
    return ingredients(request)


def updateIngredient(request, ingredient_id):
    if request.method == "POST":
        return updateIngredientPOST(request, ingredient_id)
    ing = Ingredient.objects.get(idIngredient=ingredient_id)
    name = ing.nomIngredient

    return render(
        request,
        'applipizza/FormulaireModificationIngredient.html',
        {'ingredient': name}
    )


def PizzaDeleteIngredient(request, pizza_id):
    form = IngredientForm(request.POST)
    if form.is_valid():
        ingredient = form.cleaned_data['nomIngredient']
        composition = Composition.objects.get(ingredient__nomIngredient=ingredient, pizza_id=pizza_id)
        composition.delete()
    return redirect(f'/pizzas/{pizza_id}', pizza_id)
