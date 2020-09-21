from django import template


register = template.Library()

@register.filter(name='productsubtotal')
def productsubtotal(price, amount):
    return price * amount