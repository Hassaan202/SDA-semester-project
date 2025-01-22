from django import forms
from .models import *

class SubjectSelectionForm:
    class Meta:
        model=Subject
        fields= '__all__'


class DiscussionForm:
        class Meta:
            model=Discussion
            fields= '__all__'


SUBJECT_CHOICES=[]

def getSubjects():
    SUBJECT_CHOICES=Subject.object.all()



class ResourceForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    file = forms.FileField()