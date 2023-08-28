from django.contrib.auth.forms import UserCreationForm
from . constants import ACCOUNT_TYPE,GENDER_TYPE
from django import forms
from django.contrib.auth.models import User
from . models import UserBankAccount,UserAddress
class UserRegistrationForm(UserCreationForm):
    account_type = forms.CharField(max_length=10,choices=ACCOUNT_TYPE)
    birth_date = forms.DateTimeField(null=True,blank=True)
    gender = forms.CharField(max_length=10,choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=10)
    class Meta:
        fields = ['username','firstname','lastname','email','account_type','password1','password2','gender', 'birth_date','postalcode','street_address','city','country']
    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            postalcode = self.cleaned_data.get('postalcode')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data('street_address')

            UserAddress.objects.create(
                  user = our_user,
                  postal_code = postalcode,
                  country = country,
                  city = city,
                  street_address = street_address,

            )
            UserBankAccount.objects.create(
                user = our_user,
                account_type = account_type,
                gender = gender,
                birth_date = birth_date,
                account_no = 10000 + our_user.id,
            )
        return our_user

