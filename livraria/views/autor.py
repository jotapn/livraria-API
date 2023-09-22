from rest_framework.viewsets import ModelViewSet

from ..models import Autor
from ..serializer import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
