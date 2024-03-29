from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.forms import TextInput

from .models.answer import Answer
from .models.question import Question
from .models.comment import Comment

User = get_user_model()


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')

    # image = forms.ImageField(required=True, label='Image')

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    first_name = forms.CharField(
        label=("Name"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'text',
                                          'required': 'true',
                                          }))

    last_name = forms.CharField(
        label=("Surname"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'text',
                                          'required': 'true',
                                          }))
    username = forms.RegexField(
        label=("Username"), max_length=15, regex=r"^[\w.@+-]+$",
        help_text=("Required. 15 characters or fewer. Letters, digits and "
                   "@/./+/-/_ only."),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                        "@/./+/-/_ characters.")},
        widget=TextInput(attrs={'class': 'form-control',
                                'required': 'true',
                                })
    )

    email = forms.CharField(
        label=("Email"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'text',
                                          'required': 'true',
                                          'placeholder': 'for_example@mail.ru'
                                          }))
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',
                                          })
    )

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'required': 'true',
                                          })
    )

    def email_clean(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label=("Username or Email"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'required': 'true',
                                      }))
    password = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          }))


# class TagWidget(s2forms.ModelSelect2Widget):
#     search_fields = [
#         "name__icontains",
#     ]


class QuestionCreate(forms.ModelForm):
    title = forms.CharField(
        label=("Title"),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'required': 'true',
        }))

    content = forms.CharField(
        label=("Describe your problem in detail"),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'required': 'true',
        }))

    class Meta:
        model = Question
        # widgets = {
        #     'tag': TagWidget,
        # }
        exclude = ["author", "created_at"]
        fields = ("title", "content")


class AnswerCreate(forms.ModelForm):
    pk = forms.IntegerField(),

    # is_useful = forms.BooleanField(
    #     label=('Is Useful?'),
    #     widget=forms.HiddenInput
    # )

    label = ("Comment"),
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'required': 'true',
        }))

    # def clean_recipients(self):
    #     #cleaned_data = super().clean()
    #     #pk = cleaned_data.get("pk")
    #     pk = self.cleaned_data['pk']
    #     try:
    #         User.objects.get(pk=pk)
    #     except User.DoesNotExist:
    #         return pk
    #     raise forms.ValidationError("User Name has been taken!")

    class Meta:
        model = Answer
        exclude = ["author", "created_at"]
        fields = ("content",)


class CommentCreate(forms.ModelForm):
    label = ("Reply"),
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'required': 'true',
        }))

    class Meta:
        model = Comment
        exclude = ["author", "created_at"]
        fields = ("content",)

class UserPhotoUpdate(forms.ModelForm):
    image = forms.ImageField(
        label=(""),
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'type': 'file'
        }))

    class Meta:
        model = User
        #exclude = ["author", "created_at"]
        fields = ("image",)
