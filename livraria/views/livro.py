from rest_framework.viewsets import ModelViewSet

from ..models import Livro
from ..serializer import LivroSerializer, LivroDatailSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    # serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return LivroDatailSerializer
        if self.action == "retrieve":
            return LivroDatailSerializer
        else:
            return LivroSerializer
