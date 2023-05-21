from django.shortcuts import render


def index(request):
    """ A view to return to the index page """

    return render(request, 'home/index.html')
