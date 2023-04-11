from django.forms import ModelForm
from .models import Contact

#Code for Contact form
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'