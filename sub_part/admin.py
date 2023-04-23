from django.contrib import admin

from . models import add_equipment_table, add_farmer_table, add_vendor_table, add_vehicle_table, add_fertilizer_table, add_pesticide_table, add_cart_table, contact_table, signup_table, add_feedback_table, add_drive_table, add_report_table, add_payment_table, add_booking_table, add_land_table, add_charge_table, add_duration_table

# Register your models here.

admin.site.register(contact_table)
admin.site.register(signup_table)
admin.site.register(add_feedback_table)
admin.site.register(add_cart_table)
admin.site.register(add_drive_table)
admin.site.register(add_report_table)
admin.site.register(add_payment_table)
admin.site.register(add_booking_table)
admin.site.register(add_land_table)
admin.site.register(add_charge_table)
admin.site.register(add_duration_table)
admin.site.register(add_equipment_table)
admin.site.register(add_farmer_table)
admin.site.register(add_vendor_table)
admin.site.register(add_vehicle_table)
admin.site.register(add_fertilizer_table)
admin.site.register(add_pesticide_table)