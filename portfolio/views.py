from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from .models import Profile, Service, Project
from .forms import ContactForm
# Create your views here.


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, pk=1)
        return context


class ServicesView(ListView):
    model = Service
    template_name = 'portfolio/services.html'


class PortfolioView(ListView):
    model = Project
    template_name = 'portfolio/portfolio.html'

    def get_queryset(self):
        """Return the last six projects."""
        return Project.objects.order_by('-date')[:6]


class ContactView(CreateView):
    template_name = 'portfolio/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'