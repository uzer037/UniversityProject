from django.shortcuts import render, get_object_or_404

from .models import EventsModel


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def announce(request):
    events_list = EventsModel.objects.all()
    return render(request, 'main/announce.html', {'events_list': events_list})

def announce_detail(request):
    events_list = EventsModel.objects.all()
    return render(request, 'main/announce_detail.html', {'events_list': events_list})