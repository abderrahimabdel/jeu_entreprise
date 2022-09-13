import random
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import (AbstractBaseUser, UserManager,AbstractUser)
from copy import deepcopy

class Joueur(AbstractUser):
    username = models.CharField(max_length=200, unique=True, null=True)
    password1 = models.CharField(max_length=80, null=True)
    password2 = models.CharField(max_length=80, null=True)
    points = models.IntegerField(null=True)
    points_depart = models.IntegerField(null=True)
    mission_courante = models.ForeignKey('Mission_Joueur', on_delete=models.CASCADE, null=True, default=None)
    missions_passe = models.ManyToManyField('Mission_Joueur', related_name='missions_passe', default="")
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def create_superuser(self, username, password, email=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def clean(self):
        super().clean()
        if self.password1 != self.password2:
            raise ValidationError(
                "password and confirm_password does not match"
            )

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        self.points_depart = deepcopy(self.points)
        return super(Joueur, self).save(*args, **kwargs)

    def reset(self):
        self.mission_courante = None
        self.missions_passe.clear()
        print(self.points, self.points_depart)
        self.points = self.points_depart

    def update_password(self):
        self.set_password(self.password1)
        self.save()

    def update_points(self, reponse):
        resultat = self.mission_courante.resultat(reponse)
        self.points += resultat
        self.save()
        return resultat > 0

    def update_mission(self):
        missions_passe = self.missions_passe.all()
        missions_p = [m.mission for m in missions_passe]

        if (missions_passe.count() % 5==0) and (missions_passe.count() > 0):
            missions = Mission.objects.filter(type="sanction")
        else:
            missions = Mission.objects.all().exclude(pk__in=[p.pk for p in missions_p]).exclude(type="sanction")
            if missions.all().count() == 0:
                return True
        mission = Mission.get_random_mission(missions)
        mission_joueur = Mission_Joueur(mission=mission,temps_restant=mission.temps_en_secondes)
        mission_joueur.set_attributes()
        mission_joueur.save()
        self.mission_courante = mission_joueur
        self.missions_passe.add(mission_joueur)
        self.save()
        return mission

    def __str__(self):
        return self.username    

class Mission_Joueur(models.Model):
    mission = models.ForeignKey('Mission', on_delete=models.CASCADE)
    temps_restant = models.IntegerField(null=True)
    enonce = models.TextField(default="",null=True)
    reponse = models.CharField(max_length=80 ,default="",null=True)

    def set_attributes(self):
        mission = self.mission.get_mission()
        if mission.type == "quizz":
            self.enonce =  mission.question
            self.reponse = mission.get_reponse()
        elif mission.type == "sanction":
            self.enonce =  mission.enonce()
            self.reponse = None
        else:
            mission.generer_mission(self)
        
    def resultat(self, reponse):
        mission = self.mission.get_mission()
        if reponse == self.reponse:
            if mission.type == "sanction":
                return mission.resultat()
            else:
                return mission.points
        else:
            return -mission.points

class Mission(models.Model):
    titre = models.CharField(max_length=200,null=True)
    type = models.CharField(max_length=200,null=True)
    temps_en_secondes = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.titre
    
    def get_mission(self):
        if self.type == "quizz":
            return QuizzM.objects.get(titre = self.titre)
        if self.type == "sanction":
            return sanctionsM.objects.get(titre = self.titre)
        if self.type == "gestion-commerciale":
            return GestioncM.objects.get(titre = self.titre)
    
    def get_random_mission(missions):
        missions = list(missions)
        return random.choice(missions).get_mission()
        


class QuizzM(Mission):
    REPONSES_POSSILES = (
        ('a','A'),
        ('b','B'),
        ('c','C'),
        ('d','D'),
    )

    question =  models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    rep = models.CharField(max_length=6, choices=REPONSES_POSSILES, default='a')
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.titre
    
    def get_reponse(self):
        if self.rep == 'a':
            return self.op1
        if self.rep == 'b':
            return self.op2
        if self.rep == 'c':
            return self.op3
        return self.op4

class sanctionsM(Mission):
    
    intitule = models.CharField(max_length=200,null=True)
    pointsA = models.IntegerField(null=True, default=0)
    pointsR = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.titre
    
    def resultat(self):
        if self.pointsR > 0:
            return self.pointsR*-1
        if self.pointsA > 0:
            return self.pointsA
    
    def gagne(self):
        return self.pointsA > 0

    def enonce(self):
        if self.pointsR > 0:
            return f"L’un de vos clients ne vous a pas payé malgré toutes vos relances vous perdez {self.pointsR} points"
        if self.pointsA > 0:
            return f"Vous avez augmentez vos parts de marché : vous gagnez  : {self.pointsA} Points"

class Fournisseur(models.Model):
    Nom = models.CharField(max_length=200,null=True, unique=True)
    Adresse = models.CharField(max_length=200,null=True)
    cp = models.CharField(max_length=200,null=True)
    ville = models.CharField(max_length=200,null=True)
    remise = models.CharField(max_length=200,null=True)
    divers = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Nom

    def get_values(self):
        return list(vars(self).values())[2:]
    

class Client(models.Model):
    Nom = models.CharField(max_length=200,null=True, unique=True)
    Adresse = models.CharField(max_length=200,null=True)
    cp = models.CharField(max_length=200,null=True)
    ville = models.CharField(max_length=200,null=True)
    remise = models.CharField(max_length=200,null=True)
    divers = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Nom

    def get_values(self):
        return list(vars(self).values())[2:]

class Produit(models.Model):
    Nom = models.CharField(max_length=200,null=True, unique=True)
    prix_achatHT = models.CharField(max_length=200,null=True)
    prix_venteHT = models.CharField(max_length=200,null=True)
    prix_venteTTC = models.CharField(max_length=200,null=True)
    TVA = models.CharField(max_length=200,null=True)
    stock = models.CharField(max_length=200,null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nom
    
    def get_values(self):
        return list(vars(self).values())[2:]
    

class GestioncM(Mission):
    enonce = models.TextField()
    nbre_ref = models.IntegerField(null=True, default=0)
    min_qte = models.IntegerField(null=True, default=0)
    max_qte = models.IntegerField(null=True, default=0)
    points = models.IntegerField(null=True, default=0)

    def get_random_item(Class,n=1):
        objects = list(Class.objects.all())
        return random.sample(objects, k=n)

    def generer_mission(self, mission_joueur):
        nouv_enonce = self.enonce

        if '(client)' in self.enonce:
            nouv_enonce = nouv_enonce.replace("(client)", GestioncM.get_random_item(Client)[0].Nom)
            produits_objects = GestioncM.get_random_item(Produit,self.nbre_ref)
            produits = list(map(lambda x:x.Nom, produits_objects))
        
        if '(fournisseur)' in self.enonce:
            fournisseur = GestioncM.get_random_item(Fournisseur)
            nouv_enonce = nouv_enonce.replace("(fournisseur)", GestioncM.get_random_item(Fournisseur)[0].Nom)
            produits_objects = Produit.objects.filter(fournisseur=fournisseur)
            produits = list(map(lambda x:x.Nom, produits_objects))
        
        produits_text = ""
        reponse = 0
        for i in range(self.nbre_ref):
            qte = random.randint(self.min_qte, self.max_qte)
            reponse += int(produits_objects[i].prix_venteTTC) * qte
            produits_text += f'{produits[i]} pour {qte} \n'
        
        nouv_enonce = nouv_enonce.replace("(produits)", produits_text)
        
        mission_joueur.enonce = nouv_enonce
        mission_joueur.reponse = reponse
        print(reponse)
    
