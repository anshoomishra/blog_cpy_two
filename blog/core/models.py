from django.db import models
from django.db.models.fields.json import JSONField
from django.contrib.postgres.indexes import GinIndex
# Create your models here.

class ModelWithMetaData(models.Model):
    private_meta_data = JSONField( null=True,blank = True)
    meta_data = JSONField(null=True,blank = True)
    
    class Meta:
        indexes = [
            GinIndex(fields=["private_metadata"], name="%(class)s_p_meta_idx"),
            GinIndex(fields=["metadata"], name="%(class)s_meta_idx"),
        ]
        abstract = True
    
    def get_private_meta_data(self,key,default=None):
        self.private_meta_data(key,default)
    def clear_private_meta_data(self):
        
        self.private_meta_data = {}
    


    
