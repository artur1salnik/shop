# Generated by Django 3.0.6 on 2020-05-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200515_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/products/', verbose_name='Фото'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
