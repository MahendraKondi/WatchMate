from django.shortcuts import render
from django.http import HttpResponse


def watch(request):
    return HttpResponse("Hello ")