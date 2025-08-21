from django import forms
from django.utils import timezone
from .models import Task

DATETIME_INPUT_FORMAT = "%Y-%m-%dT%H:%M"

class BaseTaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"},
            format=DATETIME_INPUT_FORMAT,
        ),
        input_formats=[DATETIME_INPUT_FORMAT],
    )

    class Meta:
        model = Task
        fields = []
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.deadline:
            dt = self.instance.deadline
            try:
                dt = timezone.localtime(dt)
            except Exception:
                pass
            self.initial["deadline"] = dt.strftime(DATETIME_INPUT_FORMAT)


class TaskCreateForm(BaseTaskForm):
    class Meta(BaseTaskForm.Meta):
        fields = ["content", "deadline", "tags"]


class TaskUpdateForm(BaseTaskForm):
    class Meta(BaseTaskForm.Meta):
        fields = ["content", "deadline", "tags", "is_done"]
