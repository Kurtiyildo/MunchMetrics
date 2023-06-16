# Generated by Django 4.2.1 on 2023-06-14 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Metrics', '0010_reviewmeal_user_alter_reviewmeal_meal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviewmeal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviewrestaurant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]