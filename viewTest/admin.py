from django.contrib import admin

# Register your models here.

from .models import Product, Merk, Categorie, Gebruiker, Adress, Invoice, Invoice_Producten, Review

admin.site.register(Product)
admin.site.register(Merk)
admin.site.register(Categorie)
admin.site.register(Gebruiker)
admin.site.register(Adress)
admin.site.register(Invoice)
admin.site.register(Invoice_Producten)
admin.site.register(Review)
