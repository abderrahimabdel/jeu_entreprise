
from django.contrib.auth.decorators import permission_required, login_required

from django.shortcuts import render, redirect

from base.models import Client, Fournisseur, GestioncM, Joueur, Produit, QuizzM, sanctionsM, Mission

from base.forms import createChoixForm, createClientForm, createFournisseurForm, createGestionComForm, createProduitForm, createQuizzForm, createPlayerForm, createSanctionForm

# Create your views here.


def gestionM(request):
    types = ["quizz", "sanction", "gestion-commerciale"]
    context = {'types': types}
    return render(request, "gestion_missions.html", context)

def afficherM(request):
    q = request.GET.get("q")
    missions = Mission.objects.all()
    types = ["quizz", "sanction", "gestion-commerciale"]
    if q:
        missions = Mission.objects.filter(type=q)
    
    return render(request, "afficher_missions.html", {"missions":missions, "types" : types})

def modifierM(request, pk):
    mission = Mission.objects.get(titre=pk)
    if mission.type == "quizz":
        mission = QuizzM.objects.get(titre=pk)
        return ModifierMission(request, mission, createQuizzForm, "quizzM.html")
    elif mission.type == "sanction":
        mission = sanctionsM.objects.get(titre=pk)
        return ModifierMission(request, mission, createSanctionForm, "sanctionM.html")
    elif mission.type == "gestion-commerciale":
        mission = GestioncM.objects.get(titre=pk)
        return ModifierMission(request, mission, createGestionComForm, "gestionc_mission.html")
    return redirect("afficher-missions")

def ModifierMission(request, mission, Form, html_fichier):
    form = Form(instance=mission)
    if request.method == "POST":
        form = Form(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            return redirect("afficher-missions")
    context = {'form': form}
    return render(request, html_fichier, context)

def supprimerM(request, pk):
    mission = Mission.objects.get(titre=pk)
    if request.method == "POST":
        mission.delete()
        return redirect("afficher-missions")
    return render(request, "supprimer.html", {"joueur" : mission})
    
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

def creerTypeQuizz(request):
    form = createChoixForm()
    if request.method == "POST":
        form = createChoixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("creer-quizz")
    context = {'form': form}
    return render(request, "creer_type_quizz.html", context)

def sanctionM(request):
    form = createSanctionForm()
    if request.method == "POST":
        form = createSanctionForm(request.POST)
        form.instance.type = "sanction"
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("afficher-missions")
    context = {'form': form}
    return render(request, "sanctionM.html", context)

def parametrageGC(request):
    context = {"types" : ["Fournisseurs", "Clients", "Produits"]}
    return render(request, "parametrage_gc.html", context)

def CreerX(request, Form, fichier_html, page, type):
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(page)
    return render(request, fichier_html, context={"form":form, 'type':type})

def ModifierX(request ,objet, Form , fichier_html, page, type):
    form = Form(instance=objet)
    if request.method == "POST":
        form = Form(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            return redirect(page)
    return render(request, fichier_html, context={"form":form, 'type':type})

def SupprimerX(request ,objet, page):
    if request.method == "POST":
        objet.delete()
        return redirect(page)
    return render(request, "supprimer.html", {"joueur" : objet})


def fournisseurs(request):
    form = createFournisseurForm()
    labels = list(map(lambda x:x.label, form.base_fields.values()))
    fournisseurs = Fournisseur.objects.all()
    return render(request, "fournisseurs.html", context={"labels" : labels, "fournisseurs":fournisseurs})

def CreerFournisseur(request):
    Form = createFournisseurForm
    fichier_html = "creer_objet.html"
    page = "fournisseurs"
    return CreerX(request, Form, fichier_html, page, type="fournisseurs")

def ModifierFournisseur(request,pk):
    Form = createFournisseurForm
    fichier_html = "creer_objet.html"
    page = "fournisseurs"
    objet = Fournisseur.objects.get(Nom=pk)
    return ModifierX(request ,objet, Form , fichier_html, page, type="fournisseurs")

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
    return CreerX(request, Form, fichier_html, page, type="clients")

@permission_required('is_superuser')
def ModifierClient(request,pk):
    Form = createClientForm
    fichier_html = "creer_objet.html"
    page = "clients"
    objet = Client.objects.get(Nom=pk)
    return ModifierX(request ,objet, Form , fichier_html, page, type="clients")

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
    return CreerX(request, Form, fichier_html, page, type="produits")

@permission_required('is_superuser')
def ModifierProduit(request,pk):
    Form = createProduitForm
    fichier_html = "creer_objet.html"
    page = "produits"
    objet = Produit.objects.get(Nom=pk)
    return ModifierX(request ,objet, Form , fichier_html, page, type="produits")

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