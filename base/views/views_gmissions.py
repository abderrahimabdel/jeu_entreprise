
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from base.models import Client, Fournisseur, GestioncM, Joueur, Produit, QuizzM, sanctionsM, Mission

from base.forms import createClientForm, createFournisseurForm, createGestionComForm, createProduitForm, createQuizzForm, createPlayerForm, createSanctionForm
import random

from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.cache import cache_control


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required(login_url='/login/')
def generer(request):
    joueur = request.user
    mission_c = joueur.mission_courante
    if mission_c:
        temps_restant = mission_c.temps_restant
        n_mission = mission_c.mission
    else:
        temps_restant = 0
    if request.method == "POST":
        mission = n_mission.get_mission()
        answer = request.POST.get("reponse")
        points = mission_c.resultat(answer)
        gagne = joueur.update_points(answer)
        mission = joueur.update_mission()
        if mission == True:
            joueur.reset()
            return render(request, "resultat_final.html", context={"joueur":joueur, "points":joueur.points})
        request.session["gagne"] = gagne
        request.session["points"] = abs(points)
        return redirect('resultat')

    if temps_restant > 0:
        mission = mission_c.mission.get_mission()
    else:
        mission = joueur.update_mission()
        if mission == True:
            return render(request, "resultat_final.html", context={"joueur":joueur, "points":joueur.points})
        mission_c = joueur.mission_courante
    if mission.type == "quizz":
        return render(request, "quizzj.html", context={'mission':mission, "joueur":joueur, "temps" : temps_restant})
    elif mission.type == "sanction":
        gagne_points = mission.get_mission().gagne()

        return render(request, "sanctionj.html", context={'enonce':mission_c.enonce, "joueur":joueur, "temps" : temps_restant, "gagne" : gagne_points})
    else :
        return render(request, "gestioncj.html", context={'mission':mission_c, "joueur":joueur, "temps" : temps_restant})

@login_required(login_url='/login/')
def resultat(request):
    if request.META.get('HTTP_REFERER') == "http://127.0.0.1:8000/jouer/1":
        gagne = request.session["gagne"]
        points = request.session["points"]
        return render(request, "resultat.html", context= {"gagne":gagne, "points": points, "joueur" : request.user})
    else:
        return HttpResponseRedirect(reverse('generer'))

@login_required(login_url='/login/')
def update_temps(request):
    data = request.POST
    temps = data['temps']
    joueur = request.user
    mission_c = joueur.mission_courante
    mission_c.temps_restant = temps
    mission_c.save()
    return JsonResponse({})

@login_required(login_url='/login/')
def listing(request, pk):
    if pk == "clients":
        form = createClientForm()
        objects = Client.objects.all()
    elif pk == "produits":
        form = createProduitForm()
        objects = Produit.objects.all()
    elif pk == "fournisseurs":
        form = createFournisseurForm()
        objects = Fournisseur.objects.all()
    labels = list(map(lambda x:x.label, form.base_fields.values()))
    return render(request, "listing.html", context={"labels" : labels, "objects" : objects})