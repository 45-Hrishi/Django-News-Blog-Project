# Generated by Django 3.1.4 on 2021-04-08 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0005_auto_20210408_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='theblog.category'),
        ),
    ]
