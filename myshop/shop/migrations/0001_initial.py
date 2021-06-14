# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alloy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Сплав',
                'verbose_name_plural': 'Сплавы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsertIn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Вставка',
                'verbose_name_plural': 'Вставки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='Артикул', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Название продукта', max_length=200, db_index=True)),
                ('slug', models.SlugField(verbose_name='URL', max_length=200)),
                ('image', models.ImageField(verbose_name='Изображение продукта', blank=True, upload_to='products/%Y/%m/%d')),
                ('price', models.DecimalField(verbose_name='Цена (руб.)', max_digits=10, decimal_places=2)),
                ('stock', models.PositiveIntegerField(verbose_name='Количество на складе')),
                ('available', models.BooleanField(verbose_name='Активно', default=True)),
                ('created', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='Дата изменения', auto_now=True)),
                ('description', models.TextField(verbose_name='Описание', blank=True)),
                ('weight', models.DecimalField(verbose_name='Вес (г.)', blank=True, default=0, max_digits=5, decimal_places=2)),
                ('size_ring', models.DecimalField(verbose_name='Ширина кольца', blank=True, default=0, max_digits=5, decimal_places=1)),
                ('size_x', models.DecimalField(verbose_name='Ширина', blank=True, default=0, max_digits=5, decimal_places=1)),
                ('size_y', models.DecimalField(verbose_name='Высота', blank=True, default=0, max_digits=5, decimal_places=1)),
                ('size_z', models.DecimalField(verbose_name='Средняя ширина', blank=True, default=0, max_digits=5, decimal_places=1)),
                ('alloy', models.ManyToManyField(verbose_name='Сплав', related_name='products', to='shop.Alloy')),
                ('brend', models.ManyToManyField(verbose_name='Бренд', related_name='products', to='shop.Brend')),
                ('category', models.ForeignKey(verbose_name='Категория', related_name='products', to='shop.Category')),
                ('insertin', models.ManyToManyField(verbose_name='Вставка', related_name='products', to='shop.InsertIn')),
            ],
            options={
                'verbose_name': 'Товар',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(to='shop.Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
