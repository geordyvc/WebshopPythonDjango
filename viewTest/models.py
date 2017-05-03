from django.db import models
# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Merk(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits= 20, decimal_places=2)
    voorraad = models.IntegerField()
    btwPercentage = models.IntegerField()
    summary = models.CharField(max_length=255)
    picture = models.ImageField(upload_to= 'static/productimages/')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    merk = models.ForeignKey(Merk, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('product')
        verbose_name_plural = ('products')
        ordering = ('name',)



class Adress(models.Model):
    adress = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ' ' + self.adress

class Invoice_Producten(models.Model):
    product = models.ForeignKey(Product)

class Invoice(models.Model):
    invoice_producten = models.ForeignKey(Invoice_Producten, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewtext = models.TextField(max_length=555)

class Gebruiker(models.Model):
    name = models.CharField(max_length=255)
    wachtwoord = models.CharField(max_length=255)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + ' ' + self.name
