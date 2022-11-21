from django import template
register = template.Library()


@register.filter
def showdiscountprice(product):
    total = product.price-((product.price*product.discount_percentage)/100)
    return total



