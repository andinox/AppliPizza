from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from webpizza.forms import PizzaForm, IngredientForm, CompositionForm
from webpizza.models import Pizza, Composition, Ingredient


class PizzaView:
    @staticmethod
    def pizzas(request):
        lesPizzas = Pizza.objects.all()
        return render(request, 'applipizza/pizzas.html', {'pizzas': lesPizzas})

    @staticmethod
    def update(request, pizza_id):
        form = PizzaForm(request.POST)
        if form.is_valid():
            piz = Pizza.objects.get(idPizza=pizza_id)
            piz.nomPizza = form.cleaned_data['nomPizza']
            piz.imagePizza = request.FILES['imagePizza'] if request.FILES else piz.imagePizza
            piz.prix = form.cleaned_data['prix']
            piz.save()
            return redirect(f'/pizzas/{pizza_id}')
        return render(request, 'applipizza/FormulaireModificationPizza.html', {
            'pizza': Pizza.objects.get(idPizza=pizza_id)
        })

    @staticmethod
    def add(request):
        if not request.POST: redirect("pizzas/add/")
        form = PizzaForm(request.POST)
        if form.is_valid():
            piz = Pizza()
            piz.nomPizza = form.cleaned_data['nomPizza']
            piz.imagePizza = request.FILES['imagePizza']
            piz.prix = form.cleaned_data['prix']
            piz.save()
            return redirect('/pizzas/')
        return render(request, 'applipizza/FormulaireCreationPizza.html')

    @staticmethod
    def delete(request, pizza_id):
        piz = Pizza.objects.get(idPizza=pizza_id)
        piz.delete()
        return redirect(f'/pizzas/', pizza_id)

    @staticmethod
    @require_http_methods(["POST"])
    def addIngredient(request, pizza_id):
        form = CompositionForm(request.POST)
        if form.is_valid():
            composition = Composition()
            composition.ingredient = form.cleaned_data['ingredient']
            composition.pizza = Pizza.objects.get(idPizza=pizza_id)
            composition.quantity = form.cleaned_data['quantity']
            composition.save()
        redirect('/pizzas/')

    @staticmethod
    @require_http_methods(["POST"])
    def deleteIngredient(request, pizza_id):
        form = IngredientForm(request.POST)
        if form.is_valid():
            composition = Composition.objects.get(ingredient__nomIngredient=form.cleaned_data['nomIngredient'],
                                                  pizza_id=pizza_id)
            composition.delete()
        return redirect(f'/pizzas/{pizza_id}', pizza_id)

    @staticmethod
    def pizza(request, pizza_id):
        if request.POST: PizzaView.addIngredient(request, pizza_id)

        laPizza = Pizza.objects.get(idPizza=pizza_id)
        IngredientsOfPiz = Composition.objects.filter(pizza_id=laPizza)
        Ingredients = Ingredient.objects.exclude(idIngredient__in=IngredientsOfPiz.values_list('ingredient_id'))

        IngredientsOfPizza = [
            {'nom': compo.ingredient.nomIngredient, 'quantity': compo.quantity} for compo in IngredientsOfPiz
        ]
        return render(
            request,
            'applipizza/pizza.html',
            {
                'pizza': laPizza,
                'ingredients': IngredientsOfPizza,
                'IngredientsM': Ingredients,
            }
        )
