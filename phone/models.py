from django.db import models

# Create your models here.


class Color(models.base):
    name = models.CharField(verbose_name="رنگ", max_length=20, blank=False)

    class Meta:
        verbose_name_plural = "رنگ‌ها"
        verbose_name = "رنگ"


class Brand(models.base):
    name = models.CharField(verbose_name="نام برند", max_length=30, blank=False)

    class Meta:
        verbose_name_plural = "برند"
        verbose_name = "برند‌ها"


class Country(models.base):
    name = models.CharField(verbose_name="کشور", max_length=30, blank=False)

    class Meta:
        verbose_name_plural = "کشور"
        verbose_name = "کشور‌ها"


class Nationality(models.base):
    name = models.CharField(verbose_name="ملیت", max_length=30, blank=False)

    class Meta:
        verbose_name_plural = "ملیت"
        verbose_name = "ملیت‌ها"


class Phone(models.base):
    brand = models.ForeignKey(
        Brand, verbose_name="برند", on_delete=models.CASCADE, blank=False
    )
    nationality = models.ForeignKey(
        Nationality, verbose_name="ملیت", on_delete=models.CASCADE, blank=False
    )
    model = models.CharField(
        verbose_name="مدل", max_length=50, unique=True, blank=False
    )
    price = models.PositiveIntegerField(verbose_name="قیمت", blank=False)
    color = models.ForeignKey(
        Color, verbose_name="رنگ", on_delete=models.CASCADE, blank=False
    )
    size = models.DecimalField(
        verbose_name="سایز صفحه نمایش", max_digits=4, decimal_places=2, blank=False
    )
    inventory = models.BooleanField(verbose_name="وضعیت موجودی", default=False)
    country = models.ForeignKey(
        Country, verbose_name="کشور", on_delete=models.CASCADE, blank=False
    )

    class Meta:
        verbose_name_plural = "گوشی"
        verbose_name = "گوشی‌ها"
