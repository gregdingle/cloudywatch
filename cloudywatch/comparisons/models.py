from django.db import models

from apps.models import Application


class Comparison(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    applications = models.ManyToManyField(Application)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('comparison_detail', [self.slug])
