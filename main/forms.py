from django import forms
from apps.fleet.models import Trucks, Trailers
from apps.orders.models import Orders
from apps.employees.models import Employees
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from apps.users.models import CustomUser


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != 'status':
                visible.field.widget.attrs['class'] = 'form-control'

# ORDERS FORMS
class OrdersForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Orders
        fields = ['order_type', 'company', 'address', 'cargo_weight', 'cargo_size', 'eta', 'status',]
        widgets = {
            'eta': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 2, 'cols': 20, 'maxRows': 2}),
            'status': forms.RadioSelect(choices=((True, 'Uncompleted'), (False, 'Completed'))),
            'order_type': forms.Select(attrs={'placeholder': 'Select order type'})
        }




# ---------------------------------------------------------------------------------------------------

# FLEET FORMS
class TrucksForm(BaseForm, forms.ModelForm):
    
    class Meta:
        model = Trucks
        fields = ['truck_make', 'truck_model', 'year', 'mileage', 'color', 'registration_plate', 'truck_image', 'status']

class TrailersForm(BaseForm, forms.ModelForm):
        
    class Meta:
        model = Trailers
        fields = ['trailer_make', 'trailer_model', 'year', 'color', 'registration_plate', 'trailer_image', 'status']

# ---------------------------------------------------------------------------------------------------

# USER FORMS
class UserRegistrationForm(BaseForm, UserCreationForm):
    email = forms.EmailField(help_text='A valid email address.', required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']

# EMPLOYEE FORM
class EmployeeUpdateForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username')


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = CustomUser
        fields = ['new_password1', 'new_password2']


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


# ---------------------------------------------------------------------------------------------------
