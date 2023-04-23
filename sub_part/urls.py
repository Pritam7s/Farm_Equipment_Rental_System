from codecs import namereplace_errors
from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('dashboard/<int:id>', views.dashboard, name='dashboard'),

    #--------------------------------Cart CRUD

    path('cart_details/<int:id>',views.cart_details, name='cart_details'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path('add_cart_form/<int:id>', views.add_cart_form, name='add_cart_form'),
    path('edit_cart/<int:id>/<int:row_id>', views.edit_cart, name='edit_cart'),
    path('update_cart_form/<int:id>/<int:row_id>', views.update_cart_form, name='update_cart_form'),
    path('delete_cart_data/<int:id>/<int:row_id>', views.delete_cart_data, name='delete_cart_data'),

    #--------------------------------- DRIVE CRUD

    path('drive_details/<int:id>', views.drive_details, name='drive_details'),
    path('add_drive/<int:id>', views.add_drive, name='add_drive'),
    path('edit_drive/<int:id>/<int:row_id>', views.edit_drive, name='edit_drive'),
    path('add_drive_form/<int:id>', views.add_drive_form, name='add_drive_form'),
    path('update_drive_form/<int:id>/<int:row_id>', views.update_drive_form, name='update_drive_form'),
    path('delete_drive_data/<int:id>/<int:row_id>', views.delete_drive_data, name='delete_drive_data'),
    
    #---------------------------------Feedback CRUD

    path('feedback/<int:id>', views.feedback, name='feedback'),
    path('add_feedback/<int:id>', views.add_feedback, name='add_feedback'),
    path('add_feedback_form/<int:id>', views.add_feedback_form, name='add_feedback_form'),
    path('edit_feedback/<int:id>/<int:row_id>', views.edit_feedback, name='edit_feedback'),
    path('update_feedback_form/<int:id>/<int:row_id>', views.update_feedback_form, name='update_feedback_form'),
    path('delete_feedback_data/<int:id>/<int:row_id>', views.delete_feedback_data, name='delete_feedback_data'),
    

    #---------------------------------Report CRUD

    path('report_details/<int:id>', views.report_details, name='report_details'),
    path('add_report/<int:id>', views.add_report, name='add_report'),
    path('add_report_form/<int:id>', views.add_report_form, name='add_report_form'),
    path('edit_report/<int:id>/<int:row_id>', views.edit_report, name='edit_report'),
    path('update_report_form/<int:id>/<int:row_id>', views.update_report_form, name='update_report_form'),
    path('delete_report_data/<int:id>/<int:row_id>', views.delete_report_data, name='delete_report_data'),

    #---------------------------------Land CRUD

    path('land_types/<int:id>',views.land_types,name='land_types'),
    path('add_land/<int:id>', views.add_land, name='add_land'),
    path('add_land_form/<int:id>', views.add_land_form, name='add_land_form'),
    path('edit_land/<int:id>/<int:row_id>',views.edit_land,name='edit_land'),
    path('update_land_form/<int:id>/<int:row_id>', views.update_land_form, name='update_land_form'),
    path('delete_land_data/<int:id>/<int:row_id>', views.delete_land_data, name='delete_land_data'),

    #---------------------------------Rent CRUD

    path('rent_charges/<int:id>',views.rent_charges,name='rent_charges'),
    path('add_charge/<int:id>', views.add_charge, name='add_charge'),
    path('add_charge_form/<int:id>', views.add_charge_form, name='add_charge_form'),
    path('edit_charge/<int:id>/<int:row_id>',views.edit_charge,name='edit_charge'),
    path('update_charge_form/<int:id>/<int:row_id>', views.update_charge_form, name='update_charge_form'),
    path('delete_charge_data/<int:id>/<int:row_id>', views.delete_charge_data, name='delete_charge_data'),
    
    #            ---------- Charge ---------- Durartion ----------

    path('rent_duration/<int:id>',views.rent_duration,name='rent_duration'),
    path('add_duration/<int:id>', views.add_duration, name='add_duration'),
    path('add_duration_form/<int:id>', views.add_duration_form, name='add_duration_form'),
    path('edit_duration/<int:id>/<int:row_id>',views.edit_duration,name='edit_duration'),
    path('update_duration_form/<int:id>/<int:row_id>', views.update_duration_form, name='update_duration_form'),
    path('delete_duration_data/<int:id>/<int:row_id>', views.delete_duration_data, name='delete_duration_data'),
    
    #---------------------------------Booking CRUD

    path('booking_details/<int:id>', views.booking_details, name='booking_details'),
    path('add_booking/<int:id>', views.add_booking, name='add_booking'),
    path('add_booking_form/<int:id>', views.add_booking_form, name='add_booking_form'),
    path('edit_booking/<int:id>/<int:row_id>', views.edit_booking, name='edit_booking'),
    path('update_booking_form/<int:id>/<int:row_id>', views.update_booking_form, name='update_booking_form'),
    path('delete_booking_data/<int:id>/<int:row_id>', views.delete_booking_data, name='delete_booking_data'),

    #---------------------------------Payment CRUD

    path('payment_details/<int:id>', views.payment_details, name='payment_details'),
    path('add_payment/<int:id>', views.add_payment, name='add_payment'),
    path('edit_payment/<int:id>/<int:row_id>', views.edit_payment, name='edit_payment'),
    path('add_payment_form/<int:id>', views.add_payment_form, name='add_payment_form'),
    path('update_payment_form/<int:id>/<int:row_id>', views.update_payment_form, name='update_payment_form'),
    path('delete_payment_data/<int:id>/<int:row_id>', views.delete_payment_data, name='delete_payment_data'),

    #---------------------------------Equipment CRUD

    path('equipment_details/<int:id>', views.equipment_details, name='equipment_details'),
    path('add_equipment/<int:id>', views.add_equipment, name='add_equipment'),
    path('add_equipment_form/<int:id>', views.add_equipment_form, name='add_equipment_form'),
    path('edit_equipment/<int:id>/<int:row_id>', views.edit_equipment, name='edit_equipment'),
    path('update_equipment_form/<int:id>/<int:row_id>', views.update_equipment_form, name='update_equipment_form'),
    path('delete_equipment_data/<int:id>/<int:row_id>', views.delete_equipment_data, name='delete_equipment_data'),

    #---------------------------------Farmer CRUD
    
    path('farmer_details/<int:id>', views.farmer_details, name='farmer_details'),
    path('add_farmer/<int:id>', views.add_farmer, name='add_farmer'),
    path('add_farmer_form/<int:id>', views.add_farmer_form, name='add_farmer_form'),
    path('edit_farmer/<int:id>/<int:row_id>', views.edit_farmer, name='edit_farmer'),
    path('update_farmer_form/<int:id>/<int:row_id>', views.update_farmer_form, name='update_farmer_form'),
    path('delete_farmer_data/<int:id>/<int:row_id>', views.delete_farmer_data, name='delete_farmer_data'),

    #---------------------------------Vendor CRUD

    path('vendor_details/<int:id>', views.vendor_details, name='vendor_details'),
    path('add_vendor/<int:id>', views.add_vendor, name='add_vendor'),
    path('add_vendor_form/<int:id>', views.add_vendor_form, name='add_vendor_form'),
    path('edit_vendor/<int:id>/<int:row_id>', views.edit_vendor, name='edit_vendor'),
    path('update_vendor_form/<int:id>/<int:row_id>', views.update_vendor_form, name='update_vendor_form'),
    path('delete_vendor_data/<int:id>/<int:row_id>', views.delete_vendor_data, name='delete_vendor_data'),

    #---------------------------------Vehicle CRUD

    path('vehicle_details/<int:id>', views.vehicle_details, name='vehicle_details'),
    path('add_vehicle/<int:id>', views.add_vehicle, name='add_vehicle'),
    path('add_vehicle_form/<int:id>', views.add_vehicle_form, name='add_vehicle_form'),
    path('edit_vehicle/<int:id>/<int:row_id>', views.edit_vehicle, name='edit_vehicle'),
    path('update_vehicle_form/<int:id>/<int:row_id>', views.update_vehicle_form, name='update_vehicle_form'),
    path('delete_vehicle_data/<int:id>/<int:row_id>', views.delete_vehicle_data, name='delete_vehicle_data'),

    #---------------------------------Fertilizer CRUD

    path('fertilizer_details/<int:id>', views.fertilizer_details, name='fertilizer_details'),
    path('add_fertilizer/<int:id>', views.add_fertilizer, name='add_fertilizer'),
    path('add_fertilizer_form/<int:id>', views.add_fertilizer_form, name='add_fertilizer_form'),
    path('edit_fertilizer/<int:id>/<int:row_id>', views.edit_fertilizer, name='edit_fertilizer'),
    path('update_fertilizer_form/<int:id>/<int:row_id>', views.update_fertilizer_form, name='update_fertilizer_form'),
    path('delete_fertilizer_data/<int:id>/<int:row_id>', views.delete_fertilizer_data, name='delete_fertilizer_data'),

    #---------------------------------Pesticide CRUD

    path('pesticide_details/<int:id>', views.pesticide_details, name='pesticide_details'),
    path('add_pesticide/<int:id>', views.add_pesticide, name='add_pesticide'),
    path('add_pesticide_form/<int:id>', views.add_pesticide_form, name='add_pesticide_form'),
    path('edit_pesticide/<int:id>/<int:row_id>', views.edit_pesticide, name='edit_pesticide'),
    path('update_pesticide_form/<int:id>/<int:row_id>', views.update_pesticide_form, name='update_pesticide_form'),
    path('delete_pesticide_data/<int:id>/<int:row_id>', views.delete_pesticide_data, name='delete_pesticide_data'),



    path('contact_form', views.contact_form, name='contact_form'),
    path('signup_form', views.signup_form, name='signup_form'),
    path('signin_form', views.signin_form, name='signin_form'),
    path('logout', views.logout, name='logout'),
]

