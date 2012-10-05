from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from gifs.models import Photo
from gifs.tasks import download_most_recent_gifs

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
        make_option('-t',action='store',type='int',dest='before'),
    )

	def handle(self, *args, **options):
		before = options.get('before',None)
		if before:
			download_most_recent_gifs(before=before)
		else:
			earliest_photo = Photo.objects.filter(timestamp__isnull=False).order_by('timestamp')[0]
			if earliest_photo.timestamp:
				download_most_recent_gifs(before=earliest_photo.timestamp)
			else:
				print "Earliest photo doesn't have timestamp. Run with -t option"

