from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from products.models import Nomenclature

class NomenclatureAdmin(MPTTModelAdmin):
    list_display = ('name',)

admin.site.register(Nomenclature, NomenclatureAdmin)
