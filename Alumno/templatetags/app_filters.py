from django import template
register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    return (value-1)*arg+10

@register.filter(name='ordenar')
def ordenar(value, arg):
	return ((value-1)//arg)*100