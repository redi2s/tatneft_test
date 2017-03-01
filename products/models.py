from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Nomenclature(MPTTModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=u'Номенклатура')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def __str__(self):
        return str(self.name)

    class MPTTMeta:
        order_insertion_by = ['name']

    # class Meta:
    #     verbose_name_plural = u'Номенклатура'
    #     verbose_name = u'Номенклатура'
