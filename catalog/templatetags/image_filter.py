from django import template

register = template.Library()

@register.filter()
def image_product(path):
    if path:
        return f"/media/{path}"
    return "#"