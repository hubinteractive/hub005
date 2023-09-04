from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileInfo

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TimeInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

        # widgets = {
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
            
        # }

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-check'}))
    is_superuser = forms.CharField(max_length=150, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(max_length=150, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(max_length=150, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','username', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', )


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.EmailField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2' )



class ProfileCreteForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields ='__all__'
        # fields = ('title', 'title_tag', 'author','header_image', 'snippet', 'content', 'cat_name', 'body', )

        # widgets = {
        #     'title': forms.TextInput(attrs={'class':'form-control'}),  
        #     'title_tag': forms.TextInput(attrs={'class':'form-control'}),  
        #     'author': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'sneks', 'type':'hidden'}), 
        #      'snippet': forms.Textarea(attrs={'class':'form-control'}),
        #     # 'author': forms.Select(attrs={'class':'form-control'}),  
        #     'cat_name': forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
        #     'body': forms.Textarea(attrs={'class':'form-control'}),  
        # }


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = '__all__'
        # fields = ('title', 'title_tag', 'author','header_image', 'snippet', 'content', 'cat_name', 'body', )

        # widgets = {
        #     'title': forms.TextInput(attrs={'class':'form-control'}),  
        #     'title_tag': forms.TextInput(attrs={'class':'form-control'}),  
        #     'author': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'sneks', 'type':'hidden'}), 
        #      'snippet': forms.Textarea(attrs={'class':'form-control'}),
        #     # 'author': forms.Select(attrs={'class':'form-control'}),  
        #     'cat_name': forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
        #     'body': forms.Textarea(attrs={'class':'form-control'}),  
        # }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileInfo
        fields = '__all__'
        # fields = ('title', 'title_tag', 'author','header_image', 'snippet', 'content', 'cat_name', 'body', )

        # widgets = {
        #     'title': forms.TextInput(attrs={'class':'form-control'}),  
        #     'title_tag': forms.TextInput(attrs={'class':'form-control'}),  
        #     'author': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'sneks', 'type':'hidden'}), 
        #      'snippet': forms.Textarea(attrs={'class':'form-control'}),
        #     # 'author': forms.Select(attrs={'class':'form-control'}),  
        #     'cat_name': forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
        #     'body': forms.Textarea(attrs={'class':'form-control'}),  
        # }


 