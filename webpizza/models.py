from django.db import models


class Ingredient(models.Model):
    idIngredient = models.AutoField(primary_key=True)

    nomIngredient = models.CharField(max_length=50, verbose_name='nom de l\'ingrédient')

    def __str__(self) -> str:
        return self.nomIngredient


class Pizza(models.Model):
    idPizza = models.AutoField(primary_key=True)
    nomPizza = models.CharField(max_length=50, verbose_name='nom de la pizza')
    prix = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='prix de la pizza')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self) -> str:
        return 'pizza' + self.nomPizza + ' ( prix : ' + str(self.prix) + ' €)'


class Composition(models.Model):
    class Meta:
        unique_together = ('ingredient', 'pizza')

    idComposition = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100, verbose_name='quantité de l\'ingrédient')

    def __str__(self) -> str:
        ing = self.ingredient
        piz = self.pizza
        return ing.nomIngredient + ' fait partie de la pizza' + piz.nomPizza + '(quantité : )' + self.quantity + ')'
