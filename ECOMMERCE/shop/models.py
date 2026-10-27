from django.db import models

class Categorie(models.Model):
    nom =models.CharField(max_length=200)
    date_ajout =models.DateTimeField(auto_now=True)
    class Meta():
        ordering =['-date_ajout']
    def __str__(self):
         return self.nom

class Produit(models.Model):
    titre =models.CharField(max_length=200)
    prix =models.DecimalField(max_digits=10, decimal_places=2)
    description =models.TextField()
    categorie =models.ForeignKey(Categorie, related_name='categorie', on_delete=models.CASCADE)
    image =models.CharField(max_length=500)
    date_ajout = models.DateTimeField(auto_now=True)
    class Meta():
            ordering =['-date_ajout']
    def __str__(self):
             return self.titre

class Commande(models.Model):
    items =models.CharField(max_length=300)
    nom =models.CharField(max_length=100)
    email = models.EmailField()
    adresse =models.CharField(max_length=100)
    ville = models.CharField(max_length=50)
    pays =models.CharField(max_length=50)
    zipcode =models.CharField(max_length=300)
    date_commande =models.DateTimeField(auto_now=True)
    montant=models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        ordering =['-date_commande']
    def __str__(self):
         return self.nom
    