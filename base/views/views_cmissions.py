
from multiprocessing import context
from django.contrib.auth.decorators import permission_required, login_required

from django.shortcuts import render, redirect

from base.models import Choix, Client, Fournisseur, GestioncM, Joueur, Produit, QuizzM, VEntrepriseM, Mission

from base.forms import createChoixForm, createClientForm, createFournisseurForm, createGestionComForm, createProduitForm, createQuizzForm, createPlayerForm, createVEntrepriseForm

# Create your views here.


@permission_required('is_superuser')
def gestionM(request):
    types = ["quizz", "vie d'entreprise", "gestion-commerciale"]
    context = {'types': types}
    return render(request, "gestion_missions.html", context)

@permission_required('is_superuser')
def afficherM(request):
    q = request.GET.get("q")
    missions = Mission.objects.all()
    types = ["quizz", "vie d'entreprise", "gestion-commerciale"]
    types += list(map(lambda x:x.choix,Choix.objects.all()))
    types = list(set(types))
    if q:
        missions = Mission.objects.filter(type=q)
    
    return render(request, "afficher_missions.html", {"missions":missions, "types" : types})

@permission_required('is_superuser')
def modifierM(request, pk):
    mission = Mission.objects.get(titre=pk)
    if mission.type == "quizz":
        mission = QuizzM.objects.get(titre=pk)
        return ModifierMission(request, mission, createQuizzForm, "quizzM.html")
    elif mission.type == "vie d'entreprise":
        mission = VEntrepriseM.objects.get(titre=pk)
        return ModifierMission(request, mission, createVEntrepriseForm, "vie_entrepriseM.html")
    elif mission.type == "gestion-commerciale":
        mission = GestioncM.objects.get(titre=pk)
        return ModifierMission(request, mission, createGestionComForm, "gestionc_mission.html")
    return redirect("afficher-missions")

@permission_required('is_superuser')
def ModifierMission(request, mission, Form, html_fichier):
    form = Form(instance=mission)
    if request.method == "POST":
        form = Form(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            return redirect("afficher-missions")
    context = {'form': form}
    return render(request, html_fichier, context)

@permission_required('is_superuser')
def supprimerM(request, pk):
    mission = Mission.objects.get(titre=pk)
    if request.method == "POST":
        mission.delete()
        return redirect("afficher-missions")
    return render(request, "supprimer.html", {"joueur" : mission})
    
@permission_required('is_superuser')
def quizzM(request):
    form = createQuizzForm()
    if request.method == "POST":
        form = createQuizzForm(request.POST)
        form.instance.type = "quizz"
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("afficher-missions")
    context = {'form': form}
    return render(request, "quizzM.html", context)

@permission_required('is_superuser')
def creerTypeQuizz(request):
    form = createChoixForm()
    if request.method == "POST":
        form = createChoixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("creer-quizz")
    context = {'form': form}
    return render(request, "creer_type_quizz.html", context)

@permission_required('is_superuser')
def vieEntrepriseM(request):
    form = createVEntrepriseForm()
    if request.method == "POST":
        form = createVEntrepriseForm(request.POST)
        form.instance.type = "vie d'entreprise"
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("afficher-missions")
    context = {'form': form}
    return render(request, "vie_entrepriseM.html", context)

@permission_required('is_superuser')
def parametrageGC(request):
    context = {"types" : ["Fournisseurs", "Clients", "Produits"]}
    return render(request, "parametrage_gc.html", context)

@permission_required('is_superuser')
def CreerX(request, Form, fichier_html, page, type):
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(page)
    return render(request, fichier_html, context={"form":form, 'type':type, "page":page})

@permission_required('is_superuser')
def ModifierX(request ,objet, Form , fichier_html, page, type):
    form = Form(instance=objet)
    if request.method == "POST":
        form = Form(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            return redirect(page)
    return render(request, fichier_html, context={"form":form, 'type':type,"page":page})

@permission_required('is_superuser')
def SupprimerX(request ,objet, page):
    if request.method == "POST":
        objet.delete()
        return redirect(page)
    return render(request, "supprimer.html", {"joueur" : objet})

@permission_required('is_superuser')
def fournisseurs(request):
    form = createFournisseurForm()
    labels = list(map(lambda x:x.label, form.base_fields.values()))
    fournisseurs = Fournisseur.objects.all()
    return render(request, "fournisseurs.html", context={"labels" : labels, "fournisseurs":fournisseurs})


@permission_required('is_superuser')
def CreerFournisseur(request):
    Form = createFournisseurForm
    fichier_html = "creer_objet.html"
    page = "fournisseurs"
    return CreerX(request, Form, fichier_html, page, type="fournisseur")

@permission_required('is_superuser')
def ModifierFournisseur(request,pk):
    Form = createFournisseurForm
    fichier_html = "creer_objet.html"
    page = "fournisseurs"
    objet = Fournisseur.objects.get(Nom=pk)
    return ModifierX(request ,objet, Form , fichier_html, page, type="fournisseur")

@permission_required('is_superuser')
def SupprimerFournisseur(request, pk):
    page = "fournisseurs"
    objet = Fournisseur.objects.get(Nom=pk)
    return SupprimerX(request ,objet, page)

@permission_required('is_superuser')
def clients(request):
    form = createClientForm()
    labels = list(map(lambda x:x.label, form.base_fields.values()))
    clients = Client.objects.all()
    return render(request, "clients.html", context={"labels" : labels, "clients":clients})

@permission_required('is_superuser')
def CreerClient(request):
    Form = createClientForm
    fichier_html = "creer_objet.html"
    page = "clients"
    return CreerX(request, Form, fichier_html, page, type="client")

@permission_required('is_superuser')
def ModifierClient(request,pk):
    Form = createClientForm
    fichier_html = "creer_objet.html"
    page = "clients"
    objet = Client.objects.get(Nom=pk)
    return ModifierX(request ,objet, Form , fichier_html, page, type="client")

@permission_required('is_superuser')
def SupprimerClient(request, pk):
    page = "clients"
    objet = Client.objects.get(Nom=pk)
    return SupprimerX(request ,objet, page)

@permission_required('is_superuser')
def produits(request):
    form = createProduitForm()
    labels = list(map(lambda x:x.label, form.base_fields.values()))
    produits = Produit.objects.all()
    return render(request, "produits.html", context={"labels" : labels, "produits":produits})

@permission_required('is_superuser')
def CreerProduit(request):
    Form = createProduitForm
    fichier_html = "creer_objet.html"
    page = "produits"
    return CreerX(request, Form, fichier_html, page, type="produit")

@permission_required('is_superuser')
def ModifierProduit(request,pk):
    Form = createProduitForm
    fichier_html = "creer_objet.html"
    page = "produits"
    objet = Produit.objects.get(Nom=pk)
    return ModifierX(request ,objet, Form , fichier_html, page, type="produit")

@permission_required('is_superuser')
def SupprimerProduit(request, pk):
    page = "produits"
    objet = Produit.objects.get(Nom=pk)
    return SupprimerX(request ,objet, page)

@permission_required('is_superuser')
def gestioncM(request):
    form = createGestionComForm()
    if request.method == "POST":
        form = createGestionComForm(request.POST)
        form.instance.type = "gestion-commerciale"
        if form.is_valid():
            form.save()
            return redirect("afficher-missions")
    context = {'form': form}
    return render(request, "gestionc_mission.html", context)