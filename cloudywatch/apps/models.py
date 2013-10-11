from django.db import models

from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('application_list', [self.slug])


class Application(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    logo = ImageField(upload_to='apps/%y/%m')
    description = RichTextField()
    url = models.URLField()
    pingdom_id = models.PositiveIntegerField(unique=True)
    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('application_detail', [self.category.slug, self.slug])
