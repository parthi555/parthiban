from django import forms


from .models import Employee


class empfom(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True)
    mobile_no = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    course = forms.CharField(max_length=200)

    class Meta:
        model = Employee
        fields = {'name', 'mobile_no', 'email', 'course'}