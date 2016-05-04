import json

from django.db import models
from django import forms
from django.forms.widgets import Textarea, NumberInput
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.encoding import force_text


class BBCodeWidget(Textarea):
    class Media:
        js = ('js/ckeditor/ckeditor.js', )

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return format_html('<textarea{}>\r\n{}</textarea><script>CKEDITOR.replace(' + json.dumps(name) + ')</script>',
                           flatatt(final_attrs),
                           force_text(value))


class RatingWidget(NumberInput):
    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, min=1, max=5, **{'class': 'rating'})
        return super(RatingWidget, self).render(name, value, final_attrs)


class BBCodeField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'widget': BBCodeWidget}
        defaults.update(kwargs)
        return super(BBCodeField, self).formfield(**defaults)
