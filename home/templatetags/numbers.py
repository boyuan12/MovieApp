from django import template

register = template.Library()

def format_number(value):
    return f"{value:,}"

register.filter('format_number', format_number)