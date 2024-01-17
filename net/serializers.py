from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from net.models import Organization, Product, Contact



class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели организации
    """
    def validate(self, attrs):
        """
        Проверка нулевого уровня организации
        """

        if attrs.get('organization_type', False) == 'factory' and attrs.get('debt', False):
            raise ValidationError('У завода не может быть какой либо задолженности')
        if attrs.get('organization_type', False) == 'factory' and attrs.get('supplier', False):
            raise ValidationError('У завода не может быть какого либо поставщика')

        return attrs
    class Meta:
        model = Organization
        fields = ('__all__')


class OrganizationUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления организации без возможности обновления задолженности
    """

    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, required=False)

    class Meta:
        model = Organization
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продуктов организации
    """
    class Meta:
        model = Product
        fields = ('__all__')


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор для контактов организации
    """
    class Meta:
        model = Contact
        fields = ('__all__')


class OrganizationDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения информации о организации
    """

    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('__all__')