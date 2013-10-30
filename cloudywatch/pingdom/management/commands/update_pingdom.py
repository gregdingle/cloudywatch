from datetime import datetime, timedelta
import time

from django.core.management.base import BaseCommand

from pingdom.api import pingdom, PingdomError
from apps.models import Application
from pingdom.models import Probe


class Command(BaseCommand):
    "This command should run every hour and collect latest pingdom data for last hour"
    
    def handle(self, *args, **opts):
        for app in Application.objects.filter(enabled=True):
            print 'getting pingdom data for %s(%s)' % (app, app.pingdom_id)
            downtime_from = datetime.now() - timedelta(days=30)
            downtime_from_timestamp = time.mktime(downtime_from.timetuple())
            try:
                probes = pingdom.get('/results/{0}'.format(app.pingdom_id))['results']
                downtime = pingdom.get('/summary.average/{0}?from={1}&includeuptime=true'
                                       .format(app.pingdom_id,
                                               downtime_from_timestamp))['summary']['status']['totaldown']
            except PingdomError, e:
                print e
                continue

            app.downtime = downtime
            app.save()

            instances_to_create = []
            for probe in probes:
                # obj, created = app.pingdom_probes.get_or_create(
                #     probeid=int(probe['probeid']),
                #     timestamp=datetime.fromtimestamp(probe['time']),
                #     defaults=dict(
                #         status=probe['status'],
                #         responsetime=probe.get('responsetime')
                #     )
                # )
                #print created, obj.probeid, obj.timestamp

                probeid = int(probe['probeid'])
                timestamp = datetime.fromtimestamp(probe['time'])
                if Probe.objects.filter(application=app, probeid=probeid, timestamp=timestamp).exists():
                    continue
                instances_to_create.append(
                    Probe(
                        application=app,
                        probeid=probeid,
                        timestamp=timestamp,
                        status=probe['status'],
                        responsetime=probe.get('responsetime')
                    )
                )

            print "{0} new probe(s) created".format(len(instances_to_create))
            Probe.objects.bulk_create(instances_to_create)
