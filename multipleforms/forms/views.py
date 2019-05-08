from django.shortcuts import render, redirect
from django.contrib import messages

from forms import forms
from forms.multiple_forms import MultipleFormsView
from django.core.mail import send_mail


# Create your views here.
class MultipleFormsDemoView(MultipleFormsView):
    template_name = 'forms.html'
    success_url = '/'

    # here we specify all forms that should be displayed
    forms_classes = [
        forms.GlobalMessageForm,
        forms.ContactForm,
        forms.SubscriptionForm,
        forms.SuggestionForm
    ]

    def get_forms_classes(self):
        # we hide staff_only forms from not-staff users
        # our goal no. 3 about dynamic amount list of forms
        forms_classes = super(MultipleFormsDemoView, self).get_forms_classes()
        user = self.request.user
        if not user.is_authenticated() or not user.is_staff:
            return list(filter(lambda form: not getattr(form, 'staff_only', False), forms_classes))

        return forms_classes

    def form_valid(self, form):
        print("yay it's valid!")
        return super(MultipleFormsDemoView, self).form_valid(form)


    def get_form(request):
        if request.request.method == 'POST':
            form_contact = forms.ContactForm(request.request.POST)
            form_suggestion = forms.SuggestionForm(request.request.POST)
            if form_contact.is_valid():
                post_contact = form_contact.save(commit=False)
                post_contact.save()
                return form_contact

            if form_suggestion.is_valid():
                subject = form_suggestion.data['type']
                message = form_suggestion.data['text']
                from_email = 'pruebra.monoku@gmail.com'
                send_mail(subject, message, from_email, ['sjcc333@gmail.com']) 
                return form_suggestion
        else:
            return form_contact
