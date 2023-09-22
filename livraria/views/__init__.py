from .categoriaClass import CategoriaView
from .categoriaAPIVIEW import CategoriaDetail, CategoriasList
from .categoriaGenericView import CategoriaListGeneric, CategoriaDetailGeneric

from .autor import AutorViewSet
from .categoria import CategoriaViewSet
from .editora import EditoraViewSet
from .livro import LivroViewSet
from .compra import CompraViewSet

a = [CompraViewSet,
     CategoriaView, CategoriaDetail, CategoriasList,
     CategoriaListGeneric, CategoriaDetailGeneric,
     AutorViewSet, CategoriaViewSet, EditoraViewSet,
     LivroViewSet]
