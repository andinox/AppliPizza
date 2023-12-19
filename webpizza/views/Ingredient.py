from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from webpizza.forms import PizzaForm, IngredientForm, CompositionForm
from webpizza.models import Pizza, Composition, Ingredient


class IngredientsView:
    @staticmethod
    def ingredients(request):
        return render(request, 'applipizza/ingredients.html', {'ingredients': Ingredient.objects.all()})

    @staticmethod
    def update(request, ingredient_id):
        form = IngredientForm(request.POST)
        if form.is_valid():
            ing = Ingredient.objects.get(idIngredient=ingredient_id)
            ing.nomIngredient = form.cleaned_data['nomIngredient']
            ing.imageIng = request.FILES['imageIng'] if request.FILES else ing.imageIng
            ing.save()
            return redirect(f'/ingredients/')

        return render(
            request,
            'applipizza/FormulaireModificationIngredient.html',
            {'ingredient': Ingredient.objects.get(idIngredient=ingredient_id)}
        )

    @staticmethod
    def delete(request, ingredient_id):
        ing = Ingredient.objects.get(idIngredient=ingredient_id)
        ing.delete()
        return redirect('/ingredients/')

    @staticmethod
    def add(request):
        if not request.POST: redirect("ingredients/add/")
        form = IngredientForm(request.POST)
        if form.is_valid():
            ing = Ingredient()
            ing.nomIngredient = form.cleaned_data['nomIngredient']
            ing.imageIng = request.FILES['imageIng']
            ing.save()
            return redirect('/ingredients/')
        return render(request, 'applipizza/FormulaireCreationIngredient.html')
