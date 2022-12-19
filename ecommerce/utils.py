from .models import Product
from django.core.serializers.json import DjangoJSONEncoder
import json


def order_json_to_products(order_data):
    list_data = []
    for i in range(len(order_data)):
        order_detail_data = order_data[i]['order_details']
        for product in order_detail_data:
            print(product)
            products = Product.objects.get(id=product['product_id'])
            print(products)
            product_quantity = product['quantity']
            product_price = products.price
            list_data.append({"products":products,"qty":product_quantity,"price":product_price})
    return list_data    

def total_stock_quantity(order_quantity):
    for i in order_quantity:
        total_stock_quantity=i.get('product__stock_quantity')
        quantity=i.get('quantity')
        product_id=i.get('product_id')
        pro=Product.objects.get(id=product_id)
        if pro.stock_quantity:
            pro.stock_quantity=total_stock_quantity-quantity
            print(pro.stock_quantity)
            pro.save()    





