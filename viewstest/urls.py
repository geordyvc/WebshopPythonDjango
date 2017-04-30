"""viewstest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from viewTest import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='index'),
    url(r'^(?P<merk_id>[0-9]+)/merk/$', views.producten_merk, name='merken'),
    url(r'^(?P<product_id>[0-9]+)/product/$', views.producten_product_id, name='product'),
    url(r'^(?P<categorie_id>[0-9]+)/categorie/$', views.producten_categorie, name='categorie'),
    url(r'^/winkelmand/$', views.winkelmand, name='winkelmand'),
    url(r'^(?P<product_id>[0-9]+)/add/product/$', views.addproduct, name='addproduct'),
    # url(r'^producten/categorie/([0-9]{2})/$', views.producten_categorie),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()