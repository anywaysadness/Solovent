from django.contrib import admin
from users.models import User, EmailVerification
from store.admin import BasketAdmin
from django.utils.safestring import mark_safe


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'get_small_image', )
    list_display_links = ('id', 'username',)
    readonly_fields = ('id', 'date_joined', 'get_small_image', 'get_xs_image',)
    fieldsets = (
        ('For admin', {
            "fields": (
                'id',
                ('username', 'password'),
                'date_joined',
                ('user_permissions', 'groups'),
                ('is_superuser', 'is_staff', 'is_active')
            )
        }),
        ('User information', {
            "fields": (
                ('first_name', 'last_name'),
                ('email', 'phone_number'),
                'is_verified_email',
                'get_xs_image', 'image',
            )
        }),
    )
    inlines = (BasketAdmin,)

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


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
