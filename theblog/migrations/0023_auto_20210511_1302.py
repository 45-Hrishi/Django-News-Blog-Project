# Generated by Django 3.1.4 on 2021-05-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0022_remove_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
