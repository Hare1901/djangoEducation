from django.shortcuts import render


# Create your views here.

def index(request):
    context = {"title": "Magazine Store"}

    return render(request, "products/index.html", context)


def products(request):
    context = {"title": "Store - Каталог"}
    return render(request, "product/products.html", context)
