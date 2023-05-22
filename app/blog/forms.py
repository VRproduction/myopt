from django import forms
from .models import *


class AppointmentForm(forms.ModelForm):

    name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'name',
        'placeholder':'Sizin adınız'



    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={



        'type': 'email',
        'name':'email',
        'placeholder':'Sizin e-mail'


    }
    ))


    date = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={

        'type': 'text',
        'name':'date',
        'placeholder':'Görüş tarixi',
        'id':'datepicker'
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
        'name':'username',
        'placeholder':'Sizin adınız'



    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={



        'type': 'email',
        'name':'email',
        'placeholder':'Sizin email'


    }
    ))

    phone = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'phone',
        'placeholder':'Sizin nömrə'



    }))

    subject = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'subject',
        'placeholder':'Mövzu başlığı'



    }))


    message = forms.CharField(max_length=1200, widget=forms.Textarea(attrs={



        'name':'message',
        'placeholder':'Sizin mesaj'



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
        'placeholder':'Sizin adınız'



    }))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={



        'type': 'email',
        'name':'email',
        'placeholder':'Sizin email'


    }
    ))

    phone = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={


        'type': 'text',
        'name':'phone',
        'placeholder':'Sizin nömrə'



    }))

    date = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={

        'type': 'text',
        'name':'date',
        'placeholder':'Gorus Tarixi',
        'id':'datepicker'
    }))



    message = forms.CharField(max_length=1200, widget=forms.Textarea(attrs={



        'name':'message',
        'placeholder':'Sizin mesaj'



    }))



    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""