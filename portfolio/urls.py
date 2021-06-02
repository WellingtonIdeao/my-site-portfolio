from django.urls import path
from .views import IndexView, AboutView, ServicesView, PortfolioView, ContactView

app_name = 'portfolio'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='service'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('contact/', ContactView.as_view(), name='contact'),
]

