from dataclasses import fields
from django.forms import ModelForm
from django import forms

from .models import Choix, Client, Fournisseur, Produit, QuizzM, Joueur, GestioncM, sanctionsM
#from django.contrib.auth.forms import UserCreationForm

class createPlayerForm(ModelForm):
    class Meta:
        model = Joueur
        fields = ["username", "password1", "password2", "points", "type_de_missions"]
        widgets = {
            'type_de_missions': forms.CheckboxSelectMultiple(),
        }

class createQuizzForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super(createQuizzForm, self).__init__(*args, **kwargs)
            self.fields['type_de_quizz'].queryset = self.fields['type_de_quizz'].queryset.exclude(choix__in=[p for p in Choix.objects.all() if p.choix in ["sanction", "gestion-commerciale"]])


    class Meta:
        model = QuizzM
        fields = '__all__'
        exclude = ['type']

class createChoixForm(ModelForm):
    class Meta:
        model = Choix
        fields = '__all__'
        labels = {"choix":"type du quizz"}

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