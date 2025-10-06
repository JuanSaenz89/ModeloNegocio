from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(unique=True, verbose_name="Key Name", max_length=100)
    name = models.CharField(max_length=200, verbose_name="Social Net")
    url = models.URLField(verbose_name="URL", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
        ordering = ['name']


    def __str__(self):
        return self.name