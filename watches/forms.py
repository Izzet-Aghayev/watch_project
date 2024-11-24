from django import forms
# Yaratfığımız model import edilir
from watches.models import Watch


class WatchForm(forms.ModelForm):

    class Meta:
        model = Watch
        exclude = ('user',)  # Bununla seçilmiş fieldlər xaric digər fieldlər götrülür.
