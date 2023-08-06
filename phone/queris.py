from django.db.models import F
from django.db.models.query import QuerySet

from .models import Brand, Color, Country, Nationality, Phone


def get_list_phone_nationality(na: Nationality) -> QuerySet:
    return list(Phone.objects.filter(nationality=na).values())


def get_list_phone_brand(na: Brand) -> QuerySet:
    return list(Phone.objects.filter(brand=na).values())


def get_same_brand_and_nationality() -> QuerySet:
    return list(Phone.objects.filter(brand__name=F("nationality__name")).values())
