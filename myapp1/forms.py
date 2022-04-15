from django import forms
from myapp1.models import OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'client', 'items_ordered']
        labels = {
            'items_ordered': 'Quantity',
            'client': 'Client Name'
        }
        widgets = {
            'client': forms.RadioSelect()
        }

class InterestForm(forms.Form):
    interested = forms.ChoiceField(widget=forms.RadioSelect(), choices=((1, 'Yes'), (0, 'No')))
    quantity = forms.IntegerField(initial=1, min_value=1)
    comments = forms.CharField(label='Additional Comments', widget=forms.Textarea(), required=False)