from typing import Optional, Type

from django.forms.models import BaseModelForm
from django.shortcuts import HttpResponse, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, View

from .models import Brand, Color, Country, Nationality, Phone


# Create your views here.
class PhonePut(CreateView):
    model = Phone
    template_name = "phone/spec_put.html"
    fields = "__all__"


class PhoneUpdate(UpdateView):
    model = Phone
    template_name = "phone/spec_put.html"
    fields = "__all__"


class PhoneDelete(DeleteView):
    model = Phone
    template_name = "phone/spec_delete.html"


class ColorPut(CreateView):
    model = Color
    template_name = "phone/spec_put.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "رنگ"
        return context


class ColorDelete(DeleteView):
    model = Color
    template_name = "phone/spec_delete.html"
    success_url = reverse_lazy("phone:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "رنگ"
        return context


class ColorUpdate(UpdateView):
    model = Color
    template_name = "phone/spec_put.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "رنگ"
        return context


class CountryPut(CreateView):
    model = Country
    template_name = "phone/spec_put.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "کشور"
        return context


class CountryUpdate(UpdateView):
    model = Country
    template_name = "phone/spec_put.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "کشور"
        return context


class CountryDelete(DeleteView):
    model = Country
    template_name = "phone/spec_delete.html"
    success_url = reverse_lazy("phone:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "کشور"
        return context


class BrandPut(CreateView):
    model = Brand
    template_name = "phone/spec_put.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "برند"
        return context


class BrandDelete(DeleteView):
    model = Brand
    template_name = "phone/spec_delete.html"
    success_url = reverse_lazy("phone:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "برند"
        return context


class BrandUpdate(UpdateView):
    model = Brand
    template_name = "phone/spec_put.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "برند"
        return context


class NationalityPut(CreateView):
    model = Nationality
    template_name = "phone/spec_put.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ملیت"
        return context


class NationalityUpdate(UpdateView):
    model = Nationality
    template_name = "phone/spec_put.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ملیت"
        return context


class NationalityDelete(DeleteView):
    model = Nationality
    template_name = "phone/spec_delete.html"
    success_url = reverse_lazy("phone:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ملیت"
        return context


class Index(View):
    template_name = "phone/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)
