import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from applications.entrada.models import Entry
from applications.home.models import Home
from .forms import SuscribersForm,ContactForm
from .models import Suscribers
from django.views.generic import (
    TemplateView,CreateView,DetailView
)


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        
        # objeto de tipo formulario
        context['form']=SuscribersForm

        # datos de home
        context['home']=Home.objects.latest('created')
        # contexto de portada
        context["portada"]=Entry.objects.entrada_en_portada()
        # contectos para los articulos en home
        context["entradas_home"]=Entry.objects.entradas_en_home()
        # entradas recientes
        context["entradas_recientes"]=Entry.objects.entradas_recientes()
        
        return context
    

class SuscribersCreateView(CreateView):
    form_class=SuscribersForm # indispensable indicar
    success_url='.' # una vez contestado el formulario se dirigira 
                    # a la misma pagina en donde se encuentra

    # No es obligatorio especificar un template
    # template_name = ...


class ContactCreateView(CreateView):
    form_class=ContactForm # indispensable indicar
    success_url='.' # una vez contestado el formulario 
                    # se dirigira  a la misma pagina en 
                    # donde se encuentra
    # No es obligatorio especificar un template
    #template_name = "TEMPLATE_NAME"





    






    


