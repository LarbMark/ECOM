from django.contrib import admin
from .models import Categorie,Produit,Commande

class AdmiCat(admin.ModelAdmin):
    list_display = ('nom','date_ajout')

class AdmiProd(admin.ModelAdmin):
    list_display = ('titre','prix','categorie','date_ajout')

class AdmiCommande(admin.ModelAdmin):
    list_display = ('date_commande','items','nom','email','adresse','ville','pays','montant')

admin.site.register(Categorie,AdmiCat)
admin.site.register(Produit,AdmiProd)
admin.site.register(Commande,AdmiCommande)


