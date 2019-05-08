#contact form a formulario de base de datos, suggestion enviar a correo
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = {'name', 'message'}
        labels = {'name': 'Nombre', 'message': 'Mensaje'}

class SubscriptionForm(forms.Form):
    email = forms.EmailField()
    want_spam = forms.BooleanField(required=False)


class SuggestionForm(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.TextInput)
    type = forms.ChoiceField(choices=[('bug', 'Bug'), ('feature', 'Feature')])


class GlobalMessageForm(forms.Form):
    staff_only = True
    global_message = forms.CharField(max_length=200, widget=forms.TextInput)

class MessageForm(forms.Form):
    message = forms.CharField(max_length=200, widget=forms.Textarea)
