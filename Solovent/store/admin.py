from django.contrib import admin
from .models import Category, Product, Basket, WorkDays
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_small_image')

    readonly_fields = ('id', 'get_small_image', 'get_xs_image',)
    fieldsets = (
        ('For admin', {
            "fields": (
                'id',
            )
        }),
        ('Category information', {
            "fields": (
                ('name', 'slug', 'get_xs_image')
            )
        }),
    )

    def get_small_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width=30 height=30')
        else:
            return "No image"
    get_small_image.short_description = "Image S-size"

    def get_xs_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width=100 height=100')
        else:
            return "No image"
    get_xs_image.short_description = "Image XS-size"


class WorkDaysInlines(admin.StackedInline):
    model = WorkDays
    extra = 1
    max_num = 7


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (WorkDaysInlines,)
    list_display = ('id', 'name', 'category', 'price', 'created_time', 'creator', 'get_small_image')
    list_display_links = ('id', 'name',)
    readonly_fields = ('id', 'created_time', 'get_small_image', 'get_xs_image',)
    fieldsets = (
        ('INFORMATION FOR ADMIN', {
            "fields": (
                'id', ('creator', 'created_time',),
                ('slug', 'available'),
            )
        }),
        ('PRODUCT INFORMATION', {
            "fields": (
                ('name', 'category'),
            )
        }),
        (None, {
            "fields": (
                ('price', 'number_of_guests'), 'description',
            )
        }),
        (None, {
            "fields": (
                'get_xs_image', 'image',
            )
        }),
    )

    def get_small_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width=30 height=30')
        else:
            return "No image"
    get_small_image.short_description = "Image S-size"

    def get_xs_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width=300 height=300')
        else:
            return "No image"

    get_xs_image.short_description = "Image XS-size"

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProductAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['creator'].initial = request.user
        if str(request.user) != 'admin':
            form.base_fields['creator'].disbled = request.user

        return form
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp',)
    readonly_fields = ('created_timestamp',)
    extra = 0



