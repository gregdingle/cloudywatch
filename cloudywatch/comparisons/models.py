from django.db import models

from apps.models import Application


class Comparison(models.Model):
    title = models.CharField(max_length=200, editable=False)
    slug = models.CharField(max_length=200, unique=True, editable=False)
    applications = models.ManyToManyField(Application)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        parts = [app.title for app in self.apps]
        self.title = ' vs '.join(parts)
        self.slug = Comparison.generate_slug(self.apps)
        super(Comparison, self).save(*args, **kwargs)

    @classmethod
    def generate_slug(cls, applications):
        parts = [app.slug for app in applications]
        return '/vs/'.join(parts)

    @models.permalink
    def get_absolute_url(self):
        return ('comparison_detail', [Comparison.generate_slug(self.applications.all())])
