from django.db import models
from django.contrib.auth.models import User

class restorantModel(models.Model):
    root_usr = models.ForeignKey(User, on_delete=models.CASCADE)
    rest_name = models.CharField(max_length=1000, )
    rest_url = models.CharField(max_length=1000, null=True, blank=True)
    rest_owner_name = models.CharField(max_length=1000, null=True, blank=True)
    rest_owner_phone = models.IntegerField(null=True, blank=True)
    rest_phone = models.IntegerField(null=True, blank=True)
    rest_addres = models.CharField(max_length=10000, null=True, blank=True)
    rest_area = models.CharField(max_length=1000, null=True, blank=True)
    rest_city = models.CharField(max_length=1000, null=True, blank=True)
    rest_state = models.CharField(max_length=1000, null=True, blank=True)
    rest_country = models.CharField(max_length=1000, null=True, blank=True)
    rest_opntime = models.TimeField(null=True, blank=True)
    rest_clstime = models.TimeField(null=True, blank=True)
    rest_type = models.CharField(max_length=500, null=True, blank=True)
    rest_like = models.ManyToManyField(User, related_name='like')
    rest_dislike = models.ManyToManyField(User, related_name='dislike')
    rest_image = models.CharField(max_length=10000, null=True, blank=True)
    rest_reg_date = models.DateTimeField()

    def __str__(self):
        return self.rest_name

class restMenuModel(models.Model):
    restorant = models.ForeignKey(restorantModel, on_delete=models.CASCADE)
    Menu = models.CharField(max_length=3000)
    spacial = models.CharField(max_length=3000, null=True, blank=True)
    offer = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.Menu

class restFoodModel(models.Model):
    Menu = models.ForeignKey(restMenuModel, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=3000)
    food_image = models.CharField(max_length=5000, null=True, blank=True)
    food_description = models.TextField(max_length=10000, null=True, blank=True)
    food_like = models.ManyToManyField(User, related_name='foodlike')
    food_dislike = models.ManyToManyField(User, related_name='fooddislike')
    food_prize = models.PositiveIntegerField()
    veg = models.BooleanField(null=True, blank=True)
    nonveg = models.BooleanField(null=True, blank=True)
    egg = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.food_name



