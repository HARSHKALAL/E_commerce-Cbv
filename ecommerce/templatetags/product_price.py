from django import template
register = template.Library()


@register.filter
def product_price(cart): 
    total =cart.product.price * cart.quantity   
    return total







