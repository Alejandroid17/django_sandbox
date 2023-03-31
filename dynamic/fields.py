from django.db import models
from django.db.models.fields.files import FieldFile

# DEVREL
# 

class FieldFileDynamic(FieldFile):
    pass
    
    # def _set_file(self, file):
        # pass

    # def _get_file(self):
        # return self.instance.model_b.binary.open()

class DynamicField(models.FileField):

    attr_class = FieldFileDynamic


