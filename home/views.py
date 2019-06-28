from django.shortcuts import render
from django.views.generic import TemplateView

from category.models import Category
from events.models import Event

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def home_page_view(request):
    services = Category.objects.all()

    featured_event = Event.objects.get(featured='featured')

    categories = Category.objects.all()[:3]

    context = {
        'services': services,
        'categories': categories,
        'featured_event': featured_event,
    }

    return render(request, 'index.html', context)

def service_page_view(request):
    services = Category.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'service.html', context)
