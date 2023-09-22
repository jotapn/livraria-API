from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    SerializerMethodField,
)
from rest_framework import serializers
from .models import Categoria, Editora, Autor, Livro, Compra, ItensCompra


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"


class EditoraNestedSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = [
            "nome",
        ]


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroDatailSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    editora = EditoraNestedSerializer()
    autores = SerializerMethodField()

    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

    def get_autores(self, instance):
        nome_autores = []
        autores = instance.autores.get_queryset()
        for autor in autores:
            nome_autores.append(autor.nome)
        return nome_autores


class ItensCompraSerializer(ModelSerializer):
    """Listar itens de compra"""

    total = SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade", "total")
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco


class ComprasSerializer(ModelSerializer):
    """Lista compras"""

    usuario = CharField(source="usuario.username")
    status = SerializerMethodField()
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("id", "status", "usuario", "itens", "total")

    def get_status(self, instance):
        return instance.get_status_display()


class CriarEditarItensCompraSerializar(ModelSerializer):
    """Criar novos itens de compra"""

    class Meta:
        model = ItensCompra
        fields = ("id", "livro", "quantidade")


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializar(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
            instance.save()
        return instance
