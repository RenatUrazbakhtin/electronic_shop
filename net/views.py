from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from net.models import Organization, Product, Contact
from net.serializers import OrganizationUpdateSerializer, OrganizationSerializer, OrganizationDetailSerializer, \
    ProductSerializer, ContactSerializer
from users.permissions import IsActive


# Create your views here.
class OrganizationCreateView(generics.CreateAPIView):
    """
    Создание организации
    """

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsActive]

class OrganizationListView(generics.ListAPIView):
    """
    Список организаций
    """

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contacts__country']
    permission_classes = [IsActive]

class OrganizationDetailView(generics.RetrieveAPIView):
    """
    Получение организации
    """

    serializer_class = OrganizationDetailSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsActive]

class OrganizationUpdateView(generics.UpdateAPIView):
    """
    Обновление организации
    """

    serializer_class = OrganizationUpdateSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsActive]

class OrganizationDeleteView(generics.DestroyAPIView):
    """
    Удаление организации
    """

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsActive]

class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD для продуктов организации
    """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ContactViewSet(viewsets.ModelViewSet):
    """
    CRUD для контактов организации
    """

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()