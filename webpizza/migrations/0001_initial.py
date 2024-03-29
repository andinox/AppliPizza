# Generated by Django 4.2.7 on 2023-11-24 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('idIngredient', models.AutoField(primary_key=True, serialize=False)),
                ('monIngredient', models.CharField(max_length=50, verbose_name="nom de l'ingrédient")),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('idPizza', models.AutoField(primary_key=True, serialize=False)),
                ('nomPizza', models.CharField(max_length=50, verbose_name='nom de la pizza')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=50, verbose_name='prix de la pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('idComposition', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=100, verbose_name="quantité de l'ingrédient")),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpizza.ingredient')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpizza.pizza')),
            ],
            options={
                'unique_together': {('ingredient', 'pizza')},
            },
        ),
    ]
