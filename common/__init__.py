import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class OGBaseModel(models.Model):
    id = models.CharField(max_length=50,
                          primary_key=True,
                          verbose_name='ID')

    class Meta:
        abstract = True


@receiver(pre_save)
def new_uuid_value(sender, **kwargs):
    if issubclass(sender, OGBaseModel):
        instance = kwargs.get('instance')
        if instance.id is None:
            instance.id = uuid.uuid4().hex
