# Generated by Django 5.1.1 on 2024-11-16 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_productfact_brand_slug_productfact_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttranslation',
            name='description',
            field=models.TextField(verbose_name='Description des'),
        ),
    ]
