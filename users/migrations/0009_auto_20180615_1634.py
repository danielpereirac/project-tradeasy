# Generated by Django 2.0.4 on 2018-06-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180614_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publicationDate',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='collection',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='size',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
