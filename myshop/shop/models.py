from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                           args=[self.slug])
    def get_absolute_url_new(self):
        return reverse('product_catalog_new',
                           args=[self.slug])


class Alloy(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Сплав'
        verbose_name_plural = 'Сплавы'

    def __str__(self):
        return self.name

    def get_absolute_url_a(self):
        return reverse('shop:product_list_by_alloy',
                           args=[self.slug])

class Brend(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

class InsertIn(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Вставка'
        verbose_name_plural = 'Вставки'

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Артикул")
    category = models.ForeignKey(Category, related_name='products',verbose_name="Категория")
    alloy = models.ManyToManyField(Alloy, related_name='products',verbose_name="Сплав")
    brend = models.ManyToManyField(Brend, related_name='products',verbose_name="Бренд")
    insertin = models.ManyToManyField(InsertIn, related_name='products', verbose_name="Вставка")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название продукта")
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Изображение продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб.)")
    stock = models.PositiveIntegerField( verbose_name="Количество на складе")
    available = models.BooleanField(default=True, verbose_name="Активно")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    description = models.TextField(blank=True, verbose_name="Описание")
    weight = models.DecimalField( default=0,decimal_places=2, max_digits=5, verbose_name="Вес (г.)", blank=True)
    size_ring = models.DecimalField(default=0,decimal_places=1, max_digits=5, blank=True, verbose_name="Ширина кольца")
    size_x = models.DecimalField(default=0,decimal_places=1, max_digits=5, blank=True, verbose_name="Ширина")
    size_y = models.DecimalField(default=0,decimal_places=1, max_digits=5, blank=True, verbose_name="Высота")
    size_z = models.DecimalField(default=0,decimal_places=1, max_digits=5, blank=True, verbose_name="Средняя ширина")


    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                           args=[self.id, self.slug])

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})