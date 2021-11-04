from django import forms


class CollectBulkOrdersForm(forms.Form):
    orders = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "batch_emailer_orders"})
    )
    url = forms.CharField(widget=forms.HiddenInput(attrs={"id": "batch_emailer_url"}))
