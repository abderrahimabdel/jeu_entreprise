from django.contrib import admin

from .models import sanctionsM, QuizzM
from .forms import Joueur
# Register your models here.
admin.site.register(Joueur)
admin.site.register(QuizzM)
admin.site.register(sanctionsM)