from __future__ import absolute_import

from .widgets import RankedChoiceWidget
from django.forms import MultiValueField
from django.forms.fields import ChoiceField

import copy

try:
    from sorl.thumbnail.fields import ImageWithThumbnailsField
except ImportError:
    from django.db.models import ImageField

    class ImageWithThumbnailsField(ImageField):

        def __init__(self, *args, **kwargs):
            kwargs.pop('thumbnail', None)
            super(ImageWithThumbnailsField, self).__init__(*args, **kwargs)

class RankedChoiceField(MultiValueField):
    widget = RankedChoiceWidget

    def __init__(self, choices=None, *args, **kwargs):
        if choices is None:
            choices = ()

        fields = (
                ChoiceField(),
                ChoiceField(),
                ChoiceField(),
        )
        super(RankedChoiceField, self).__init__(fields, *args, **kwargs)
        self.choices = choices

    def __deepcopy__(self, memo):
        result = super(RankedChoiceField, self).__deepcopy__(memo)
        result.fields = copy.deepcopy(self.fields, memo)
        return result

    def compress(self, data_list):
        if data_list:
            return ','.join(data_list)

    def _set_choices(self, value):
        self._choices = list(value)

        # set on field for validation
        for field in self.fields:
            field.choices = self._choices

        # set on widget for rendering
        for widget in self.widget.widgets:
            widget.choices = self._choices

    def _get_choices(self):
        return self._choices

    choices = property(_get_choices, _set_choices)
