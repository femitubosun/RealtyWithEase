from django.db import models
import uuid


# Create your models here.
class BaseModel(models.Model):
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
