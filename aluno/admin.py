from django.contrib import admin
from .models import Cliente, Hospedagem, Quarto, Consumo

admin.site.register(Cliente)
admin.site.register(Hospedagem)
admin.site.register(Quarto)
admin.site.register(Consumo)
