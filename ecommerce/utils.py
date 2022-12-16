from .models import Product
def order_json_to_products(order_data):
    list_data = []
    for i in range(len(order_data)):
        order_detail_data = order_data[i]['order_details']        
        for product in order_detail_data:
            products = Product.objects.get(id=int(product['product_id']))
            product_quantity = product['quantity']
            product_price = product['price']
            list_data.append({"products":products,"qty":product_quantity,"price":product_price})

    return list_data    