import uuid

from django.db import models
from tinymce.models import HTMLField


class Activity(models.Model):
    """The Activity model that stores the student activity"""

    name = models.TextField()
    description = models.TextField()
    activity_type = models.CommaSeparatedIntegerField(max_length=3) # CAS: 1,2,3
    learning_obj = models.CommaSeparatedIntegerField(max_length=8)  # 1,...,8
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(blank=True, null=True)

    # Activity advisor information.
    # This is different from the school advisor, which has a model!
    advisor_name = models.CharField(max_length=30, blank=True)
    advisor_title = models.CharField(max_length=30, blank=True)
    advisor_email = models.EmailField(blank=True)
    advisor_phone = models.CharField(max_length=12, blank=True)
    # TODO: Move field to form validation
    # advisor_phone = localflavor_models.PhoneNumberField(blank=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ('start_date',)


class Entry(models.Model):
    """The Entry model that stores the student activity"""

    activity = models.ForeignKey(Activity)
    entry = HTMLField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
