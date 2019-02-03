from django.shortcuts import render

from recursive.models import Recursive1
from django.http import HttpResponse


def draw(string, recursive_items, i):
    i += 1
    for recursive_item in recursive_items:
        string += "#"*i + " " + recursive_item.label + "<br/>"
        string = draw(string, recursive_item.recursive1_set.all(), i)
    return string


def recursive_view(request):
    recursives = Recursive1.objects.all()
    string = ''
    string += '<div>'
    string += draw(string, recursives, 0)
    string += '</div>'
    return HttpResponse(string)
