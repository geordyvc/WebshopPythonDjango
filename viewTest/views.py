from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.urls import reverse
from django.template import RequestContext


from .models import Merk
from .models import Product
from .models import Categorie
# Create your views here.

def homepage(request):
    menu_list = Categorie.objects.all()
    brand_list = Merk.objects.all()
    producten = Product.objects.all()


    context = {'menu_list': menu_list, 'brand_list': brand_list, 'producten': producten}
    return render(request, 'homepage.html', context)


def producten_merk(request, merk_id):
    merk = get_object_or_404(Merk, id=merk_id)
    producten = Product.objects.filter(idMerk=merk.id)
    title = merk.name
    menu_list = Categorie.objects.all()
    brand_list = Merk.objects.all()
    context = {'producten': producten, 'title': title, 'menu_list': menu_list, 'brand_list': brand_list}
    return render(request, 'productenpage.html', context)

def producten_product_id(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    menu_list = Categorie.objects.all()
    brand_list = Merk.objects.all()

    context = {'product': product, 'menu_list': menu_list, 'brand_list': brand_list}
    return render(request, 'productpage.html', context)

def producten_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    producten = Product.objects.filter(idCategorie=categorie.id)
    title = categorie.name
    menu_list = Categorie.objects.all()
    brand_list = Merk.objects.all()
    context = {'producten': producten, 'title': title, 'menu_list': menu_list, 'brand_list': brand_list}
    return render(request, 'productenpage.html', context)

def winkelmand(request):
    response = render_to_response()

def addproduct(request, product_id):






# def producten_categorie(request, categorieId):
#
# def producten():
