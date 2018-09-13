from django import forms
from apps.postserver.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['texto'] # 'timestamp', 'ip'

        labels = {
        'texto': 'Escribe tu post',
        }

        widgets = {
        'texto': forms.TextInput(attrs={'class':'form-control'}),
        }
