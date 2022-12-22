from .models import Product
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
import json

def order_json_to_products(order_data):
    list_data = []
    for i in range(len(order_data)):
        order_detail_data = order_data[i]['order_details']
        for product in order_detail_data:
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

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

def add_product_data(data,img,klass):
  data = data.dict()  
  data.pop("csrfmiddlewaretoken")
  a = klass.objects.create(**{"name":data.pop("name"),"text":data.pop("text"),"description":data.pop("description"),"image":img['image'],"price":data.pop("price"),"discount_percentage":data.pop("discount_percentage"),"stock_quantity":data.pop("stock_quantity")})
  a.category.set(data.pop("category"))
  a.save()
  a.sold_by.set(data.pop("sold_by"))
  a.save()  
  return a

def updateproduct(data,img,klass,id):
  data=data.dict()
  data.pop("csrfmiddlewaretoken")
  
  cat_updated = json.loads(data.pop("category"))
  sold_by_updated = json.loads(data.pop("sold_by"))

  b=klass.objects.filter(id=id)
  b.update(**{"name":data.pop("name"),"text":data.pop("text"),"description":data.pop("description"),"price":data.pop("price"),"discount_percentage":data.pop("discount_percentage"),"stock_quantity":data.pop("stock_quantity")})
  b.image=img['image']
  b.category.set(cat_updated)
  b.sold_by.set(sold_by_updated)
  b.save()  
  return b