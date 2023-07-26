from django.contrib import admin 
from .models import  Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email','mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Contato, ContatoAdmin)