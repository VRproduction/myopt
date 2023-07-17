from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class AppointmentForm(forms.ModelForm):

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={'type': 'text',
                                                                                                'name': 'name',
                                                                                                'placeholder': _('Ad, Soyad')
                                                                                                }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'type': 'email',
                                                                                               'name': 'email',
                                                                                               'placeholder': _('E-mail')
                                                                                               }))

    date = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={'type': 'text',
                                                                                                   'name': 'date',
                                                                                                   'placeholder': _("Görüş tarixi"),
                                                                                                   # 'id': 'datepicker'
                                                                                                   }))

    class Meta:
        model = Appointment
        fields = '__all__'
        localized_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['name'].widget.attrs['placeholder'] = 'Ad, Soyad'
        # self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        # self.fields['date'].widget.attrs['placeholder'] = 'Görüş tarixi'

        for key, field in self.fields.items():
            field.label = ""





















class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'username',
        'placeholder': _('Ad, Soyad')
    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'type': 'email',
        'name': 'email',
        'placeholder': _('E-mail')
    }))

    phone = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'phone',
        'placeholder': _('Nömrə')
    }))

    subject = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'subject',
        'placeholder': _('Mövzu başlığı')
    }))

    message = forms.CharField(max_length=1200, widget=forms.Textarea(attrs={
        'name': 'message',
        'placeholder': _('Mesajınız')
    }))

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
















class Appointment2Form(forms.ModelForm):

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'phone',
        'placeholder': _('Ad, Soyad')
    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'type': 'email',
        'name': 'email',
        'placeholder': _('E-mail')
    }))

    phone = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'phone',
        'placeholder': _('Nömrə')
    }))

    date = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'date',
        'placeholder': _('Görüş tarixi'),
        'id': 'datepicker'
    }))

    message = forms.CharField(max_length=1200, widget=forms.Textarea(attrs={
        'name': 'message',
        'placeholder': _('Mesajınız')
    }))


    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
