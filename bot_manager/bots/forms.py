from django import forms
from .models import BotGroup

class BotGroupForm(forms.ModelForm):
    class Meta:
        model = BotGroup
        fields = ['title', 'platform', 'url', 'is_active']

    def clean_url(self):
        url = self.cleaned_data.get('url')
        platform = self.cleaned_data.get('platform')

        if platform == 'Facebook' and not url.startswith('https://www.facebook.com/groups/'):
            raise forms.ValidationError('URL must begin with https://www.facebook.com/groups/ for Facebook platform.')
        
        return url
