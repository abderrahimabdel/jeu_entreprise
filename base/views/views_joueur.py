

from django.contrib.auth.decorators import permission_required, login_required

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect

from base.models import Joueur

from base.forms import  createPlayerForm

# Create your views here.


@permission_required('is_superuser')
def dashboard(request):
    return render(request, "dashboard.html")

@permission_required('is_superuser')
def creerJoueur(request):
    form = createPlayerForm()
    if request.method == 'POST':
        form = createPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.update_password()
            return redirect("joueurs")
    context = {'form': form, "creer":True}
    return render(request, "creerJoueur.html", context)

@permission_required('is_superuser')
def modifierJoueur(request,pk):
    joueur = Joueur.objects.get(username=pk)
    form = createPlayerForm(instance=joueur)
    if request.method == 'POST':
        form = createPlayerForm(request.POST, instance=joueur)
        if form.is_valid():
            form.save()
            joueur.update_password()
            return redirect("joueurs")
    context = {'form': form, "creer":False}
    return render(request, "creerJoueur.html", context)

@permission_required('is_superuser')
def supprimerJoueur(request,pk):
    joueur = Joueur.objects.get(username=pk)
    if request.method == "POST":
        joueur.delete()
        return redirect("joueurs")
    return render(request, "supprimer.html", {"joueur" : joueur})

@permission_required('is_superuser')
def joueurs(request):
    context = {'form': Joueur.objects.all()}
    return render(request, "gestion_joueurs.html", context)

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username").lower().strip()
        password = request.POST.get("password")
        try:
            joueur = Joueur.objects.get(username=username)
            if joueur.password1==password:
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("jouer")
        except:
            pass
    return render(request, "login.html")

@login_required(login_url='/login/')
def jouer(request):
    joueur = request.user
    commencer = True
    if joueur.missions_passe:
        commencer = False
    return render(request, "jouer.html", context={"joueur":joueur, "commencer" : commencer})

@login_required(login_url='/login/')
def Logout(request):
    logout(request)
    return redirect('login')