from typing import KeysView
from django.db import models

class EntryManager(models.Manager):
    """procedimiento para entrada"""

    def entrada_en_portada(self):
        
        # de las portadas publicas 
        # elegira la mas reciente
        return self.filter(
            public=True,
            portada=True
        ).order_by('-created',).first()

    def entradas_en_home(self):
        # devuelve las ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True
        ).order_by('-created')[:4]

    def entradas_recientes(self):
        # devuelve las ultimas 6 entradas recientes
        return self.filter(
            public=True,
            in_home=True
        ).order_by('-created')[:6]

    def buscar_entrada(self,kword,categoria):
        '''
        Buscar entradas por palabra clave o cateogoria
        '''

        if len(categoria)>0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword
            ).order_by('-created')
            
        else:
            return self.filter(
                title__icontains=kword
            ).order_by('-created')



        