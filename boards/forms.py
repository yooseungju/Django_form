from django import forms
from .models import Board
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Board



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
            'rows':5,
            'cols':50 })
        
        }
        
        error_messages={
            'title':{'requird': '제목을 입력해주세요ㅜㅜ'},
            'content':{'requird': '내용을 입력해 주세요ㅜㅜ'}
        }
    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit('submit','작성'))
        
        
    
    
    