from django.shortcuts import render


def drycleaning(request):
    context = {}
    return render(request, "drycleaning.html", context)
