from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from ..models import Categoria
from ..serializer import CategoriaSerializer


class CategoriaListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
