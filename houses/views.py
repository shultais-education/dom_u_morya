from django.shortcuts import render
from houses.models import House


def houses_list(request):
    houses = House.objects.all()
    return render(request, "houses/houses_list.html", {"houses": houses})
