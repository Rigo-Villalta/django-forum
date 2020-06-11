from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Subject


class NewSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["title", "text"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": _("Title of new subject"),}
        )
        self.fields["text"].widget.attrs.update({
            "class": "form-control", "rows": "3",
        })
