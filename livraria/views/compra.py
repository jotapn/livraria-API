from livraria.serializer import CriarEditarCompraSerializer
from ..models import Compra
from ..serializer import ComprasSerializer

from rest_framework.viewsets import ModelViewSet


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ComprasSerializer
        return CriarEditarCompraSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name='Administradores'):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
