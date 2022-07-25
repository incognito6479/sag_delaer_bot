from mainapp.models import *
from django import forms


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class DealersModelForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = "__all__"


class CollectionModelForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = "__all__"


class CityModelForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"


class SubCollectionModelForm(forms.ModelForm):
    class Meta:
        model = SubCollection
        fields = "name", "link", "order_number"
