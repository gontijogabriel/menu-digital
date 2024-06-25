from django.urls import path
from product.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
]
urlpatterns += router.urls
