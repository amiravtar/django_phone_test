from django.urls import path

from .views import (BrandDelete, BrandPut, BrandUpdate, ColorDelete, ColorPut,
                    ColorUpdate, CountryDelete, CountryPut, CountryUpdate, Index,
                    NationalityDelete, NationalityPut, NationalityUpdate, PhoneDelete,
                    PhonePut, PhoneUpdate)

app_name = "phone"
urlpatterns = [
    path("phone/put", PhonePut.as_view(), name="phone_put"),
    path("phone/<int:pk>", PhoneUpdate.as_view(), name="phone_update"),
    path("phone/<int:pk>/delete", PhoneDelete.as_view(), name="phone_delete"),
    path("country/put", CountryPut.as_view(), name="country_put"),
    path("country/<int:pk>", CountryUpdate.as_view(), name="country_update"),
    path("country/<int:pk>/delete", CountryDelete.as_view(), name="country_delete"),
    path("color/put", ColorPut.as_view(), name="color_put"),
    path("color/<int:pk>", ColorUpdate.as_view(), name="color_update"),
    path("color/<int:pk>/delete", ColorDelete.as_view(), name="color_delete"),
    path("brand/put", BrandPut.as_view(), name="brand_put"),
    path("brand/<int:pk>", BrandUpdate.as_view(), name="brand_update"),
    path("brand/<int:pk>/delete", BrandDelete.as_view(), name="brand_delete"),
    path("nationality/put", NationalityPut.as_view(), name="nationality_put"),
    path(
        "nationality/<int:pk>", NationalityUpdate.as_view(), name="nationality_update"
    ),
    path(
        "nationality/<int:pk>/delete",
        NationalityDelete.as_view(),
        name="nationality_delete",
    ),
    path("", Index.as_view(), name="index"),
]
