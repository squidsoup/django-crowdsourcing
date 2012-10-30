from django import forms
from django.utils.safestring import mark_safe

class RankedChoiceWidget(forms.MultiWidget):
    """ A widget which displays n select boxes, recording
        ranked choices from 1-n.
    """

    def __init__(self, attrs=None, *args, **kwargs):

        choices = kwargs.pop('choices', [])
        _widgets = (
                forms.Select(attrs=attrs, choices=choices),
                forms.Select(attrs=attrs, choices=choices),
                forms.Select(attrs=attrs, choices=choices),
                )
        super(RankedChoiceWidget, self).__init__(_widgets, *args, **kwargs)

    def decompress(self, value):
        if value:
            val = value.split(',')
            return [val[0], val[1], val[2]]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        markup = """<p class="ranked">
                    <label><span>1<sup>st</sup></span></label> %s
                    <label><span>2<sup>nd</sup></span></label> %s
                    <label><span>3<sup>rd</sup></span></label> %s
                    </p>
                    """ % (rendered_widgets[0],
                           rendered_widgets[1],
                           rendered_widgets[2],)
        return markup

