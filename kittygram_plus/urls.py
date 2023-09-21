from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


router = DefaultRouter()
router.register(r'mycats', LightCatViewSet)
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]