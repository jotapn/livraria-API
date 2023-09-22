from ..models import Editora
from ..serializer import EditoraSerializer

from rest_framework.viewsets import ModelViewSet


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
