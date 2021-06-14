from django import forms
 
from .models import Comment
 
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labуls = {
        	'body': 'Ваш отзыв'
        }
        

class SearchForm(forms.Form): 
    query = forms.CharField(label='',error_messages='')
    