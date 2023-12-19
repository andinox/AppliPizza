"""
URL configuration for AppliPizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from webpizza import views
from webpizza.views import PizzaView
from webpizza.views import IngredientsView

urlpatterns = [
    path('', PizzaView.pizzas),
    path('pizzas/', PizzaView.pizzas),
    path('pizzas/<int:pizza_id>/', PizzaView.pizza),
    path('pizzas/add/', PizzaView.add),
    path('pizzas/<int:pizza_id>/delete', PizzaView.delete),
    path('pizzas/<int:pizza_id>/deleteIngredient', PizzaView.deleteIngredient),
    path('pizzas/<int:pizza_id>/update', PizzaView.update),
    path('ingredients/', IngredientsView.ingredients),
    path('ingredients/add', IngredientsView.add),
    path('ingredients/<int:ingredient_id>/update', IngredientsView.update),
    path('ingredients/<int:ingredient_id>/delete', IngredientsView.delete),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
