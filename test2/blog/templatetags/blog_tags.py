from django import template
from ..models import  Post,Category

register = template.Library()
@register.simple_tag()
def get_recent_posts():
    return Post.objects.all().order_by('-created_time')

@register.simple_tag()
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag()
def category():
    return Category.objects.all()