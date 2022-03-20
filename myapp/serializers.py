from rest_framework import serializers
from myapp.models import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('indent_no', 'po_no', 'grn_no', 'issue_no', 'item_name', 'quantity', 'rate', 'total_amount', 'discount', 'discount_amount', 'net_amount', 'gst', 'gst_amount', 'igst_amount', 'cgst_amount', 'gross_amount')