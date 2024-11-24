from django import forms

from accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:         # Meta-dan fərqli da vermək olmaz.
        model = Profile

        fields = ('about', 'phone_num')        # Profil form-u üçün olan fieldləri bu formada veririk.
        