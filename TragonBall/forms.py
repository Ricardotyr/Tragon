from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=30, required=True, widget=forms.TextInput(attrs={'size': '43'}))
    correo = forms.EmailField(label="Correo", required=True, widget=forms.TextInput(attrs={'size':'43'}))
    mensaje = forms.CharField(label="Mensaje", max_length=1000, widget=forms.Textarea(attrs={'size': '42'}), required=True)