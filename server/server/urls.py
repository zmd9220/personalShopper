from django.contrib import admin
from django.urls import path, include
from .routers import router
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')), # 상품관련 url
    path('api/', include(router.urls)),
    path('article', TemplateView.as_view(template_name='index.html')),
    path('accounts/', include('accounts.urls')),
]

