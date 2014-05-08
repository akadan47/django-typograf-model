# coding: utf-8
from django.db import models
from django.utils.encoding import smart_unicode
from .typograf import typo


class TypoModel(models.Model):

    def save(self, *args, **kwargs):
        for field_name in self._typo_fields:
            value = typo(getattr(self, field_name), is_para=False)
            setattr(self, field_name, smart_unicode(value))
        for field_name in self._typo_fields_para:
            value = typo(getattr(self, field_name), is_para=False)
            setattr(self, field_name, smart_unicode(value))
        super(TypoModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True