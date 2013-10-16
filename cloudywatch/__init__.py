from django.conf import settings
from django.contrib import sites
from django.contrib.sites.models import Site
from django.db.backends.signals import connection_created
from django.db.models.signals import post_syncdb


def update_site(sender, **kwargs):
    try:
        Site.objects.update(domain=settings.DOMAIN, name=settings.DOMAIN)
    except AttributeError:
        pass

post_syncdb.connect(update_site, sender=sites.models)


if settings.DEBUG:
    def disable_sqlite_synchronous_mode(sender, connection, **kwargs):
        if connection.vendor == 'sqlite':
            cursor = connection.cursor()
            cursor.execute('PRAGMA synchronous=OFF;')

    connection_created.connect(disable_sqlite_synchronous_mode)
