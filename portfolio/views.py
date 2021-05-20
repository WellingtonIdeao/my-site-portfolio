from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'


class AboutView(TemplateView):
    template_name = 'portfolio/about.html'


class ServicesView(TemplateView):
    template_name = 'portfolio/services.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio/portfolio.html'


class ContactView(TemplateView):
    template_name = 'portfolio/contact.html'
