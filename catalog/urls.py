from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path("product_detail/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product_detail/create/", ProductCreateView.as_view(), name="product_create"),
    path("product_detail/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path("product_detail/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete")
]
