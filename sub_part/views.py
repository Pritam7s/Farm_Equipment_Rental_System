import email
import re
from tracemalloc import take_snapshot
from urllib import request
from xml.etree.ElementTree import register_namespace
from django.shortcuts import render

from . models import contact_table, signup_table, add_equipment_table, add_farmer_table, add_vendor_table, add_vehicle_table, add_fertilizer_table, add_pesticide_table, add_feedback_table, add_cart_table, add_drive_table, add_report_table, add_payment_table, add_booking_table, add_land_table,add_charge_table, add_duration_table
from django.contrib import messages
from django.contrib import auth

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def dashboard(request, id):
    user_data=signup_table.objects.get(id=id)
    count_feedback=add_feedback_table.objects.filter(logger_id=id).count()
    count_report=add_report_table.objects.filter(logger_id=id).count()
    count_cart=add_cart_table.objects.filter(logger_id=id).count()
    count_drive=add_drive_table.objects.filter(logger_id=id).count()
    count_booking=add_booking_table.objects.filter(logger_id=id).count()
    count_payment=add_payment_table.objects.filter(logger_id=id).count()
    count_land=add_land_table.objects.filter(logger_id=id).count()
    count_equipment=add_equipment_table.objects.filter(logger_id=id).count()
    count_rent_charges=add_charge_table.objects.filter(logger_id=id).count()
    count_rent_duration=add_duration_table.objects.filter(logger_id=id).count()
    count_farmer=add_farmer_table.objects.filter(logger_id=id).count()
    count_vendor=add_vendor_table.objects.filter(logger_id=id).count()
    count_vehice=add_vehicle_table.objects.filter(logger_id=id).count()
    count_fertilizer=add_fertilizer_table.objects.filter(logger_id=id).count()
    count_pesticide=add_pesticide_table.objects.filter(logger_id=id).count()

    return render(request, 'dashboard.html', {'user_data': user_data , 'count_feedback' : count_feedback, 'count_report':count_report,'count_cart':count_cart, 'count_drive':count_drive, 
                            'count_payment':count_payment, 'count_booking':count_booking, 'count_land': count_land, 'count_equipment':count_equipment, 'count_rent_charges':count_rent_charges,
                            'count_rent_duration':count_rent_duration, 'count_farmer':count_farmer, 'count_vendor':count_vendor, 'count_vehice':count_vehice, 'count_fertilizer':count_fertilizer, 'count_pesticide':count_pesticide })

############################################----CART----#################################################################################

def cart_details(request,id):
    user_data=signup_table.objects.get(id=id)
    view_cart_data=add_cart_table.objects.filter(logger_id=id)
    return render(request, 'cart details.html', {'user_data': user_data, 'view_cart_data': view_cart_data})

def add_cart(request,id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add cart.html', {'user_data': user_data})

def add_cart_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_cart_table(item=request.POST.get('item'), 
                                cost=request.POST.get('cost'), 
                                quantity=request.POST.get('quantity'), 
                                price=request.POST.get('price'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_cart_data=add_cart_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Cart Successfully...", extra_tags="cart_success")
        return render(request, 'cart details.html', {'user_data' : user_data, 'view_cart_data' : view_cart_data})

def edit_cart(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_cart_table.objects.get(id=row_id)
    return render(request, 'edit cart.html', {'user_data': user_data, 'edit_data': edit_data})

def update_cart_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_cart_table.objects.get(id=row_id)
    ex=add_cart_table.objects.filter(id=row_id).update(item=request.POST.get('item'), 
                                                    cost=request.POST.get('cost'), 
                                                    quantity=request.POST.get('quantity'), 
                                                    price=request.POST.get('price'),
                                                    logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Cart Updated Successfully!", extra_tags="cart_success")
    view_cart_data=add_cart_table.objects.filter(logger_id=id)
    return render(request, 'cart details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_cart_data' : view_cart_data})

def delete_cart_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_cart_data=add_cart_table.objects.filter(logger_id=id)
    edit_data=add_cart_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Cart!", extra_tags="cart_success")
    return render(request, 'cart details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_cart_data' : view_cart_data})

###################################################----DRIVE----##########################################################################

def drive_details(request,id):
    user_data=signup_table.objects.get(id=id)
    view_drive_data=add_drive_table.objects.filter(logger_id=id)
    return render(request, 'drive details.html', {'user_data': user_data, 'view_drive_data': view_drive_data})

def add_drive(request,id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add drive.html', {'user_data': user_data})

def add_drive_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex2=add_drive_table(drive=request.POST.get('drive'), 
                            transaction=request.POST.get('transaction'), 
                            tid=request.POST.get('tid'), 
                            doc=request.POST.get('doc'),
                            address=request.POST.get('address'),
                            logger_id=request.POST.get('logger_id'))
        ex2.save()
        view_drive_data=add_drive_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Drive Successfully...", extra_tags="drive_success")
        return render(request, 'drive details.html', {'user_data' : user_data, 'view_drive_data' : view_drive_data})

def edit_drive(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_drive_table.objects.get(id=row_id)
    return render(request, 'edit drive.html', {'user_data': user_data, 'edit_data': edit_data})

def update_drive_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_drive_table.objects.get(id=row_id)
    ex=add_drive_table.objects.filter(id=row_id).update(drive=request.POST.get('drive'), 
                                                        transaction=request.POST.get('transaction'), 
                                                        tid=request.POST.get('tid'), 
                                                        doc=request.POST.get('doc'),
                                                        address=request.POST.get('address'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Drive Updated Successfully!", extra_tags="drive_success")
    view_drive_data=add_drive_table.objects.filter(logger_id=id)
    return render(request, 'drive details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_drive_data' : view_drive_data})

def delete_drive_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_drive_data=add_drive_table.objects.filter(logger_id=id)
    edit_data=add_drive_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Drive!", extra_tags="drive_success")
    return render(request, 'drive details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_drive_data' : view_drive_data})

####################################################----FEEDBACK----#########################################################################

def feedback(request, id):
    user_data=signup_table.objects.get(id=id)
    view_feedback_data=add_feedback_table.objects.filter(logger_id=id)
    return render(request, 'feedback.html', {'user_data': user_data, 'view_feedback_data' : view_feedback_data})

def add_feedback(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add feedback.html', {'user_data': user_data})

def add_feedback_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_feedback_table(date=request.POST.get('date'), 
                                rating=request.POST.get('rating'), 
                                name=request.POST.get('name'), 
                                description=request.POST.get('description'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_feedback_data=add_feedback_table.objects.filter(logger_id=id)
        messages.error(request, "Feedback Successfully Added...", extra_tags="feedback_success")
        return render(request, 'feedback.html', {'user_data' : user_data, 'view_feedback_data' : view_feedback_data})

def edit_feedback(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_feedback_table.objects.get(id=row_id)
    return render(request, 'edit feedback.html', {'user_data': user_data, 'edit_data': edit_data})

def update_feedback_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_feedback_table.objects.get(id=row_id)
    ex=add_feedback_table.objects.filter(id=row_id).update(date=request.POST.get('date'), 
                                                    rating=request.POST.get('rating'), 
                                                    name=request.POST.get('name'), 
                                                    description=request.POST.get('description'),
                                                    logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Feedback Updated Successfully!", extra_tags="feedback_success")
    view_feedback_data=add_feedback_table.objects.filter(logger_id=id)
    return render(request, 'feedback.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_feedback_data' : view_feedback_data})

def delete_feedback_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_feedback_data=add_feedback_table.objects.filter(logger_id=id)
    edit_data=add_feedback_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted the Feedback!", extra_tags="feedback_success")
    return render(request, 'feedback.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_feedback_data' : view_feedback_data})

####################################################----REPORT----#########################################################################

def report_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_report_data=add_report_table.objects.filter(logger_id=id)
    return render(request, 'report details.html', {'user_data': user_data, 'view_report_data': view_report_data})

def add_report(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add report.html', {'user_data': user_data})

def edit_report(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_report_table.objects.get(id=row_id)
    return render(request, 'edit report.html', {'user_data': user_data, 'edit_data':edit_data})

def add_report_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_report_table(date=request.POST.get('date'), 
                                type=request.POST.get('type'), 
                                description=request.POST.get('description'), 
                                status=request.POST.get('status'),
                                username=request.POST.get('username'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_report_data=add_report_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Report Successfully...", extra_tags="report_success")
        return render(request, 'report details.html', {'user_data' : user_data, 'view_report_data' : view_report_data})

def update_report_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_report_table.objects.get(id=row_id)
    ex=add_report_table.objects.filter(id=row_id).update(date=request.POST.get('date'), 
                                                        type=request.POST.get('type'), 
                                                        description=request.POST.get('description'), 
                                                        status=request.POST.get('status'),
                                                        username=request.POST.get('username'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Report Updated Successfully!", extra_tags="report_success")
    view_report_data=add_report_table.objects.filter(logger_id=id)
    return render(request, 'report details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_report_data' : view_report_data})

def delete_report_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_report_data=add_report_table.objects.filter(logger_id=id)
    edit_data=add_report_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Report!", extra_tags="report_success")
    return render(request, 'report details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_report_data' : view_report_data})

####################################################----BOOKNG----#########################################################################

def booking_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_booking_data=add_booking_table.objects.filter(logger_id=id)
    return render(request, 'booking details.html', {'user_data': user_data, 'view_booking_data': view_booking_data})

def add_booking(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add booking.html', {'user_data': user_data})

def edit_booking(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_booking_table.objects.get(id=row_id)
    return render(request, 'edit booking.html', {'user_data': user_data, 'edit_data':edit_data})

def add_booking_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_booking_table(pname=request.POST.get('pname'), 
                                pcode=request.POST.get('pcode'), 
                                customer=request.POST.get('customer'), 
                                pdate=request.POST.get('pdate'),
                                status=request.POST.get('status'),
                                tid=request.POST.get('tid'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_booking_data=add_booking_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Booking Successfully...", extra_tags="booking_success")
        return render(request, 'booking details.html', {'user_data' : user_data, 'view_booking_data' : view_booking_data})

def update_booking_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_booking_table.objects.get(id=row_id)
    ex=add_booking_table.objects.filter(id=row_id).update(pname=request.POST.get('pname'), 
                                pcode=request.POST.get('pcode'), 
                                customer=request.POST.get('customer'), 
                                pdate=request.POST.get('pdate'),
                                status=request.POST.get('status'),
                                tid=request.POST.get('tid'),
                                logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Booking Updated Successfully!", extra_tags="booking_success")
    view_booking_data=add_booking_table.objects.filter(logger_id=id)
    return render(request, 'booking details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_booking_data' : view_booking_data})

def delete_booking_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_booking_data=add_booking_table.objects.filter(logger_id=id)
    edit_data=add_booking_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Booking!", extra_tags="booking_success")
    return render(request, 'booking details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_booking_data' : view_booking_data})


######################################################----LAND----#######################################################################

def land_types(request,id):
    user_data=signup_table.objects.get(id=id)
    view_land_data=add_land_table.objects.filter(logger_id=id)
    return render(request, 'land types.html', {'user_data': user_data, 'view_land_data': view_land_data})

def add_land(request,id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add land.html', {'user_data': user_data})

def edit_land(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_land_table.objects.get(id=row_id)
    return render(request, 'edit land.html', {'user_data': user_data, 'edit_data':edit_data})

def add_land_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_land_table(ltype=request.POST.get('ltype'), 
                                cost=request.POST.get('cost'), 
                                benefits=request.POST.get('benefits'), 
                                drawbacks=request.POST.get('drawbacks'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_land_data=add_land_table.objects.filter(logger_id=id)
        messages.error(request, "Added to land Successfully...", extra_tags="land_success")
        return render(request, 'land types.html', {'user_data' : user_data, 'view_land_data' : view_land_data})

def update_land_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_land_table.objects.get(id=row_id)
    ex=add_land_table.objects.filter(id=row_id).update(ltype=request.POST.get('ltype'), 
                                cost=request.POST.get('cost'), 
                                benefits=request.POST.get('benefits'), 
                                drawbacks=request.POST.get('drawbacks'),
                                logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "land Updated Successfully!", extra_tags="land_success")
    view_land_data=add_land_table.objects.filter(logger_id=id)
    return render(request, 'land types.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_land_data' : view_land_data})

def delete_land_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_land_data=add_land_table.objects.filter(logger_id=id)
    edit_data=add_land_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from land!", extra_tags="land_success")
    return render(request, 'land types.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_land_data' : view_land_data})

#######################################################----CHARGES----######################################################################

def rent_charges(request,id):
    user_data=signup_table.objects.get(id=id)
    view_charge_data=add_charge_table.objects.filter(logger_id=id)
    return render(request, 'rent charges.html', {'user_data': user_data, 'view_charge_data': view_charge_data})

def add_charge(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add charge.html', {'user_data': user_data})

def edit_charge(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_charge_table.objects.get(id=row_id)
    return render(request, 'edit charge.html', {'user_data': user_data, 'edit_data':edit_data})

def add_charge_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_charge_table(ename=request.POST.get('ename'),
                                color=request.POST.get('color'),
                                price=request.POST.get('price'),
                                time=request.POST.get('time'),
                                total=request.POST.get('total'),
                                quantity=request.POST.get('quantity'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_charge_data=add_charge_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Rent Charges Successfully...", extra_tags="charge_success")
        return render(request, 'rent charges.html', {'user_data' : user_data, 'view_charge_data' : view_charge_data})

def update_charge_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_charge_table.objects.get(id=row_id)
    ex=add_charge_table.objects.filter(id=row_id).update(ename=request.POST.get('ename'),
                                                        color=request.POST.get('color'),
                                                        price=request.POST.get('price'),
                                                        time=request.POST.get('time'),
                                                        total=request.POST.get('total'),
                                                        quantity=request.POST.get('quantity'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Rent Charges Updated Successfully!", extra_tags="charge_success")
    view_charge_data=add_charge_table.objects.filter(logger_id=id)
    return render(request, 'rent charges.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_charge_data' : view_charge_data})

def delete_charge_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_charge_data=add_charge_table.objects.filter(logger_id=id)
    edit_data=add_charge_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Rent Charges!", extra_tags="charge_success")
    return render(request, 'rent charges.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_charge_data' : view_charge_data})


##########################################################----DURATION----###################################################################

def rent_duration(request,id):
    user_data=signup_table.objects.get(id=id)
    view_duration_data=add_duration_table.objects.filter(logger_id=id)
    return render(request, 'rent duration.html', {'user_data': user_data, 'view_duration_data': view_duration_data})

def add_duration(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add duration.html', {'user_data': user_data})

def edit_duration(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_duration_table.objects.get(id=row_id)
    return render(request, 'edit duration.html', {'user_data': user_data, 'edit_data':edit_data})

def add_duration_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_duration_table(ename=request.POST.get('ename'),
                                color=request.POST.get('color'),
                                price=request.POST.get('price'),
                                time=request.POST.get('time'),
                                total=request.POST.get('total'),
                                quantity=request.POST.get('quantity'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_duration_data=add_duration_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Rent duration Successfully...", extra_tags="duration_success")
        return render(request, 'rent duration.html', {'user_data' : user_data, 'view_duration_data' : view_duration_data})

def update_duration_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_duration_table.objects.get(id=row_id)
    ex=add_duration_table.objects.filter(id=row_id).update(ename=request.POST.get('ename'),
                                                        color=request.POST.get('color'),
                                                        price=request.POST.get('price'),
                                                        time=request.POST.get('time'),
                                                        total=request.POST.get('total'),
                                                        quantity=request.POST.get('quantity'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Rent Duration Updated Successfully!", extra_tags="duration_success")
    view_duration_data=add_duration_table.objects.filter(logger_id=id)
    return render(request, 'rent duration.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_duration_data' : view_duration_data})

def delete_duration_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_duration_data=add_duration_table.objects.filter(logger_id=id)
    edit_data=add_duration_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Rent Duration!", extra_tags="duration_success")
    return render(request, 'rent duration.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_duration_data' : view_duration_data})

###################################################----PAYMENT----##########################################################################

def payment_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_payment_data=add_payment_table.objects.filter(logger_id=id)
    return render(request, 'payment details.html', {'user_data': user_data, 'view_payment_data' : view_payment_data})

def add_payment(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add payment.html', {'user_data': user_data})

def add_payment_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_payment_table(name=request.POST.get('name'), 
                                crop=request.POST.get('crop'), 
                                cost=request.POST.get('cost'), 
                                date=request.POST.get('date'),
                                income=request.POST.get('income'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_payment_data=add_payment_table.objects.filter(logger_id=id)
        messages.error(request, "payment Successfully Added...", extra_tags="payment_success")
        return render(request, 'payment details.html', {'user_data' : user_data, 'view_payment_data' : view_payment_data})

def edit_payment(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_payment_table.objects.get(id=row_id)
    return render(request, 'edit payment.html', {'user_data': user_data, 'edit_data': edit_data})

def update_payment_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_payment_table.objects.get(id=row_id)
    ex=add_payment_table.objects.filter(id=row_id).update(name=request.POST.get('name'), 
                                                    crop=request.POST.get('crop'), 
                                                    cost=request.POST.get('cost'), 
                                                    date=request.POST.get('date'),
                                                    income=request.POST.get('income'),
                                                    logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "payment Updated Successfully!", extra_tags="payment_success")
    view_payment_data=add_payment_table.objects.filter(logger_id=id)
    return render(request, 'payment details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_payment_data' : view_payment_data})

def delete_payment_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_payment_data=add_payment_table.objects.filter(logger_id=id)
    edit_data=add_payment_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted the payment!", extra_tags="payment_success")
    return render(request, 'payment details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_payment_data' : view_payment_data})

####################################################----EQUIPMENT----#########################################################################

def equipment_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_equipment_data=add_equipment_table.objects.filter(logger_id=id)
    return render(request, 'equipment details.html', {'user_data': user_data, 'view_equipment_data': view_equipment_data})

def add_equipment(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add equipment.html', {'user_data': user_data})

def edit_equipment(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_equipment_table.objects.get(id=row_id)
    return render(request, 'edit equipment.html', {'user_data': user_data, 'edit_data':edit_data})

def add_equipment_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_equipment_table(ename=request.POST.get('ename'),
                                color=request.POST.get('color'),
                                price=request.POST.get('price'),
                                time=request.POST.get('time'),
                                total=request.POST.get('total'),
                                quantity=request.POST.get('quantity'),
                                logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_equipment_data=add_equipment_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Equipments Successfully...", extra_tags="equipment_success")
        return render(request, 'equipment details.html', {'user_data' : user_data, 'view_equipment_data' : view_equipment_data})

def update_equipment_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_equipment_table.objects.get(id=row_id)
    ex=add_equipment_table.objects.filter(id=row_id).update(ename=request.POST.get('ename'),
                                                        color=request.POST.get('color'),
                                                        price=request.POST.get('price'),
                                                        time=request.POST.get('time'),
                                                        total=request.POST.get('total'),
                                                        quantity=request.POST.get('quantity'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Equipments Updated Successfully!", extra_tags="equipment_success")
    view_equipment_data=add_equipment_table.objects.filter(logger_id=id)
    return render(request, 'equipment details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_equipment_data' : view_equipment_data})

def delete_equipment_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_equipment_data=add_equipment_table.objects.filter(logger_id=id)
    edit_data=add_equipment_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Equipments!", extra_tags="equipment_success")
    return render(request, 'equipment details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_equipment_data' : view_equipment_data})

#######################################################----FARMER----######################################################################

def farmer_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_farmer_data=add_farmer_table.objects.filter(logger_id=id)
    return render(request, 'farmer details.html', {'user_data': user_data, 'view_farmer_data': view_farmer_data})

def add_farmer(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add farmer.html', {'user_data': user_data})

def edit_farmer(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_farmer_table.objects.get(id=row_id)
    return render(request, 'edit farmer.html', {'user_data': user_data, 'edit_data':edit_data})

def add_farmer_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_farmer_table(fname=request.POST.get('fname'),
                            mobile=request.POST.get('mobile'),
                            adhar=request.POST.get('adhar'),
                            password=request.POST.get('password'),
                            address=request.POST.get('address'),
                            logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_farmer_data=add_farmer_table.objects.filter(logger_id=id)
        messages.error(request, "Added to farmers Successfully...", extra_tags="farmer_success")
        return render(request, 'farmer details.html', {'user_data' : user_data, 'view_farmer_data' : view_farmer_data})

def update_farmer_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_farmer_table.objects.get(id=row_id)
    ex=add_farmer_table.objects.filter(id=row_id).update(fname=request.POST.get('fname'),
                                                        mobile=request.POST.get('mobile'),
                                                        adhar=request.POST.get('adhar'),
                                                        password=request.POST.get('password'),
                                                        address=request.POST.get('address'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "farmers Updated Successfully!", extra_tags="farmer_success")
    view_farmer_data=add_farmer_table.objects.filter(logger_id=id)
    return render(request, 'farmer details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_farmer_data' : view_farmer_data})

def delete_farmer_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_farmer_data=add_farmer_table.objects.filter(logger_id=id)
    edit_data=add_farmer_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from farmers!", extra_tags="farmer_success")
    return render(request, 'farmer details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_farmer_data' : view_farmer_data})

########################################################----VENDOR----#####################################################################

def vendor_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_vendor_data=add_vendor_table.objects.filter(logger_id=id)
    return render(request, 'vendor details.html', {'user_data': user_data, 'view_vendor_data': view_vendor_data})

def add_vendor(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add vendor.html', {'user_data': user_data})

def edit_vendor(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_vendor_table.objects.get(id=row_id)
    return render(request, 'edit vendor.html', {'user_data': user_data, 'edit_data':edit_data})

def add_vendor_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_vendor_table(vname=request.POST.get('vname'),
                            contact=request.POST.get('contact'),
                            vid=request.POST.get('vid'),
                            location=request.POST.get('location'),
                            adhar=request.POST.get('adhar'),
                            logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_vendor_data=add_vendor_table.objects.filter(logger_id=id)
        messages.error(request, "Added to vendors Successfully...", extra_tags="vendor_success")
        return render(request, 'vendor details.html', {'user_data' : user_data, 'view_vendor_data' : view_vendor_data})

def update_vendor_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_vendor_table.objects.get(id=row_id)
    ex=add_vendor_table.objects.filter(id=row_id).update(vname=request.POST.get('vname'),
                                                        contact=request.POST.get('contact'),
                                                        vid=request.POST.get('vid'),
                                                        location=request.POST.get('location'),
                                                        adhar=request.POST.get('adhar'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "vendors Updated Successfully!", extra_tags="vendor_success")
    view_vendor_data=add_vendor_table.objects.filter(logger_id=id)
    return render(request, 'vendor details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_vendor_data' : view_vendor_data})

def delete_vendor_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_vendor_data=add_vendor_table.objects.filter(logger_id=id)
    edit_data=add_vendor_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from vendors!", extra_tags="vendor_success")
    return render(request, 'vendor details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_vendor_data' : view_vendor_data})

#########################################################----VEHICLE----####################################################################

def vehicle_details(request,id):
    user_data=signup_table.objects.get(id=id)
    return render(request,'vehicle details.html', {'user_data': user_data})

def add_vehicle(request):
    return render(request,'add vehicle.html')

def edit_vehicle(request):
    return render(request,'edit vehicle.html')


def vehicle_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_vehicle_data=add_vehicle_table.objects.filter(logger_id=id)
    return render(request, 'vehicle details.html', {'user_data': user_data, 'view_vehicle_data': view_vehicle_data})

def add_vehicle(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add vehicle.html', {'user_data': user_data})

def edit_vehicle(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_vehicle_table.objects.get(id=row_id)
    return render(request, 'edit vehicle.html', {'user_data': user_data, 'edit_data':edit_data})

def add_vehicle_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_vehicle_table(vname=request.POST.get('vname'),
                            color=request.POST.get('color'),
                            rent=request.POST.get('rent'),
                            condition=request.POST.get('condition'),
                            company=request.POST.get('company'),
                            logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_vehicle_data=add_vehicle_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Vehicles Successfully...", extra_tags="vehicle_success")
        return render(request, 'vehicle details.html', {'user_data' : user_data, 'view_vehicle_data' : view_vehicle_data})

def update_vehicle_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_vehicle_table.objects.get(id=row_id)
    ex=add_vehicle_table.objects.filter(id=row_id).update(vname=request.POST.get('vname'),
                                                            color=request.POST.get('color'),
                                                            rent=request.POST.get('rent'),
                                                            condition=request.POST.get('condition'),
                                                            company=request.POST.get('company'),
                                                            logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Vehicles Updated Successfully!", extra_tags="vehicle_success")
    view_vehicle_data=add_vehicle_table.objects.filter(logger_id=id)
    return render(request, 'vehicle details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_vehicle_data' : view_vehicle_data})

def delete_vehicle_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_vehicle_data=add_vehicle_table.objects.filter(logger_id=id)
    edit_data=add_vehicle_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Vehicles!", extra_tags="vehicle_success")
    return render(request, 'vehicle details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_vehicle_data' : view_vehicle_data})

######################################################----FERTILIZER----#######################################################################

def fertilizer_details(request,id):
    user_data=signup_table.objects.get(id=id)
    return render(request,'fertilizer details.html', {'user_data': user_data})

def add_fertilizer(request):
    return render(request,'add fertilizer.html')

def edit_fertilizer(request):
    return render(request,'edit fertilizer.html')


def fertilizer_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_fertilizer_data=add_fertilizer_table.objects.filter(logger_id=id)
    return render(request, 'fertilizer details.html', {'user_data': user_data, 'view_fertilizer_data': view_fertilizer_data})

def add_fertilizer(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add fertilizer.html', {'user_data': user_data})

def edit_fertilizer(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_fertilizer_table.objects.get(id=row_id)
    return render(request, 'edit fertilizer.html', {'user_data': user_data, 'edit_data':edit_data})

def add_fertilizer_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_fertilizer_table(fname=request.POST.get('fname'),
                                supplier=request.POST.get('supplier'),
                                weight=request.POST.get('weight'),
                                price=request.POST.get('price'),
                                company=request.POST.get('company'),
                            logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_fertilizer_data=add_fertilizer_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Fertilizers Successfully...", extra_tags="fertilizer_success")
        return render(request, 'fertilizer details.html', {'user_data' : user_data, 'view_fertilizer_data' : view_fertilizer_data})

def update_fertilizer_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_fertilizer_table.objects.get(id=row_id)
    ex=add_fertilizer_table.objects.filter(id=row_id).update(fname=request.POST.get('fname'),
                                                        supplier=request.POST.get('supplier'),
                                                        weight=request.POST.get('weight'),
                                                        price=request.POST.get('price'),
                                                        company=request.POST.get('company'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Fertilizers Updated Successfully!", extra_tags="fertilizer_success")
    view_fertilizer_data=add_fertilizer_table.objects.filter(logger_id=id)
    return render(request, 'fertilizer details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_fertilizer_data' : view_fertilizer_data})

def delete_fertilizer_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_fertilizer_data=add_fertilizer_table.objects.filter(logger_id=id)
    edit_data=add_fertilizer_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Fertilizers!", extra_tags="fertilizer_success")
    return render(request, 'fertilizer details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_fertilizer_data' : view_fertilizer_data})

########################################################----PESTICIDE----#####################################################################

def pesticide_details(request,id):
    user_data=signup_table.objects.get(id=id)
    return render(request,'pesticide details.html', {'user_data': user_data})

def add_pesticide(request):
    return render(request,'add pesticide.html')

def edit_pesticide(request):
    return render(request,'edit pesticide.html')


def pesticide_details(request, id):
    user_data=signup_table.objects.get(id=id)
    view_pesticide_data=add_pesticide_table.objects.filter(logger_id=id)
    return render(request, 'pesticide details.html', {'user_data': user_data, 'view_pesticide_data': view_pesticide_data})

def add_pesticide(request, id):
    user_data=signup_table.objects.get(id=id)
    return render(request, 'add pesticide.html', {'user_data': user_data})

def edit_pesticide(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_pesticide_table.objects.get(id=row_id)
    return render(request, 'edit pesticide.html', {'user_data': user_data, 'edit_data':edit_data})

def add_pesticide_form(request, id):
    user_data=signup_table.objects.get(id=id)
    if request.method=='POST':
        ex1=add_pesticide_table(pname=request.POST.get('pname'),
                                supplier=request.POST.get('supplier'),
                                weight=request.POST.get('weight'),
                                price=request.POST.get('price'),
                                company=request.POST.get('company'),
                            logger_id=request.POST.get('logger_id'))
        ex1.save()
        view_pesticide_data=add_pesticide_table.objects.filter(logger_id=id)
        messages.error(request, "Added to Pesticides Successfully...", extra_tags="pesticide_success")
        return render(request, 'pesticide details.html', {'user_data' : user_data, 'view_pesticide_data' : view_pesticide_data})

def update_pesticide_form(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    edit_data=add_pesticide_table.objects.get(id=row_id)
    ex=add_pesticide_table.objects.filter(id=row_id).update(pname=request.POST.get('pname'),
                                                        supplier=request.POST.get('supplier'),
                                                        weight=request.POST.get('weight'),
                                                        price=request.POST.get('price'),
                                                        company=request.POST.get('company'),
                                                        logger_id=request.POST.get('logger_id'))
    print("Successfully Updated")
    messages.error(request, "Pesticides Updated Successfully!", extra_tags="pesticide_success")
    view_pesticide_data=add_pesticide_table.objects.filter(logger_id=id)
    return render(request, 'pesticide details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_pesticide_data' : view_pesticide_data})

def delete_pesticide_data(request, id, row_id):
    user_data=signup_table.objects.get(id=id)
    view_pesticide_data=add_pesticide_table.objects.filter(logger_id=id)
    edit_data=add_pesticide_table.objects.get(id=row_id)
    edit_data.delete()
    print("Successfully Deleted the Data.........")
    messages.error(request,"Successfully Deleted from Pesticides!", extra_tags="pesticide_success")
    return render(request, 'pesticide details.html', {'edit_data': edit_data, 'user_data' : user_data, 'view_pesticide_data' : view_pesticide_data})

##########################################################----CONTACT[Index]----###################################################################




def contact_form(request):
    if request.method=='POST':
        if contact_table.objects.filter(email=request.POST.get('email'), phone=request.POST.get('phone')):
            messages.error(request, 'Already Received Your Response with same Email Address & Phone Number', extra_tags='exist')
            return render(request, 'contact.html')
        elif contact_table.objects.filter(phone=request.POST.get('phone')):
            messages.error(request,'Already Received Your Resposnse with same Phone number', extra_tags='exist')
            return render(request, 'contact.html')
        elif contact_table.objects.filter(email=request.POST.get('email')):
            messages.error(request, 'Already Receieved Your Response with same Email Address', extra_tags='exist')
            return render(request, 'contact.html')
        else:
            ex1=contact_table(name=request.POST.get('name'), email=request.POST.get('email'), phone=request.POST.get('phone'), message=request.POST.get('message'))
            ex1.save()
            messages.error(request, 'Saved Successfully', extra_tags='saved')
            return render(request, 'contact.html')
    else:
          return render(request, 'contact.html')

###################################################----LOGIN/REGISTER/LOGOUT----###############################################################

def signup_form(request):
    if request.method=="POST":
        if signup_table.objects.filter(email=request.POST.get('email'), username=request.POST.get('username')).exists():
            messages.error(request, 'Already Exist Email & Username', extra_tags='exist')
            return render(request, 'login.html')
        elif signup_table.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request, 'Email Already Exist.', extra_tags='exist')
            return render(request, 'login.html')
        elif signup_table.objects.filter(username=request.POST.get('username')).exists():
            messages.error(request, 'Username Already Exist', extra_tags='exist')
            return render(request, 'login.html')
        else:
            temp=signup_table(username=request.POST.get('username'),
                            email=request.POST.get('email'),
                            password=request.POST.get('password'))
            if len(request.FILES) != 0:
                temp.picture = request.FILES.get('picture')
            temp.save()
            
            # uname=request.POST.get('username')
            # mail=request.POST.get('email')
            # subject='Welcome To AGRARYANS World.'
            # message=f'Hi {uname}, Thank You for Registering.'
            # email_form= settings.EMAIL_HOST_USER
            # recipient_list= [mail,]
            # send_mail(subject,message,email_form,recipient_list)
            # print("Email Successfully Sent..............")


            messages.error(request, 'Registered Susscessfully', extra_tags='registered')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


# def signin_form(request):
# 		if request.method=="POST":
# 			if signup_table.objects.filter(email=request.POST.get('email'),password=request.POST.get('password')).exists():
# 				ex1=signup_table.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
#                 # take_email = ex1.email
#                 # print(take_email)
#                 # user_data=signup_table.objects.get(email=take_email)
#                 # request.session ['email'] = ex1.email
#                 # return render(request,'dashboard.html', {'user_data' : user_data})
# 			else:
# 				messages.error(request, 'Invalid Email or Password', extra_tags='invalid')
# 				return render(request,'login.html')
# 		else:
# 			return render(request,'login.html')

# def logout(request):
#     auth.logout(request)
#     #request.session.clear() 
#     return render(request, 'login.html')

def signin_form (request):
    if request.method=="POST":
        if signup_table.objects.filter(email=request.POST.get('email'), password=request.POST.get('password')).exists():
            ex1=signup_table.objects.get(email=request.POST.get('email'),password=request.POST.get('password'))
            take_email=ex1.email
            take_id=ex1.id
            print(take_email)
            request.session['email']=ex1.email
            user_data=signup_table.objects.get(email=take_email)
            count_equipment=add_equipment_table.objects.filter(logger_id=take_id).count()
            count_farmer=add_farmer_table.objects.filter(logger_id=take_id).count()
            count_vendor=add_vendor_table.objects.filter(logger_id=take_id).count()
            count_land=add_land_table.objects.filter(logger_id=take_id).count()
            count_rent_charges=add_charge_table.objects.filter(logger_id=take_id).count()
            count_rent_duration=add_duration_table.objects.filter(logger_id=take_id).count()
            count_booking=add_booking_table.objects.filter(logger_id=take_id).count()
            
            count_payment=add_payment_table.objects.filter(logger_id=take_id).count()
            count_vehice=add_vehicle_table.objects.filter(logger_id=take_id).count()
            count_fertilizer=add_fertilizer_table.objects.filter(logger_id=take_id).count()
            count_pesticide=add_pesticide_table.objects.filter(logger_id=take_id).count()
            
            count_feedback=add_feedback_table.objects.filter(logger_id=take_id).count()
            count_report=add_report_table.objects.filter(logger_id=take_id).count()
            count_cart=add_cart_table.objects.filter(logger_id=take_id).count()
            count_drive=add_drive_table.objects.filter(logger_id=take_id).count()
            return render(request,'dashboard.html', {'user_data' : user_data, 'count_equipment' : count_equipment, 'count_pesticide':count_pesticide, 'count_fertilizer':count_fertilizer, 'count_vehice':count_vehice, 'count_payment':count_payment, 'count_booking':count_booking, 'count_rent_duration': count_rent_duration, 'count_rent_charges': count_rent_charges, 'count_land' : count_land, 'count_farmer' : count_farmer, 'count_vendor': count_vendor, 'count_feedback' : count_feedback, 'count_report':count_report, 'count_cart':count_cart, 'count_drive':count_drive})
        else:
            messages.error(request, 'Invalid Email or Password', extra_tags='invalid')
            return render(request,'login.html')
    else:
        return render(request, 'login.html')
    
#############################################################################################################################

def logout(request):
    request.session.clear()
    return render(request, 'login.html')