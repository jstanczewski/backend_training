from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea
from viewer.models import Genre
import re
from datetime import date
from django.core.exceptions import ValidationError


# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')


class MyFieldClass(IntegerField):
    def clean(self):
        pass


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Title must be capitalized!')


class PastDateField(DateField):
    def validate(self, value):
        super().validate(value)
        if value > date.today():
            raise ValidationError('Future dates are not allowed!')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(Form):
    title = CharField(max_length=170, validators=[capitalized_validator])
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    released = PastDateField()
    description = CharField(widget=Textarea, required=False)

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Horror' and result['rating'] > 5:
            self.add_error('genre', '')
            self.add_error('rating', '')
            raise ValidationError('A horror movie cannot be rated above 5!')
        return result
