from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def new(request):
    return HttpResponse("This is is a page for New products")


def categories(request):
    return HttpResponse("This is a Categories Page")




