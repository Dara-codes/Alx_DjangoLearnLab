from glob import escape
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Book
from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField(
        required=False, 
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    profile_photo = forms.ImageField(
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'profile_photo']

from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9\s]*$',
                message='Only alphanumeric characters are allowed.',
                code='invalid_search'
            )
        ]
    )

    def clean_search_query(self):
        """Additional cleaning/sanitization of search query."""
        query = self.cleaned_data.get('search_query', '')
        return escape(query.strip())
    
    class ExampleForm(forms.Form):
       name = forms.CharField(max_length=100)
       email = forms.EmailField()
       message = forms.CharField(widget=forms.Textarea)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
    
    def clean_title(self):
        """Sanitize the title field."""
        title = self.cleaned_data.get('title')
        return escape(title.strip())

    def clean_author(self):
        """Sanitize the author field."""
        author = self.cleaned_data.get('author')
        return escape(author.strip())