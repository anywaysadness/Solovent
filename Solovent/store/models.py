from django.db import models
from users.models import User
from django.utils.timezone import now
from django.conf import settings
import datetime


class Category(models.Model):
    name = models.CharField(max_length=100, default='No category', db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_image/', blank=True, verbose_name='Category_icon')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    # Fields model
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                null=True, related_name='user_rn')
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='Product_Category', verbose_name='Category product')

    name = models.CharField(max_length=250, db_index=True, verbose_name='Name product')
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=250, db_index=True)
    image = models.ImageField(upload_to='product_image/', blank=True, verbose_name='Photo product')
    description = models.TextField(max_length=500, blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=10, default=0.0, decimal_places=2, verbose_name='Price for person')
    number_of_guests = models.PositiveSmallIntegerField(default=1, null=True, blank=True,
                                                        verbose_name='Minimal number of guests')
    available = models.BooleanField(default=True, verbose_name='Availability')

    # Meta options
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Product {self.name} created by'


class WorkDays(models.Model):
    MON = 'MONDAY'
    TUE = 'TUESDAY'
    WED = 'WEDNESDAY'
    THU = 'THURSDAY'
    FRI = 'FRIDAY'
    SAT = 'SATURDAY'
    SUN = 'SUNDAY'

    # DAYS
    DAYS_OF_WORK = [
        (MON, 'Monday'),
        (TUE, 'Tuesday '),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday'),
    ]
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE,
                                blank=True, null=True, related_name='product_rn')
    name_day = models.CharField(max_length=100, blank=True, null=True,
                                default=DAYS_OF_WORK[0][0], choices=DAYS_OF_WORK,
                                verbose_name='Day')
    beginning_of_work_day_time = models.TimeField(default=datetime.time(8, 00),
                                                  verbose_name='Beginning of work time')
    end_of_work_day_time = models.TimeField(default=datetime.time(20, 00),
                                            verbose_name='End of work time')

    class Meta:
        verbose_name = 'day'
        verbose_name_plural = 'days'

    def __str__(self):
        return f'{self.name_day}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Number of guests')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Created time')
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Basket for {self.user.username} | Product: {self.product.name }'

    def sum(self):
        return self.product.price * self.quantity

