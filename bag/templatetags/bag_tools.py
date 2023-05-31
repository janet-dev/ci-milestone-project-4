from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ custom template filter for calculating subtotal column
    on the shopping bag page"""

    return price * quantity
