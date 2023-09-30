from django import forms
from posts.models import Posts, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['user', 'content']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            # 'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control border-0 bg  form-control-lg',
                                             'rows': '1', 'type': "text", 'placeholder': "What's happening?"}),
                                            }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user', 'content']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;'}),
            'content': forms.Textarea(attrs={'class': 'form-control', "rows": "2"})
                   }