from django import template

register = template.Library()


@register.inclusion_tag('side.html')
def side(side):
    return{"side": side}


@register.inclusion_tag('priority.html')
def priority(priority):
    return {"priority": priority}


@register.inclusion_tag('food_type.html')
def food_type(side):
    pass


@register.inclusion_tag('confirm.html')
def confirm(confirm):
    return {"confirm": confirm}


@register.inclusion_tag('invitation.html')
def invitation(side):
    pass
