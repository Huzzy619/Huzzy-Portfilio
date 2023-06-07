from django import template

register = template.Library()

@register.filter(name="zip")
def zip_lists(first_list, second_list):
  return zip(first_list, second_list)

