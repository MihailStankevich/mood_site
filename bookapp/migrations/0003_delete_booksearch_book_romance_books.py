# Generated by Django 4.1 on 2022-09-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_booksearch'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookSearch',
        ),
        migrations.AddField(
            model_name='book',
            name='romance_books',
            field=models.BooleanField(default=False),
        ),
    ]
