from django import forms
from .models import FeedBack


# class Form(forms.Form):
#     name = forms.CharField(label='enter name', min_length=2,
#                            error_messages={
#                                'min_length': 'name is too short',
#                                'required': 'nessasary field'
#                            })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))

class Form(forms.ModelForm):
    class Meta:
        model = FeedBack
        # fields = ['name', 'feedback']
        # exclude = ['surname']
        fields = '__all__'
        labels = {
            'name': 'label_name',
            'surname': 'label_surname',
            'feedback': 'label_feedback',
        }
        error_messages = {
            'name': {
                'min_length': 'min lenght error'
            }
        }
