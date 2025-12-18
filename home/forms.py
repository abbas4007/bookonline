from django import forms
from .models import Rating


class RatingForm(forms.ModelForm) :
    stars = forms.ChoiceField(
        choices = [(i, '★' * i) for i in range(1, 6)],
        widget = forms.RadioSelect(attrs = {'class' : 'rating-radio'}),
        label = "امتیاز شما",
        required = True
    )

    review = forms.CharField(
        widget = forms.Textarea(attrs = {
            'rows' : 4,
            'placeholder' : 'نظر خود را درباره این محصول بنویسید...',
            'class' : 'form-control'
        }),
        label = "نظر شما",
        required = False
    )

    class Meta :
        model = Rating
        fields = ['stars', 'review']