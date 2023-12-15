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
from django.contrib import admin
from django.urls import path, include
from webpizza import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('pizzas/', views.pizzas),
    path('ingredients/', views.ingredients),
    path('pizzas/<int:pizza_id>/', views.pizza),
    path('ingredients/add', views.FormulaireCreationIngredient),
    path('pizzas/add/', views.FormulaireCreationPizza),
    path('pizzas/<int:pizza_id>/delete', views.supprimerPizza),
    path('pizzas/<int:pizza_id>/deleteIngredient', views.PizzaDeleteIngredient),
    path('pizzas/<int:pizza_id>/update', views.afficherFormulaireModificationPizza),
    path('ingredients/<int:ingredient_id>/update', views.updateIngredient),
    path('ingredients/<int:ingredient_id>/delete', views.deleteIngredient),
    path('', include('applicompte.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
