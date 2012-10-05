import jsonfield
from batch_select.models import BatchManager
from django.db import models


class Tag(models.Model):
    """
    The model representing a tag on Tumblr
    """
    objects = BatchManager()
    name = models.CharField(max_length=100, unique=True)


class Photo(models.Model):
    """
    The model for a Tumblr Photo post containing one image
    """
    objects = BatchManager()
    post_url = models.URLField(
        verify_exists=False,
        max_length=255,
        unique=True,
        help_text='The full, canonical, non-shortened URL for the image.'
    )
    note_count = models.IntegerField(blank=True, null=True)
    url = models.URLField(verify_exists=False, max_length=255)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    tags_json = jsonfield.JSONField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='photos')
    date_posted = models.DateTimeField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    date_downloaded = models.DateTimeField(auto_now_add=True)
