from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'portfolio'
urlpatterns = [
    path('', TemplateView.as_view(template_name='portfolio/index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='portfolio/about.html'), name='about'),
    path('services/', TemplateView.as_view(template_name='portfolio/services.html'), name='services'),
    path('portfolio/', TemplateView.as_view(template_name='portfolio/portfolio.html'), name='portfolio'),
    path('contact/', TemplateView.as_view(template_name='portfolio/contact.html'), name='contact'),
]

