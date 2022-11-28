from django.urls import path
from . import views

# urls
app_name = 'clientViewApp'
urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about-pfl', views.aboutPage, name='aboutPage'),
    path('contact', views.contactPage, name='contactPage'),
    path('services', views.servicePage, name='servicePage'),
    path('portfolio', views.portfolioPage, name='portfolioPage'),
]