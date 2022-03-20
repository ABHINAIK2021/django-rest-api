from django.db import models

class Purchase(models.Model):
    indent_no = models.CharField(max_length=30)
    po_no = models.CharField(max_length=30)
    grn_no = models.CharField(max_length=30)
    issue_no = models.CharField(max_length=30)
    item_name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    rate = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    total_amount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    discount = models.IntegerField(default=0)
    discount_amount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    net_amount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    gst = models.IntegerField(default=0)
    gst_amount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    igst_amount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    cgst_amount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    gross_amount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)