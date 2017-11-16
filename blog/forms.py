from django import forms
#Use Built in form frame works in django to make eaasy use of forms.
class EmailPostForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject  = forms.CharField()
    message = forms.CharField(required=False, widget=forms.Textarea)
