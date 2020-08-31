from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
def upload_path(instance, filename):
    return '{0}/{1}'.format('logo_location', filename)


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, null=True, blank=True)
    logo = models.FileField(upload_to="logo_location", null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return str(self.title)

    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url

    def image_img(self):
        if self.logo and hasattr(self.logo, 'url'):
            return mark_safe('<img src="%s" style="width: 60px; height: 60px" />' % self.logo.url)
        else:
            return _('No Thumbnail')

    image_img.short_description = _('Thumbnail')


class Domain(DomainMixin):
    pass
