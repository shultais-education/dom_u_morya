from django import forms

from orders.models import Order
from houses.models import House


class OrderForm(forms.ModelForm):
    house = forms.ModelChoiceField(queryset=House.objects.all(), widget=forms.HiddenInput())
    personal_data = forms.BooleanField(label="Я согласен на обработку персональных данных", required=True)

    class Meta:
        model = Order
        fields = ["house", "name", "phone"]
