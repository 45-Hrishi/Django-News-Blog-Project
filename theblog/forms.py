from django import forms
from django.db.models import fields
from .models import Comment, Post,Category
from django.forms import ChoiceField
from theblog.models import User

choices = Category.objects.all().values_list('name','name')
#choices = [('India','India'),('Entertainment','Entertainment'),('Technology','Technology'),('Corona','Corona'),('Politics','Politics'),('Buisness','Buisness'),('Sports','Sports'),('other','other')]
choice_list = []
for item in choices:
    choice_list.append(item)
 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body','header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id' : 'elder','type':'hidden'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body' : forms.TextInput(attrs={'class':'form-control','placeholder':'Content'}),
            
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','body')
        widgets = {
                'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
                'category' : forms.Select(choices=choice_list,attrs={'class':'form-control'}),
                'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}),
            }

class CommnetForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','author')
        widgets = {
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'Comment Here'}),
            
        }




    
