#!/home/bin/python
# -*- coding: utf-8
import os, sys
from django.db import transaction
from django.conf import settings
from fccdata.parser import EN, AM, HD

FCC_PATH = '/Users/afast/Downloads/l_amat/'

# ******* generic
def import_object(parsing_class, line, id_column):
    parsed = parsing_class(line)
    obj = parsed.get_object()
    try:
        obj.save()
        return obj
    except:
        print 'ID: %s' % line.split('|')[id_column]
        print sys.exc_info()[0]
        print sys.exc_info()[1]
        exit()

def importer(file_path, parsing_class, id_column=0, delimiter=',', import_above=None):
    data_file = open(file_path)

    import datetime
    start = datetime.datetime.now()

    for line in data_file:
        line = line.replace('\r\n', '')

        if import_above: # if this arg is passed, see if the current ID is above that value before importing
            if int(line.split(delimiter)[id_column]) > int(import_above):
                obj = import_object(parsing_class, line, id_column)
        else:
            obj = import_object(parsing_class, line, id_column)

    print('%s took %s' % (file_path, datetime.datetime.now() - start))

if __name__ == '__main__':
    if settings.DEBUG:
        print('Turn debug off, dummy.')
        exit()

    from fccdata.models import en, am, hd
    print('%s existing en objects' % en.objects.all().count())
    importer(os.path.join(FCC_PATH, 'EN.dat'), EN, id_column=1, delimiter='|', import_above=None)

    print('%s existing am objects' % am.objects.all().count())
    importer(os.path.join(FCC_PATH, 'AM.dat'), AM, id_column=1, delimiter='|', import_above=None)

    print('%s existing hd objects' % hd.objects.all().count())
    importer(os.path.join(FCC_PATH, 'HD.dat'), HD, id_column=1, delimiter='|', import_above=None)
