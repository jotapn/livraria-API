from livraria.serializer import CriarEditarCompraSerializer
from ..models import Compra
from ..serializer import ComprasSerializer

from rest_framework.viewsets import ModelViewSet


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    # serializer_class = ComprasSerializer

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ComprasSerializer
        return CriarEditarCompraSerializer
