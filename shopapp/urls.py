from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, SSListView
from . import views

urlpatterns = [
    path('plist/', ProductListView.as_view(), name='p_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='p_detail'),
    path('new/', ProductCreateView.as_view(), name='p_new'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='p_edit'),
    path('sslist/', SSListView.as_view(), name='ss_list'),
]