# Generated by Django 4.2.4 on 2023-09-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
