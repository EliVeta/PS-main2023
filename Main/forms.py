from .models import CommentsPost
from django.forms import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsPost
        fields = ['id_user','text','created',
                  'grade']
