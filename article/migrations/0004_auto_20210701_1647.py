# Generated by Django 3.1 on 2021-07-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210630_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleinfo',
            name='image',
            field=models.ImageField(blank=True, default='article/default5.jpg', max_length=200, null=True, upload_to='article/%y/%m/%d', verbose_name='封面'),
        ),
    ]
