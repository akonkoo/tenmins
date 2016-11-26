#coding: utf-8

from django import forms

def word_validator(comment):
    if len(comment) < 4:
        raise ValidationError("not enough words")

def comment_validator(comment):
    keywords = [u"发票", u"钱"]
    for keyword in keywords:
        if keyword in comment:
            raise ValidationError("Your comment contains invalid words,please check it again.")

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages = {
            "required": 'wow, such words'
            },
        validators = [word_validator, comment_validator]
        )

class ChangeUserForm(forms.Form):
    SEX_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
    )
    username = forms.CharField(max_length=250, label=u"姓名", initial="你的真实姓名" , required=False)
    sex = forms.ChoiceField(choices=SEX_CHOICES, required=False)
    password = forms.CharField(max_length=250, label=u"密码", initial="******", required=False)
    avatar = forms.ImageField(label=u"修改头像", required=False)