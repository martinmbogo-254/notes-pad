from django import forms
from django import forms
from .models import Note

class NoteCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
    class Meta:
        model = Note
        fields = ['title','description']