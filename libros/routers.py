from rest_framework.routers import DefaultRouter

from .views import LibroCatalogoViewSet, LibroViewSet, ResenaViewSet

router = DefaultRouter()
router.register("libros", LibroViewSet, basename="libro")
router.register("resenas", ResenaViewSet, basename="resena")
router.register("catalogo", LibroCatalogoViewSet, basename="catalogo-libro")
