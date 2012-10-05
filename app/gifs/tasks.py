from celery.task import task, periodic_task
from celery.task import subtask
from celery.schedules import crontab
from django.utils import simplejson as json
from gifs.tumblr import tumblr_tag_request, save_post

import logging
logger = logging.getLogger(__name__)


@periodic_task(run_every=crontab())
def download_most_recent_gifs(before=None):
    """
    Downloads the most recent posts tagged with 'gif' and 'lol' and saves them to the database
    add before to get more
    &before=1333132865
    """
    tags = ['gif', 'LOL']
    for tag in tags:
        logger.info('Downloading for tag: %s' % (tag))
        tumblr_response = tumblr_tag_request(tag, before=before)
        data = json.loads(tumblr_response)
        posts = data['response']
        for post in posts:
            item, status = save_post(post)
            logger.info("%s was %s" % (item, status))
