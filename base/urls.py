from django.urls import path
from . import views

urlpatterns = [
    # login
    path('login/', views.Login, name="login"),
    path('', views.dashboard, name="dashboard"),
    
    # gestion des joueurs
    path('creer-joueur', views.creerJoueur, name="creer-joueur"),
    path('joueurs', views.joueurs, name="joueurs"),
    path('modifier-joueur/<str:pk>/', views.modifierJoueur, name="modifier-joueur"),
    path('supprimer-joueur/<str:pk>/', views.supprimerJoueur, name="supprimer-joueur"),

    # gestion des missions
    path('gestion-missions', views.gestionM, name="gestion-missions"),
    
    
    path('afficher-missions', views.afficherM, name="afficher-missions"),
    path('modifier-mission/<str:pk>/', views.modifierM, name="modifier-mission"),
    path('supprimer-mission/<str:pk>/', views.supprimerM, name="supprimer-mission"),
    
    #creer des missions
    path('creer-quizz', views.quizzM, name="creer-quizz"),
    path('creer-type-quizz', views.creerTypeQuizz, name="creer-type-quizz"),
    path('creer-sanction', views.sanctionM, name="creer-sanction"),

    
    #path('creer-gestion-commerciale', views.gectioncM, name="creer-gestion-commerciale"),

    path('parametrage-gc', views.parametrageGC, name="parametrage-gc"),
    path('fournisseurs', views.fournisseurs, name="fournisseurs"),
    path('creer-fournisseur', views.CreerFournisseur, name="creer-fournisseur"),
    path('modifier-fournisseur/<str:pk>/', views.ModifierFournisseur, name="modifier-fournisseur"),
    path('supprimer-fournisseur/<str:pk>/', views.SupprimerFournisseur, name="supprimer-fournisseur"),

    path('clients', views.clients, name="clients"),
    path('creer-client', views.CreerClient, name="creer-client"),
    path('modifier-client/<str:pk>/', views.ModifierClient, name="modifier-client"),
    path('supprimer-client/<str:pk>/', views.SupprimerClient, name="supprimer-client"),

    path('produits', views.produits, name="produits"),
    path('creer-produit', views.CreerProduit, name="creer-produit"),
    path('modifier-produit/<str:pk>/', views.ModifierProduit, name="modifier-produit"),
    path('supprimer-produit/<str:pk>/', views.SupprimerProduit, name="supprimer-produit"),

    path('creer-gestion-commerciale', views.gestioncM, name="creer-gestion-commerciale"),

    #jouer
    path("jouer", views.jouer, name="jouer"),
    path("jouer/1", views.generer, name="generer"),
    path("jouer/resultat", views.resultat, name="resultat"),
    path("jouer/1/save", views.update_temps, name="save"),

    path('listing/<str:pk>/', views.listing , name="listing"),

    path('logout/', views.Logout, name="logout")
]