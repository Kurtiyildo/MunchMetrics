from django.forms import ModelForm
from django import forms
from .models import Restaurant, Meal, ReviewMeal, ReviewRestaurant
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('owner',)

        widgets = {
            'name': forms.TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Name'}),
            'address': forms.TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Address'}),
            'cuisine': forms.Select(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'cuisine'}),
            'image': forms.FileInput(
                attrs={'class': "form-control", 'style': 'max-width: 300px;'}),

        }


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Name'}),
            'price': forms.NumberInput(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Price'}),
            'restaurant': forms.Select(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Restaurant'}),
            'cuisine': forms.Select(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Cuisine'}),
            'image': forms.FileInput(
                attrs={'class': "form-control", 'style': 'max-width: 300px;'}),
        }


class MealRateForm(ModelForm):

    class Meta:
        model = ReviewMeal
        exclude = ('user', 'meal')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Title'}),
        }


class RestaurantRateForm(ModelForm):

    class Meta:
        model = ReviewRestaurant
        exclude = ('user', 'restaurant')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Title'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Email Address'})),
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'First Name'})),
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control", 'style': 'max-width: 300px;', 'placeholder': 'Last Name'})),

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. ' \
                                    'Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar ' \
                                     'to your other personal information.</li><li>Your password must contain at least' \
                                     '8 characters.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, ' \
                                     'for verification.</small></span>'


class UpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = User
        fields = ('username',  'first_name', 'last_name', 'email')
