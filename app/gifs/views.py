from django.shortcuts import render
from endless_pagination.decorators import page_template
from gifs.models import Tag, Photo

@page_template('photo_feed.html')
def index(request, template='base.html', extra_context=None):
    photos = Photo.objects.all().batch_select('tags').order_by('-date_downloaded')
    context = {}
    context['photos'] = photos
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)
