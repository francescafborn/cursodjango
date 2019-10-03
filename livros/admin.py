from django.contrib import admin
from livros.models import Autor, Livro

class AdminAutor(admin.ModelAdmin):
    list_display = ( 'nome',)
    list_filter = ('nome',)
    search_fields = ['nome']

class AdminLivro(admin.ModelAdmin):
    list_display = ( 'titulo',)
    list_filter = ( 'autor','categoria',)
    search_fields = ['titulo', 'autor__nome',]


admin.site.register(Autor, AdminAutor)
admin.site.register(Livro, AdminLivro)
admin.site.site_header = 'Cogumelos em letras'
admin.site.index_title = 'Features'
admin.site.site_title = 'COGUMELOS'
