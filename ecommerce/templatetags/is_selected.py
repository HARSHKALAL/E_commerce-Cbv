from django import template
register = template.Library()


@register.filter
def selectedcategory(product,category):

    return category in product.category.all()

@register.filter
def selectedsold_by(product,sold_by):
    
    return sold_by in product.sold_by.all() 



