from core.abstract.serializers import AbstractSerializer
from core.product.models import Product


class ProductSerializer(AbstractSerializer):
    def update(self, instance, validated_data):
        
        instance = super().update(instance, validated_data)
        return instance

    class Meta:
        model = Product
        fields = '__all__'
