from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

CUISINES = [
    ('Chinese', 'CHINESE'),
    ('Italian', 'ITALIAN'),
    ('Turkish', 'TURKISH'),
    ('Mexican', 'MEXICAN'),
    ('Fast Food', 'FAST FOOD'),
    ('Vegan', 'VEGAN'),
    ('Coffee', 'COFFEE'),

]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        instance.groups.add(Group.objects.get(name='NormalUser'))


class Meal(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    cuisine = models.CharField(max_length=75, choices=CUISINES)
    image = models.ImageField(null=True, blank=True, default='images/default.png', upload_to='images/')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=100)
    address = models.CharField(null=True, blank=True, max_length=200)
    cuisine = models.CharField(max_length=75, choices=CUISINES)
    image = models.ImageField(null=True, blank=True, default='images/default.png', upload_to='images/')

    def __str__(self):
        return self.name


class ReviewRestaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class ReviewMeal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE, related_name='reviews')
    title = models.TextField(max_length=100)
    description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
