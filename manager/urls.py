from django.urls import path, include
from .views import home, project, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('project', project, name='project'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]
