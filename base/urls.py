from django.urls import path
from . import views

urlpatterns = [
    # login
    path('login/', views.Login, name="login"),
    path('', views.dashboard, name="dashboard"),
    
    # gestion des joueurs
    path('joueurs/creer-joueur', views.creerJoueur, name="creer-joueur"),
    path('joueurs', views.joueurs, name="joueurs"),
    path('joueurs/modifier-joueur/<str:pk>/', views.modifierJoueur, name="modifier-joueur"),
    path('joueurs/supprimer-joueur/<str:pk>/', views.supprimerJoueur, name="supprimer-joueur"),

    # gestion des missions
    path('missions', views.gestionM, name="gestion-missions"),
    
    
    path('missions/afficher-missions', views.afficherM, name="afficher-missions"),
    path('missions/modifier-mission/<str:pk>/', views.modifierM, name="modifier-mission"),
    path('missions/supprimer-mission/<str:pk>/', views.supprimerM, name="supprimer-mission"),
    
    #creer des missions
    path('missions/creer-quizz', views.quizzM, name="creer-quizz"),
    path('missions/creer-type-quizz', views.creerTypeQuizz, name="creer-type-quizz"),
    path("missions/creer-vie d'entreprise", views.vieEntrepriseM, name="creer-vie d'entreprise"),

    
    #path('creer-gestion-commerciale', views.gectioncM, name="creer-gestion-commerciale"),

    path('missions/parametrage-gc', views.parametrageGC, name="parametrage-gc"),
    path('missions/fournisseurs', views.fournisseurs, name="fournisseurs"),
    path('missions/fournisseurs/creer-fournisseur', views.CreerFournisseur, name="creer-fournisseur"),
    path('missions/fournisseurs/modifier-fournisseur/<str:pk>/', views.ModifierFournisseur, name="modifier-fournisseur"),
    path('missions/fournisseurs/supprimer-fournisseur/<str:pk>/', views.SupprimerFournisseur, name="supprimer-fournisseur"),

    path('missions/clients', views.clients, name="clients"),
    path('missions/clients/creer-client', views.CreerClient, name="creer-client"),
    path('missions/clients/modifier-client/<str:pk>/', views.ModifierClient, name="modifier-client"),
    path('missions/clients/supprimer-client/<str:pk>/', views.SupprimerClient, name="supprimer-client"),

    path('missions/produits', views.produits, name="produits"),
    path('missions/produits/creer-produit', views.CreerProduit, name="creer-produit"),
    path('missions/produits/modifier-produit/<str:pk>/', views.ModifierProduit, name="modifier-produit"),
    path('missions/produits/supprimer-produit/<str:pk>/', views.SupprimerProduit, name="supprimer-produit"),

    path('missions/creer-gestion-commerciale', views.gestioncM, name="creer-gestion-commerciale"),

    #jouer
    path("jouer", views.jouer, name="jouer"),
    path("jouer/1", views.generer, name="generer"),
    path("jouer/resultat", views.resultat, name="resultat"),
    path("jouer/1/save", views.update_temps, name="save"),

    path('listing/<str:pk>/', views.listing , name="listing"),

    path('logout/', views.Logout, name="logout")
]