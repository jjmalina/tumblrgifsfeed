import requests
import settings
from datetime import datetime
from pytz import timezone

from gifs.models import Tag, Photo
from gifs.utils import normalize_query

eastern = timezone('US/Eastern')
tumblr_key = settings.TUMBLR_KEY


def tumblr_tag_querystring(query, before=None):
    """
    **Internal function**
    Constructs a URL for a call to Tumblr's API
    """
    query = normalize_query(query)
    endpoint = 'http://api.tumblr.com/v2/tagged?'
    api_call = 'tag=%s' % (query)
    if before:
        api_call += '&before=%i' % (before)
    api_call += "&api_key=%s" % (tumblr_key)
    return endpoint + api_call


def tumblr_tag_request(tag_query, before=None):
    """
    Makes an API request to Tumblr to get response back from a tag request
    If response succeeds, returns the response as json string
    If response fails, returns an dict with error key
    """
    querystring = tumblr_tag_querystring(tag_query, before=before)
    response = requests.get(querystring)
    if response.status_code == 200:
        return response.text
    else:
        return {'error': "Couldn\'t retrieve response from tumbr"}


def bulk_get_or_create_tags(tag_list):
    """
    **Internal function**
    Gets or creates a list of tags, returns them
    """
    tags = []
    for tag_item in tag_list:
        tag, created = Tag.objects.get_or_create(name=tag_item)
        tags.append(tag)
    return tags


def save_post(post_dict):
    """
    Saves a single post and its tags to the database
    Returns the URL of the saved post 
    and whether it was saved, a duplicate, or was not a photo for logging purposes
    """
    if 'type' in post_dict and post_dict['type'] == 'photo':
        post_url = post_dict['post_url']
        photo, created = Photo.objects.get_or_create(post_url=post_url)
        # only save data if the photo does not exist
        photos = post_dict['photos']
        if created and photos:
            photo.note_count = post_dict['note_count']
            photo.tags_json = post_dict['tags']
            photo.tags = bulk_get_or_create_tags(post_dict['tags'])
            photo.timestamp = post_dict['timestamp']
            photo.date_posted = eastern.localize(datetime.fromtimestamp(post_dict['timestamp']))
            photo_dict = photos[0]
            original_dict = photo_dict['original_size']
            photo.width = original_dict['width']
            photo.height = original_dict['height']
            photo.url = original_dict['url']
            photo.save()
            return (photo.post_url, 'saved')
        else:
            return (post_url, 'duplicate')
    else:
        return ('None', 'not a photo')
