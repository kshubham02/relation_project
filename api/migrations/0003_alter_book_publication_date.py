# Generated by Django 5.0.7 on 2024-08-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_book_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
