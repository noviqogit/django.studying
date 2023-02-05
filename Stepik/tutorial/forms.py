from django import forms


class Form(forms.Form):
    name = forms.CharField(label='enter name', min_length=2,
                           error_messages={
                               'min_length': 'name is too short',
                               'required': 'nessasary field'
                           })
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
