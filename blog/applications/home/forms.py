from django import forms
from django.forms import widgets

from .models import Suscribers,Contact

class SuscribersForm(forms.ModelForm):
    """Form definition for Suscribers."""

    class Meta:
        """Meta definition for Suscribersform."""

        model = Suscribers
        fields = ('email',)
        widgets= {
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'Correo electronico...'
                }
            )
        }

class ContactForm(forms.ModelForm):
    """Form definition for Contact."""
    class Meta:
        """Meta definition for Contactform."""
        model = Contact
        fields = '__all__'


