from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeView, contacts, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path("<int:pk>/product_detail/", ProductListView.as_view(), name="product_detail"),
    path("create/product_detail/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/product_detail/update", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/product_detail/delete", ProductDeleteView.as_view(), name="product_delete"),
]
