from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PizzaUser(User):
    image = models.ImageField(default='images/default.png', upload_to='imagesUsers/')