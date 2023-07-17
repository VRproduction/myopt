from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _


class AppointmentForm(forms.ModelForm):

    name = forms.CharField(label=_('Ad, Soyad'), max_length=1200, widget=forms.TextInput(attrs={'type': 'text',
                                                                                                'name': 'name',
                                                                                                'placeholder': 'Ad, Soyad'
                                                                                                }))

    email = forms.EmailField(label=_('E-mail'), max_length=100, widget=forms.EmailInput(attrs={'type': 'email',
                                                                                               'name': 'email',
                                                                                               'placeholder': 'E-mail'
                                                                                               }))

    date = forms.CharField(label=_("Görüş tarixi"), max_length=1200, widget=forms.TextInput(attrs={'type': 'text',
                                                                                                   'name': 'date',
                                                                                                   'placeholder': 'Görüş tarixi',
                                                                                                   # 'id': 'datepicker'
                                                                                                   }))

    """
    date = forms.CharField(label=_('Görüş tarixi'), max_length=1200, widget=forms.TextInput(attrs={'type': 'text',
                                                                                                   'name': 'date',
                                                                                                   'placeholder': 'Görüş tarixi',
                                                                                                   # 'id': 'datepicker'
                                                                                                   }))
    """

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

    name = forms.CharField(label=_('Ad, Soyad'), max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'username',
        'placeholder': 'Ad, Soyad'
    }))

    email = forms.EmailField(label=_('E-mail'), max_length=100, widget=forms.EmailInput(attrs={
        'type': 'email',
        'name':'email',
        'placeholder':'E-mail'
    }))

    phone = forms.CharField(label=_('Nömrə'), max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name':'phone',
        'placeholder':'Nömrə'
    }))

    subject = forms.CharField(label=_('Mövzu başlığı'), max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name':'subject',
        'placeholder':'Mövzu başlığı'
    }))

    message = forms.CharField(label=_('Mesajınız'), max_length=1200, widget=forms.Textarea(attrs={
        'name':'message',
        'placeholder':'Mesajınız'
    }))

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
















class Appointment2Form(forms.ModelForm):

    name = forms.CharField(label=_('Ad, Soyad'), max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name':'phone',
        'placeholder':'Ad, Soyad'
    }))

    email = forms.EmailField(label=_('E-mail'), max_length=100, widget=forms.EmailInput(attrs={
        'type': 'email',
        'name':'email',
        'placeholder':'E-mail'
    }))

    phone = forms.CharField(label=_('Nömrə'), max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name':'phone',
        'placeholder':'Nömrə'
    }))

    date = forms.CharField(label=_('Görüş tarixi'), max_length=1200, widget=forms.TextInput(attrs={
        'type': 'text',
        'name':'date',
        'placeholder':'Görüş tarixi',
        'id':'datepicker'
    }))

    message = forms.CharField(label=_('Mesajınız'), max_length=1200, widget=forms.Textarea(attrs={
        'name': 'message',
        'placeholder': 'Mesajınız'
    }))


    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
