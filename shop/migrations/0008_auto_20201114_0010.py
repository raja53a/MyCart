# Generated by Django 2.2.14 on 2020-11-13 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20201114_0010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='subcategory',
            new_name='sub_category',
        ),
    ]
