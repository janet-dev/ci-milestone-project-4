from django import template


""" custom template filter for calculating subtotal column
on the shopping bag page"""
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
