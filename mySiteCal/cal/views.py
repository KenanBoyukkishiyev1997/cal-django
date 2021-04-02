from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Service,Gallery,Faq,Company


# Create your views here.
class ServiceCal(ListView):
    model = Service
    template_name= 'cal/index.html' 
    context_object_name='service'



class GalleryCal(ListView):
    model = Gallery
    template_name= 'cal/gallery.html' 
    context_object_name='gallery'




class FaqCal(ListView):
    model = Faq
    template_name= 'cal/index.html' 
    context_object_name='faq'



class CompanyCal(ListView):
    model=Company
    template_name= 'cal/index.html' 
    context_object_name='about_item'


    




