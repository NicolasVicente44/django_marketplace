from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "price", "image")
        widgets = {
        'category': forms.Select(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        }),
        'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        }),
        'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        }),
        'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        }),
        'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        })
    }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "image", 'is_sold')
        widgets = {
        'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        }),
        'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        }),
        'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        }),
        'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES,
                'required': 'required'
        })
    }
