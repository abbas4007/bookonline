# your_app/templatetags/wishlist_tags.py
from django import template

register = template.Library()

@register.filter
def is_in_wishlist(product, request):
    """
    استفاده: {% if product|is_in_wishlist:request %}
    """
    if not request.user.is_authenticated:
        return False
    # فرض: هر کاربر یک Wishlist داره
    return request.user.wishlist.products.filter(id=product.id).exists()