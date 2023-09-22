from rest_framework.viewsets import ModelViewSet
from ..models import Categoria
from ..serializer import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
