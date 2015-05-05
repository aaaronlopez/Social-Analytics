from django import template

register = template.Library()

def key(dictionary, key_name):
	return dictionary[key_name]
key = register.filter('key', key)