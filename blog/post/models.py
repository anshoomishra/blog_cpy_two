from django.db import models
import uuid
from core.models import ModelWithMetaData
from django.contrib.auth.models import User
# Create your models here.

class PostQueryset(models.QuerySet):
    pass

class PostManager(models.Manager):
    pass

class Post(ModelWithMetaData):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    title = models.CharField(max_length=20,unique=True)
    cerated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    is_published = models.BooleanField(default=False)
    publication_date = models.DateTimeField()
    image = models.ImageField(uploadto = "",null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "created")
    slug = models.SlugField()
    published_by = models.ForeignKey(User,on_delete = models.CASCADE,related_name = "publisher")
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-publication_date']

