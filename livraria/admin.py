from django.contrib import admin
from .models import Autor, Editora, Categoria, Compra, Livro, ItensCompra


admin.site.register([Autor, Editora, Categoria, Livro])

class IntensInLine(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines= (IntensInLine,)