# Generated by Django 3.1.4 on 2021-04-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_profile_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Mobile',
            field=models.CharField(default='', max_length=11),
        ),
    ]
