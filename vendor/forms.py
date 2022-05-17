from random import choice
from django import forms
from .models import *




class VendorForm(forms.ModelForm):
     business_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item-light mb-10 bg-transparent',
      'placeholder': 'Business name'
      
      }))
      
     location = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item-light mb-10 bg-transparent',
      'placeholder': 'Location'
      
      }))
      
     contact = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item-light mb-10 bg-transparent',
      'placeholder': 'contact 1'
      
      }))
      
     contact_2 = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item-light mb-10 bg-transparent',
      'placeholder': 'Contact 2'
      
      }))
      
     description = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item-light mb-10 bg-transparent',
      'placeholder': 'Description'
      
      }))
     photo = forms.ImageField(label=False, widget=forms.FileInput(attrs={
      'class':'form-item-light mb-10 bg-transparent',
      
      
      }))

     class Meta:
          model = VendorAcount
          fields=[
                'business_name',
                'photo',
                'location',
                'contact',    
                'contact_2',
                'description',
            ]
            


class VendorProfileForm(forms.ModelForm):
     business_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10',
      'placeholder': 'Business name'
      
      }))
      
     location = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10',
      'placeholder': 'Location'
      
      }))
      
     contact = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10',
      'placeholder': 'contact 1'
      
      }))
      
     contact_2 = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10',
      'placeholder': 'Contact 2'
      
      }))
      
     description = forms.CharField(label=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10',
      'placeholder': 'Description'
      
      }))
     photo = forms.ImageField(label=False,  widget=forms.FileInput(attrs={
      'class':'form-item mb-10',
      }))

     class Meta:
          model = VendorAcount
          fields=[
                'business_name',
                'photo',
                'location',
                'contact',    
                'contact_2',
                'description',
            ]
            

class FoodForm(forms.ModelForm):
     name = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10 bg-transparent',
      'placeholder': 'Food name'
      
      }))
      
     price = forms.IntegerField(label=False,required=False, widget=forms.NumberInput(attrs={
      'class':'form-item mb-10 ',
      'placeholder': 'Price'
      
      }))
      
     offer = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10 ',
      'placeholder': 'Offer'
      
      }))
      
     description = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10 ',
      'placeholder': 'Description'
      
      }))
     delivery_time = forms.CharField(label=False,required=False, widget=forms.TextInput(attrs={
      'class':'form-item mb-10 ',
      'placeholder': 'Delivery Time'
      
      }))
     photo = forms.ImageField(label=False,required=False, widget=forms.FileInput(attrs={
      'class':'form-item mb-10 ',      
      }))
      
     class Meta:
          model = Food
          fields=[
                'name',
                'photo',
                'price',
                'offer',
                'delivery_time',
                'description',
            ]
            
class FoodReviewForm(forms.ModelForm):
     rate = forms.ChoiceField(label=False,required=False, choices=reiview_choice, widget=forms.Select(attrs={
      'class':'form-item mb-10 ',  
      }))
     text = forms.CharField(label=False,required=False,widget=forms.TextInput(attrs={
      'class':'form-item mb-10 ',
      'placeholder': 'Comment'
      
      }))
     class Meta:
          model = FoodReview
          fields=[
                'rate',
                'text',
            ]