from django.contrib import admin
from .models import  Expo, Obra


class ObraInline(admin.StackedInline):
    model = Obra

class ExpoAdmin(admin.ModelAdmin):
    inlines = [ ObraInline ]



admin.site.register(Expo, ExpoAdmin)
