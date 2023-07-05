from django import forms
from .models import *


class AppointmentForm(forms.ModelForm):

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'name',
        'placeholder':'Ad, Soyad'



    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={



        'type': 'email',
        'name':'email',
        'placeholder':'E-mail'


    }
    ))


    date = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={

        'type': 'text',
        'name': 'date',
        'placeholder': 'Görüş tarixi',
        'id': 'datepicker'
    }))


    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""




class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name': 'username',
        'placeholder': 'Ad, Soyad'



    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={



        'type': 'email',
        'name':'email',
        'placeholder':'E-mail'


    }
    ))

    phone = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'phone',
        'placeholder':'Nömrə'



    }))

    subject = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'subject',
        'placeholder':'Mövzu başlığı'



    }))


    message = forms.CharField(max_length=1200, widget=forms.Textarea(attrs={



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

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'phone',
        'placeholder':'Ad, Soyad'



    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={



        'type': 'email',
        'name':'email',
        'placeholder':'E-mail'


    }
    ))

    phone = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'phone',
        'placeholder':'Nömrə'



    }))

    date = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={

        'type': 'text',
        'name':'date',
        'placeholder':'Görüş tarixi',
        'id':'datepicker'
    }))

    message = forms.CharField(max_length=1200, widget=forms.Textarea(attrs={


        'name':'message',
        'placeholder':'Mesajınız'



    }))



    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
