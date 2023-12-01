from django import forms
from django.forms import ModelForm
from webpizza.models import Pizza, Ingredient, Composition


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['nomIngredient']


class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['idPizza', 'nomPizza', 'prix']


class CompositionForm(ModelForm):

    class Meta:
        model = Composition
        fields = ['ingredient', 'quantity']

