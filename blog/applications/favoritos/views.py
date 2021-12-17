from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse

from django.views.generic import (
    ListView,View,DeleteView
)

from applications.entrada.models import Entry

from .models import Favorites


# a esta vista solo podran acceder los usuario que hayan 
# iniciado sesion
class FavoritesListView(LoginRequiredMixin,ListView):
    template_name = "favoritos/perfil.html"
    context_object_name="entradas_user"
    login_url=reverse_lazy("users_app:user-login")

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)



class AddFavoritosView(LoginRequiredMixin,View):
    login_url=reverse_lazy("users_app:user-login")

    def post(self,request,*args,**kwargs):
        # recuperar el usuario
        usuario=self.request.user
        entrada=Entry.objects.get(id=self.kwargs['pk'])
        login_url=reverse_lazy("users_app:user-login")

        Favorites.objects.create(
            user=usuario,
            entry=entrada,
        )

        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil',
            )
        )


class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url=reverse_lazy("favoritos_app:perfil")



