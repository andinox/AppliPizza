from django.contrib import admin

# Register your models here.
from webpizza.models import Ingredient, Pizza, Composition
admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Composition)