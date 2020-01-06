from django import forms


class QRForm(forms.Form):
    text = forms.CharField(label='Enter QR Text', max_length=100)


class UploadFileForm(forms.Form):
    file = forms.FileField()
