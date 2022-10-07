from django.contrib import admin

from .models import Choix, VEntrepriseM, QuizzM
from .forms import Joueur
# Register your models here.
admin.site.register(Joueur)
admin.site.register(QuizzM)
admin.site.register(VEntrepriseM)
admin.site.register(Choix)