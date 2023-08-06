from django.contrib import admin

from .models import Brand, Color, Country, Nationality, Phone


# Register your models here.
class SpecAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Fields to display in the list view
    list_filter = ("name",)


class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "brand",
        "nationality",
        "color",
        "size",
        "price",
        "country",
        "inventory",
    )  # Fields to display in the list view
    list_filter = (
        "brand",
        "nationality",
        "color",
        "size",
        "price",
        "country",
        "inventory",
    )  # Fields to use as filters


admin.site.register(Color, SpecAdmin)
admin.site.register(Nationality, SpecAdmin)
admin.site.register(Country, SpecAdmin)
admin.site.register(Brand, SpecAdmin)
admin.site.register(Phone, PhoneAdmin)
