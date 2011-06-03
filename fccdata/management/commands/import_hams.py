import datetime
import os

from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from fccdata.load import importer
from fccdata.models import en, am, hd
from fccdata.parser import EN, AM, HD

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--path', default='', dest='path',
            help='The directory where the FCC data is stored.'),
    )
    help = ("Imports data from the FCC amateur license data download.")

    def handle(self, *args, **options):
        if settings.DEBUG:
            print('You really should turn settings.DEBUG off, or else this script will eat a very large amount of your RAM.')
        else:
            input_path = options['path']

            start_time = datetime.datetime.now()

            print('%s existing en objects' % en.objects.all().count())
            importer(os.path.join(input_path, 'EN.dat'), EN, id_column=1, delimiter='|', import_above=None)

            print('%s existing am objects' % am.objects.all().count())
            importer(os.path.join(input_path, 'AM.dat'), AM, id_column=1, delimiter='|', import_above=None)

            print('%s existing hd objects' % hd.objects.all().count())
            importer(os.path.join(input_path, 'HD.dat'), HD, id_column=1, delimiter='|', import_above=None)

            print('Took %s' % (datetime.datetime.now() - start_time))
