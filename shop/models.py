from django.db import models
from django.urls import reverse

from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True,
                            verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Выберите категорию'
                                 )
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='static/images/', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_detail', args=[self.id, self.slug])
    

class Basket(models.Model):
     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
     product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
     quantity = models.PositiveSmallIntegerField(default=0)
     created_timestamp = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f'Корзина для {self.user.email} | Продукт: {self.product.name}' 
     