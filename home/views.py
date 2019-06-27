from django.shortcuts import render
from django.views.generic import TemplateView

from category.models import Category

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def home_page_view(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'index.html', context)
