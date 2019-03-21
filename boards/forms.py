from django import forms
from .models import Board

# class BoardForm(forms.Form):
#     title = forms.CharField(label='제목',widget=forms.TextInput(attrs={
#                                                         'placeholder':'THE TITLE!',
                                                        
#     }))
#     content = forms.CharField(label='내용', 
#                                             error_messages={'required':'내용을 입력해 주세요'},
#                                             widget=forms.Textarea(attrs={
#                                                         'class':'Content-input',
#                                                         'rows':5,
#                                                         'cols':50,
#                                                         'placeholder':'Fill the Content',
                                                        
#     }))

class BoardForm(forms.ModelForm):
    class Meta:
        model =Board
        fields = '__all__'
        widgets = {'title': forms.TextInput(attrs={
            'placeholder':'제목을 입력해 주세요',
            'class':'title',
        }),
        'content':forms.TextInput(attrs={
            'placeholder':'내용을 입력해주세요',
            'class':'content',
            'rows':5,'cols':50 })
        
        }
        
        error_messages={
            'title':{'requird': '제목을 입력해주세요ㅜㅜ'},
            'content':{'requird': '내용을 입력해 주세요ㅜㅜ'}
        }
        
        
    
    
    