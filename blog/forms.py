from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    subject = forms.CharField(
        label='Тема письма*',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тему вашего письма'})
    )
    from_email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
        )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваше сообщение'}),
        required=True)

    class Meta:
        model = Message
        fields = ['subject', 'from_email', 'message']
