# Generated by Django 2.0.5 on 2018-05-28 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Item')),
                ('author', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=20, null=True)),
                ('publisher', models.CharField(max_length=20, null=True)),
                ('publicationDate', models.DateTimeField()),
            ],
            bases=('users.item',),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Item')),
                ('collection', models.CharField(max_length=20)),
                ('edition', models.CharField(max_length=20, null=True)),
                ('color', models.CharField(max_length=20, null=True)),
            ],
            bases=('users.item',),
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Item')),
                ('size', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20, null=True)),
                ('brand', models.CharField(max_length=20, null=True)),
                ('collection', models.CharField(max_length=20, null=True)),
            ],
            bases=('users.item',),
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Item')),
                ('plataform', models.CharField(max_length=20)),
                ('series', models.CharField(max_length=20, null=True)),
                ('releaseDate', models.CharField(max_length=20, null=True)),
            ],
            bases=('users.item',),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
