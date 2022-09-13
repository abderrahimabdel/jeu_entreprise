from dataclasses import fields
from django.forms import ModelForm

from .models import Client, Fournisseur, Produit, QuizzM, Joueur, GestioncM, sanctionsM
#from django.contrib.auth.forms import UserCreationForm

class createPlayerForm(ModelForm):
    class Meta:
        model = Joueur
        fields = ["username", "password1", "password2", "points"]

class createQuizzForm(ModelForm):
    class Meta:
        model = QuizzM
        fields = '__all__'
        exclude = ['type']

class createSanctionForm(ModelForm):
    class Meta:
        model = sanctionsM
        fields = '__all__'
        exclude = ['type']

class createFournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'
        labels = {
            "Nom": "Nom du Fournisseur",
            "Adresse": "Adresse",
            "cp": "CP",
            "ville": "Ville",
            "remise": "Remise spécifique",
            "divers": "Divers",
        }
    
class createProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'
        labels = {
            "Nom": "Nom du Produit",
            "prix_achatHT": "Prix d’achat HT",
            "prix_venteHT": "Prix de vente HT",
            "prix_venteTTC": "Prix de vente TTC",
            "TVA": "Taux de TVA",
            "stock": "Stock",
            "fournisseur" : "Fournisseur type"}

class createClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            "Nom": "Nom du Client",
            "Adresse": "Adresse",
            "cp": "CP",
            "ville": "Ville",
            "remise": "Remise spécifique",
            "divers": "Divers",
        }

class createGestionComForm(ModelForm):
    class Meta:
        model = GestioncM
        fields = "__all__"
        exclude = ['type']