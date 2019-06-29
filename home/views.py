from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from category.models import Category
from events.models import Event
from package.models import Package
from team.models import Team
from contact.forms import ContactForm

# Create your views here.
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

def category_detail_view(request, id):
    services = Category.objects.all()

    events = Event.objects.filter(category_id=id).order_by('-id')

    category = Category.objects.get(id=id)
    
    packages = Package.objects.filter(category_id=id)

    context = {
        'services': services,
        'category': category,
        'packages': packages,
        'events': events,
    }
    return render(request, 'package.html', context)

def gallery_view(request):
    services = Category.objects.all()

    events = Event.objects.all().order_by('-id')

    context = {
        'events': events,
        'services': services,
    }

    return render(request, 'gallery.html', context)

def event_view(request, id):
    services = Category.objects.all()

    event = Event.objects.get(id=id)

    context = {
        'event': event,
        'services': services,
    }

    return render(request, 'event.html', context)

def team_view(request):
    services = Category.objects.all()

    team = Team.objects.all()

    context = {
        'services': services,
        'team': team,
    }

    return render(request, 'team.html', context)

def contact_view(request):
    services = Category.objects.all()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['your_email']
            message = form.cleaned_data['your_message']
            try:
                send_mail(subject, message, from_email, ['omoki@example.com'])
            except BadHeaderError:
                return HttpResponse('Bad Header')
            return redirect('success')

    context = {
        'services': services,
        'form': form,
    }

    return render(request, 'contact.html', context)


def contact_success_view(request):
    services = Category.objects.all()

    events = Event.objects.all().order_by('-id')[:3]

    context = {
        'services': services,
        'events': events,
    }
    return render(request, 'success.html', context)





