from django.shortcuts import redirect, render
from .models import Produit,Commande
from django.core.paginator import Paginator
def index(request):
    produits = Produit.objects.all()
    val_cherche = request.GET.get("item-name")
    if val_cherche != '' and val_cherche is not None:
        produits= Produit.objects.filter(titre__icontains=val_cherche)
    paginer = Paginator(produits,4)
    page = request.GET.get('page')
    produits=paginer.get_page(page)
    return render(request,'shop/index.html',{'produits' : produits})

def detail(request,myid):
    produit=Produit.objects.get(id=myid)
    return render(request,'shop/detail.html',{ 'produit':produit })

def checkout(request):
    if request.method == "POST" :
        items=request.POST.get("items")
        nom =request.POST.get("nom")
        email =request.POST.get("email")
        adresse =request.POST.get("adresse")
        ville =request.POST.get("ville")
        pays =request.POST.get("pays")
        zipcode =request.POST.get("zipcode")
        montant = request.POST.get("montant")
        cde=Commande(items=items,nom=nom,email=email,adresse=adresse,ville=ville,pays=pays,zipcode=zipcode,montant=montant)
        cde.save()
        return redirect('confirmation')
        
    return render(request,'shop/checkout.html')

def confirmation(request):
    cdm =Commande.objects.all()[:1]
    for item in cdm:
        nom =item.nom
        
    return render(request,'shop/confirmation.html',{'nom':nom})