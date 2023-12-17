from django import template


register = template.Library()

@register.simple_tag() #превратили функцию в тег
def Menu_fields(): #создали пользовательский тег
    menu = [
        {'title': 'Главная', 'url_name': 'main'},
        {'title': 'О нас', 'url_name': 'main'},  # Изменить путь на перемотку страницы

    ]
    return menu
