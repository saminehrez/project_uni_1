from django import forms

class TranslateForm (forms.Form) :
    sendertext = forms.CharField(
        label = 'متن را وارد نمایید', 
        widget = forms.Textarea( attrs= {
            'class' : 'form-control' ,
            'style' : 'background-color:#ecffe6' ,
        })
    )