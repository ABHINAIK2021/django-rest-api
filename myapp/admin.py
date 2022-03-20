from django.contrib import admin
from myapp.models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list = ('indent_no', 'po_no', 'grn_no', 'issue_no', 'item_name', 'quantity', 'rate', 'total_amount', 'discount', 'discount_amount', 'net_amount', 'gst', 'gst_amount', 'igst_amount', 'cgst_amount', 'gross_amount')
admin.site.register(Purchase, PurchaseAdmin)