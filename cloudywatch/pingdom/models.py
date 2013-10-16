from django.db import models


class Probe(models.Model):
    application = models.ForeignKey('apps.Application', related_name='pingdom_probes')
    status = models.CharField(max_length=200)
    probeid = models.PositiveIntegerField(db_index=True)
    responsetime = models.PositiveIntegerField(null=True)
    timestamp = models.DateTimeField(db_index=True)
    
    def __unicode__(self):
        return self.status
