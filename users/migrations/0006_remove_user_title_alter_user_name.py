# Generated by Django 4.2.4 on 2023-09-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_date_of_birth_user_name_user_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
