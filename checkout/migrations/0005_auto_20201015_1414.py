# Generated by Django 3.1.1 on 2020-10-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_userorders_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singleorder',
            name='singleordertotal',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=100),
        ),
    ]