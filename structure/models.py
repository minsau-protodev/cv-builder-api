import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curriculum(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.TextField()
    owner = models.ForeignKey(User)


class SectionType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=36)
    enabled = models.BooleanField(default=True)


class Section(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=128)
    order = models.IntegerField()
    icon_url = models.URLField()
    section_type = models.ForeignKey(SectionType)
    curriculum = models.ForeignKey(Curriculum)


class ElementType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=36)
    enabled = models.BooleanField(default=True)


class Element(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    date_display_start = models.DateTimeField(blank=True, null=True)
    date_display_end = models.DateTimeField(blank=True, null=True)
    element_type = models.ForeignKey(ElementType)
