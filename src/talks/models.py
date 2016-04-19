from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models
# settings.AUTH_USER_MODEL
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
# Create your models here

class TalkList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        unique_together = ('user', 'name')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TalkList, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('talks:lists:detail', kwargs={'slug': self.slug})
