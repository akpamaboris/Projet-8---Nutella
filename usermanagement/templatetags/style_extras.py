from django import template
register = template.Library()


@register.filter(name='addclass')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})
