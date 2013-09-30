from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
    	verbose_name_plural = 'categories'
    
    def __unicode__(self):
        return self.title


class Application(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    pingdom_id = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.title

