from django.db import models

from datetime import timedelta,datetime
from model_utils.models import TimeStampedModel
# en vez de importar el modelo usuario se importa esto
from django.conf import settings
from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import  RichTextUploadingField
# managers
from .managers import EntryManager

# Create your models here.
class Category(TimeStampedModel):
    """Categorias de una entrada"""

    short_name=models.CharField(
        'Nombre corto',
        max_length=15,
        unique=True
    )

    name=models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    """Etiquetas de un articulo"""

    name=models.CharField(
        "Nombre",
        max_length=30
    )

    class Meta:
        verbose_name="Etiqueta"
        verbose_name_plural="Etiquetas"

    def __str__(self):
        return self.name

class Entry(TimeStampedModel):
    """Modelo para las entradas de los articulos"""

    objects=EntryManager()
    # usuario que escribe el articulo
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    # un articulo puede tener varios tags
    tag=models.ManyToManyField(Tag)
    title=models.CharField(
        'Titulo',
        max_length=200
    )
    resume=models.TextField("Resumen")
    # contenido del articulo
    content=RichTextUploadingField('contenido',default="")
    # ¿el articulo ya puede ser publicado?
    public=models.BooleanField(default=False)
    image=models.ImageField(
        'Imagen',
        upload_to='Entry',
    )
    # ¿se desea que el articulo sea una portada?
    portada=models.BooleanField(default=False)
    # ¿se desea que este articulo figure en la pantalla principal?
    in_home=models.BooleanField(default=False)
    slug=models.SlugField(editable=False)
    class Meta:
        verbose_name='Entrada'
        verbose_name_plural='Entradas'
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        # calculamos el total de segundos de la hora actual
        now=datetime.now()
        total_time=timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )

        # en el mismo segundo no se registraran dos entradas iguales
        seconds=int( total_time.total_seconds() )

        # la url estara conformada por el titulo y el segundo en el que entro
        slug_unique=self.title+str(seconds)

        # asignandole un valor al slug del modelo
        self.slug=slugify(slug_unique)

        # guardando el registro en la base de datos
        super(Entry,self).save(*args,**kwargs)


        




    








    