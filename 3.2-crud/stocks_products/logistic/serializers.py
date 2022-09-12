from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['title', 'description', 'stocks']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']

    def create(self, validated_data):
        return super().create(validated_data)


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['address', 'positions']


    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            StockProduct.objects.create(stock=stock,
                                        product=position['product'],
                                        quantity=position['quantity'],
                                        price=position['price']
                                        )

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            StockProduct.objects.update_or_create(defaults=position,
                                                  product=position['product'],
                                                  stock_id=stock.pk,
                                                  )

        return stock
