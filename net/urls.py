
from django.urls import path
from rest_framework.routers import DefaultRouter

from net.apps import NetConfig
from net.views import OrganizationCreateView, OrganizationDeleteView, OrganizationListView, OrganizationUpdateView, \
    OrganizationDetailView, ProductViewSet, ContactViewSet

app_name = NetConfig.name
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('organization/create/', OrganizationCreateView.as_view(), name='organization_create'),
    path('organization/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='organization_destroy'),
    path('organization/list/', OrganizationListView.as_view(), name='organization_list'),
    path('organization/update/<int:pk>/', OrganizationUpdateView.as_view(), name='organization_update'),
    path('organization/detail/<int:pk>/', OrganizationDetailView.as_view(), name='organization_retrieve'),
] + router.urls
