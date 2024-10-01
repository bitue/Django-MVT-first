from django import forms


# turns to html code 
class contact_form (forms.Form):
    name = forms.CharField(label='User_Name')
    email = forms.EmailField(label='Email')
    profile = forms.FileField()
  
    
    
    
    