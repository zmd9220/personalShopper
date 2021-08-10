from rest_framework import routers
from products.viewsets import ProductViewSet, StockViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'stock', StockViewSet)