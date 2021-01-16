from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from hall.models import hall_details,Book_hall

class Usregis(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control',"placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","email",]
		widgets = {
		# "first_name":forms.TextInput(attrs = {
		# 	"class":"form-control",
		# 	"placeholder":"Enter Your Name",
		# 	"required":True,
		# 	}),
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your UserName",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Emailid",
			"required":True,
			}),
		
		}

# class Updation(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ["username","first_name","last_name","email"]
# 		widgets = {
# 		"username":forms.TextInput(attrs={
# 			"class":"form-control",
# 			}),
# 		"first_name":forms.TextInput(attrs={
# 			"class":"form-control",
# 			"placeholder":"Update First Name",
# 			}),
# 		"last_name":forms.TextInput(attrs={
# 			"class":"form-control",
# 			"placeholder":"Update Last Name",
# 			}),
# 		"email":forms.TextInput(attrs={
# 			"class":"form-control",
# 			"placeholder":"Update Email id",
# 			}),
# 		}

class halldetails(ModelForm):
	class Meta:
		model = hall_details
		fields = "__all__"
		widgets = {
		"number":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Room Number",
			}),
		"hall_type":forms.Select(attrs={
			"class":"form-control",
			"title":"hall_type"
			}),
		"capacity":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"capacity",
			}),
		"cost":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Cost",
			}),
		}

class Bookhall(ModelForm):
	class Meta:
		model = Book_hall
		fields = ['check_in','check_out']

		widgets = {
			"check_in":forms.DateInput(attrs={"class":"form-control","type":"date",}),
			"check_out":forms.DateInput(attrs={"class":"form-control","type":"date",}),
				}
