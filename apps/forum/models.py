from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Section(models.Model):
    title = models.CharField(_("Title"), max_length=150, unique=True)
    description = models.CharField(_("Description"), max_length=250)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Section, self).save(*args, **kwargs)


class Forum(models.Model):
    title = models.CharField(_("Title"), max_length=200150, unique=True)
    description = models.CharField(_("Description"), max_length=250)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Forum, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('forums_detail', kwargs={'slug': self.slug})


class Subject(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    title = title = models.CharField(_("Title"), max_length=150)
    publish_date = models.DateTimeField(_("Date of publication"), auto_now_add=True)
    text = models.TextField(_("Text"),)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Subject, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('subject_detail', kwargs={'slug': self.slug})


class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(_("Date of publication"), auto_now_add=True)
    text = models.TextField(_("Text"),)

    def __str__(self):
        return f"re: {self.Subject}"
