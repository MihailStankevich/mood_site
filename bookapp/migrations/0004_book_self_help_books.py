# Generated by Django 4.1 on 2022-09-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_delete_booksearch_book_romance_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='self_help_books',
            field=models.BooleanField(default=False),
        ),
    ]
