from django.db import models

# Create your models here.

"""
class Sample(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=True, default='')
    img_name = models.CharField(max_length=100, blank=True, default='')
    info = models.TextField()
    owner = models.ForeignKey('auth.user',
                              related_name='sample',
                              on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.name
"""


class Page(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    pageid = models.CharField(max_length=50, blank=False, default='index')
    header = models.CharField(max_length=150, blank=True, default='')
    message = models.TextField(blank=True)
    urltext = models.CharField(max_length=100, blank=True, default='')
    project = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.user',
                              related_name='page',
                              on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('pageid',)

    def __unicode__(self):
        return self.pageid

class Expo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=150, blank=False, default='Mi Expo')
    desde = models.DateTimeField(blank=False, auto_now=True)
    hasta = models.DateTimeField(blank=True)
    lugar = models.CharField(max_length=150, blank=True)
    descripcion = models.TextField(blank=True)
    creditos = models.TextField(blank=True)
    texto_curatorial = models.CharField(max_length=100, blank=True, default='')
    rating = models.FloatField(blank=False, default=2.5)
    likes = models.IntegerField(blank=False, default=0)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.titulo


class Obra(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    expo = models.ForeignKey(Expo, on_delete=models.CASCADE)
    creador = models.CharField(max_length=150, blank=False, default='')
    titulo = models.CharField(max_length=150, blank=False, default='')
    fecha = models.DateField(blank=False, auto_now=True)
    medio = models.CharField(max_length=150, blank=True)
    descripcion = models.TextField(blank=True)
    rating = models.FloatField(blank=False, default=2.5)
    likes = models.IntegerField(blank=False)
    lecturas = models.IntegerField(blank=True, default=0)
    active = models.BooleanField(blank=False, default=False)

    class Meta:
        ordering = ('creador',)

    def __unicode__(self):
        return self.titulo
