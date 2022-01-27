from django import forms
from menu.models import Menu, Meal, MealRating
from recipes.models import Recipe


class MealRatingForm(forms.ModelForm):
    class Meta:
        model = MealRating
        fields = ('rating', 'comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].required = False
