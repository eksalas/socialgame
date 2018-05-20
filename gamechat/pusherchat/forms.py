from django import forms
class CommentForm(forms.Form):
  comment = forms.CharField(
    max_length=400,
    widget=forms.TextInput(attrs={
      'placeholder': 'enter your review'
  }))