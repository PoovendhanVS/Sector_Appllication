from pyexpat.errors import messages
from django.shortcuts import render






from datetime import date
import datetime
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import AccessoriesModel, Country, District, Invoice_Details, ItemModel, ProductsModel, State, dashbd, mainBill , masterPage, typeCreate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import random

from django.core.paginator import Paginator

from django.views.generic import View
from .utils import render_to_pdf




# Create your views here.

# from management.models import dashbd

from django.contrib.auth.decorators import login_required
# # Create your views here.


def signin(request):
    request.session.flush()
    if request.method == "POST":
        log_name = request.session['uname'] = request.POST.get('uname','')
        log_pwd = request.session['psw'] = request.POST.get('psw','')
        if log_name != '' and log_pwd != '':
            check_data = dashbd.objects.filter(name=log_name, password=log_pwd).first()
            if check_data:
                return render(request,'admin_page.html')
            else:
                messages.error(request,'Invalid user name and password')
        else:
            messages.error(request,'Please enter user name and password')
    return render(request, 'sign_in.html')

def logout(request):
    if 'uname' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return HttpResponse('Somethings falut')
def home(request):
    user_name = request.POST.get('uname', '')
    user_email = request.POST.get('mail', '')
    user_pwd = request.POST.get('psw', '')

    if user_name != '' and user_email != '' and user_pwd != '':
        create_data = dashbd.objects.create(name=user_name, email=user_email, password=user_pwd)
        if create_data:
            return redirect('/users_list')
        else:
            return HttpResponse('Fail')
    return render(request, 'index.html')
    
def admin_board(request):
    if 'uname' in request.session:
        name = request.session.get('uname')
        return render(request, 'admin_page.html', {'name':name})
    else:
        return redirect('/')

def admin_usage(request):
    return render(request,'admin_usage.html')

def user(request):
    if 'uname' in request.session:
        return render(request,'users_page.html')
    else:
        return redirect('/')

def users_list(request):
    name = request.session.get('uname')
    if 'uname' in request.session:
        user_list = dashbd.objects.all().values
        return render(request,'users_list.html',{'user_list':user_list,'name':name})
    else:
        return redirect('/')

def update_user_page(request,id):
    if 'uname' in request.session:
        user_update = dashbd.objects.get(id=id)
        if request.method == "POST":
            user_name = request.POST.get('uname','')
            user_mail = request.POST.get('mail','')
            user_pwd = request.POST.get('psw','')
            if user_name != '':
                user_update.name = user_name
                user_update.email = user_mail
                user_update.password = user_pwd
                user_update.save()
                return redirect('/users_list')
            else:
                return render('/update_user_page')

        return render(request,'update_user_page.html', {'user_update':user_update})
    else:
        return redirect('/')

def del_user_list(request,id):
    user_del = dashbd.objects.get(id=id)
    if user_del:
        user_del.delete()
        return redirect('/users_list')
    return render(request,'users_list.html')

def master(request):
    if 'uname' in request.session:
        fetchall = masterPage.objects.all().values
        return render(request,'master.html',{'fetchall' : fetchall})
    else:
        return redirect('/')

def master_header_link(request):
    if 'uname' in request.session:
        bio_id = random.randint(124,999)
        if request.method == "POST":
            emp_gender = request.POST.get('emp_gender','')
            emp_name = request.POST.get('offici_emp_name','')
            date_of_join = request.POST.get('join_date','')
            role = request.POST.get('role','')
            site_name = request.POST.get('site_name','')
            emp_shift = request.POST.get('gst','')
            emp_cate = request.POST.get('emp_cate','')
            emp_bio = request.POST.get('bio_id','')
            emp_head = request.POST.get('emp_staff_hd','')
            emp_skill = request.POST.getlist('emp_skill')
            
            emp_photo = request.FILES['emp_photos']
            
            emp_martial = request.POST.get('emp_status', '')
            emp_dob = request.POST.get('dob', '')
            emp_age = request.POST.get('emp_age', '')
            emp_blood_grp = request.POST.get('emp_blood', '')
            emp_p_gender = request.POST.get('gender', '')
            emp_activities = request.POST.get('emp_act', '')
            emp_disability = request.POST.get('emp_pys', '')
            emp_country = request.POST.get('emp_countrys', '')
            emp_state = request.POST.get('emp_states', '')
            emp_district = request.POST.get('emp_district', '')
            emp_buildno = request.POST.get('emp_bild', '')
            emp_street = request.POST.get('emp_street', '')
            emp_area = request.POST.get('emp_area', '')
            emp_pincode = request.POST.get('emp_pin', '')
            emp_p_country = request.POST.get('emp_p_countrys', '')
            emp_p_state = request.POST.get('emp_p_states', '')
            emp_p_district = request.POST.get('emp_p_districts', '')
            emp_p_buildno = request.POST.get('emp_p_bild', '')
            emp_p_street = request.POST.get('emp_p_street', '')
            emp_p_area = request.POST.get('emp_p_area', '')
            emp_p_pincode = request.POST.get('emp_p_pin', '')

            if request.method == "POST":

                create_data = masterPage.objects.create(emp_gender=emp_gender, emp_name=emp_name, date_of_join=date_of_join,
                                            role=role,site_name=site_name,emp_shift=emp_shift,emp_cate=emp_cate,
                                            emp_bio=emp_bio,emp_head=emp_head,emp_skill=emp_skill,emp_img=emp_photo,
                    martial=emp_martial, date_of_birth=emp_dob, emp_age=emp_age,
                    blood_grp=emp_blood_grp, gender=emp_p_gender, activities=emp_activities, disability=emp_disability,
                    emp_country=emp_country, emp_state=emp_state, emp_district=emp_district, buliding_no=emp_buildno,
                    emp_street=emp_street, emp_area=emp_area, emp_pincode=emp_pincode, emp_p_country=emp_p_country,
                    emp_p_state=emp_p_state, emp_p_district=emp_p_district, p_buliding_no=emp_p_buildno,
                    emp_p_street=emp_p_street, emp_p_area=emp_p_area, emp_p_pincode=emp_p_pincode)
                
                messages.success(request, 'Employee official details stored successfully.')
            else:
                return HttpResponse('KeyError')
        context = {
            'bio_id' : bio_id,
            'gender' : ['Mr','Ms'],
            'full_gender' : ['Male','Female','Others'],
            'site_names' : ["R K Steel Manufacturing & Co Pvt. Ltd","Newton reserch organisation","Libird international Corparation","Standford brack IT Solution","Macknock Techno Private Limitted"],
            # 'working_shifts' : ["Morning Shift","Afternoon Shift","Night Shift"],
            'companies' : ["R K Steel Manufacturing & Co Pvt. Ltd","Newton reserch organisation","Libird international Corparation","Standford brack IT Solution","Macknock Techno Private Limitted"],
            'employee_categories' : ["Full-time","Part-time","Hybrid"],
            'head' : ["Manager","HR Department","HR Deployment","Admin Staff","Supervisor"],
            'skill' : ["Frontend Development","Backend Development","Full Stack Development","UI/UX","Newtworking","Administration","Business"],
            'm_status' : ['Married', 'Un-Married', 'Divorced'],
            'blood_grp' : ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
            'emp_physical' : ['None', 'Blindness','Low-vision','Leprosy Cured Persons',
                            'Hearing Impairment','Locomotor Disability','Dwarfism',
                            'Intellectual Disability','Mental Illness'],
            'countrys' : ['India'],
            'states' : ['Tamil Nadu'],
            'districts' :['Ariyalur','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode','Kancheepuram','Kanniyakumari',
                        'Karur','Krishnagiri','Madurai','Nagapattinam','Namakkal','Perambalur','Pudukkottai','Ramanathapuram',
                        'Salem','Sivaganga','Thanjavur','The Nilgiris','Theni','Thiruvallur','Thiruvarur','Thoothukkudi',
                        'Tiruchirappalli','Tirunelveli','Tiruppur','Tiruvannamalai','Vellore','Viluppuram','Virudhunagar']
        
        }
        return render(request,'master_header_link.html',context)
    else:
        return redirect('/')


def emp_official(request):
    bio_id = random.randint(124,999)
    if request.method == "POST":
        emp_gender = request.POST.get('gender','')
        emp_name = request.POST.get('emp_name','')
        date_of_join = request.POST.get('join_date','')
        role = request.POST.get('role','')
        site_name = request.POST.get('site_name','')
        emp_shift = request.POST.get('emp_shift','')
        emp_cate = request.POST.get('emp_cate','')
        emp_bio = request.POST.get('bio_id','')
        emp_head = request.POST.get('emp_staff-hd','')
        emp_skill = request.POST.getlist('emp_skill')
        
        emp_photo = request.FILES['emp_photos']

        # if emp_gender != '' and emp_name != '' and date_of_join != '' and role != '' and site_name != '' and emp_shift != '' and  emp_cate != '' and emp_head != '' and emp_skill != '' and emp_photo != '':

        #     create_data = offic_emp_det.objects.create(emp_gender=emp_gender, emp_name=emp_name, date_of_join=date_of_join,
        #                                 role=role,site_name=site_name,emp_shift=emp_shift,emp_cate=emp_cate,
        #                                 emp_bio=emp_bio,emp_head=emp_head,emp_skill=emp_skill,emp_img=emp_photo)
        # else:
        #     return HttpResponse(KeyError)
    context = {
        'bio_id' : bio_id,
        'gender' : ['Mr','Mrs'],
        'site_names' : ["Company A","Company B","Company C","Company D","Company E"],
        'working_shifts' : ["Morning Shift","Afternoon Shift","Night Shift"],
        'employee_categories' : ["Full-time","Part-time","Contract","Temporary","Intern","Freelancer"],
        'head' : ["Head A","Head B","Head C","Head D","Head E"],
        'skill' : ["skill A","skill B","skill C","skill D","skill E"],
    }

    return render(request,'emp_official.html',context)

def update_emp_official(request, id):
    if 'uname' in request.session:
        data = masterPage.objects.get(id=id)
        if request.method == "POST":
            emp_gender = request.POST.get('emp_gender', '')
            emp_name = request.POST.get('emp_name', '')
            date_of_join = request.POST.get('join_date', '')
            role = request.POST.get('role', '')
            site_name = request.POST.get('site_name', '')
            emp_shift = request.POST.get('gst', '')
            emp_cate = request.POST.get('emp_cate', '')
            emp_bio = request.POST.get('bio_id', '')
            emp_head = request.POST.get('emp_staff-hd', '')
            emp_skill = request.POST.getlist('emp_skill')
            
            emp_skill = request.POST.getlist('emp_skill')

            emp_photos = request.FILES.get('emp_p_photos')
            emp_name = request.POST.get('emp_name', '')

            emp_martial = request.POST.get('emp_status', '')
            emp_dob = request.POST.get('dob', '')
            emp_age = request.POST.get('emp_age', '')
            emp_blood_grp = request.POST.get('emp_blood', '')
            gender = request.POST.get('gender', '')
            emp_activities = request.POST.get('emp_act', '')
            emp_disability = request.POST.get('emp_pys', '')
            emp_country = request.POST.get('emp_countrys', '')
            emp_state = request.POST.get('emp_states', '')
            emp_district = request.POST.get('emp_district', '')
            emp_buildno = request.POST.get('emp_bild', '')
            emp_street = request.POST.get('emp_street', '')
            emp_area = request.POST.get('emp_area', '')
            emp_pincode = request.POST.get('emp_pin', '')
            emp_p_country = request.POST.get('emp_p_countrys', '')
            emp_p_state = request.POST.get('emp_p_states', '')
            emp_p_district = request.POST.get('emp_p_districts', '')
            emp_p_buildno = request.POST.get('emp_p_bild', '')
            emp_p_street = request.POST.get('emp_p_street', '')
            emp_p_area = request.POST.get('emp_p_area', '')
            emp_p_pincode = request.POST.get('emp_p_pin', '')

            if request.method == "POST":
                data.emp_gender = emp_gender
                data.emp_name = emp_name
                data.date_of_join = date_of_join
                data.role = role
                data.site_name = site_name
                data.emp_shift = emp_shift
                data.emp_cate = emp_cate
                data.emp_bio = emp_bio
                data.emp_head = emp_head
                data.emp_skill = emp_skill
                if emp_photos:
                    data.emp_img.delete(save=False)
                    data.emp_img = emp_photos

                
                data.martial = emp_martial
                data.date_of_birth = emp_dob
                data.emp_age = emp_age
                data.blood_grp = emp_blood_grp
                data.gender = gender
                data.activities = emp_activities
                data.disability = emp_disability
                data.emp_country = emp_country
                data.emp_state = emp_state
                data.emp_district = emp_district
                data.buliding_no = emp_buildno
                data.emp_street = emp_street
                data.emp_area = emp_area
                data.emp_pincode = emp_pincode
                data.emp_p_country = emp_p_country
                data.emp_p_state = emp_p_state
                data.emp_p_district = emp_p_district
                data.p_buliding_no = emp_p_buildno
                data.emp_p_street = emp_p_street
                data.emp_p_area = emp_p_area
                data.emp_p_pincode = emp_p_pincode

                data.save()

                return redirect('/master')
            else:
                messages.success(request, 'Something error.')

        context = {
            'gender' : ['Mr','Ms'],
            'full_gender' : ['Male','Female','Others'],
            'site_names' : ["R K Steel Manufacturing & Co Pvt. Ltd","Newton reserch organisation","Libird international Corparation","Standford brack IT Solution","Macknock Techno Private Limitted"],
            # 'working_shifts' : ["Morning Shift","Afternoon Shift","Night Shift"],
            'employee_categories' : ["Full-time","Part-time","Hybrid"],
            'head' : ["Manager","HR Department","HR Deployment","Admin Staff","Supervisor"],
            'skill' : ["Frontend Development","Backend Development","Full Stack Development","UI/UX","Newtworking","Administration","Business"],
            'm_status' : ['Married', 'Un-Married', 'Divorced'],
            'blood_grp' : ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
            'emp_physical' : ['None', 'Blindness','Low-vision','Leprosy Cured Persons',
                            'Hearing Impairment','Locomotor Disability','Dwarfism',
                            'Intellectual Disability','Mental Illness'],
            'countrys' : ['India'],
            'states' : ['Andhra Pradesh', 'Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa',
                    'Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra',
                    'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim', 'Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','Gairsain','West Bengal'],
            'districts' :['Ariyalur','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode','Kancheepuram','Kanniyakumari',
                        'Karur','Krishnagiri','Madurai','Nagapattinam','Namakkal','Perambalur','Pudukkottai','Ramanathapuram',
                        'Salem','Sivaganga','Thanjavur','The Nilgiris','Theni','Thiruvallur','Thiruvarur','Thoothukkudi',
                        'Tiruchirappalli','Tirunelveli','Tiruppur','Tiruvannamalai','Vellore','Viluppuram','Virudhunagar'],
        
        
            'data': data
        }

        return render(request, 'update_emp_offic.html', context)
    else:
        return redirect('/')

def del_emp_dte(request, id):
    if 'uname' in request.session:
        del_emp_details = masterPage.objects.filter(id=id).first()
        if del_emp_details:
            del_emp_details.delete()
            return redirect('/master')
        return render(request,'master.html')
    else:
        return redirect('/')

# def emp_personal(request):
#     fetchall = personal_emp_det.objects.all().values
#     return render(request,'emp_personal.html',{'fetchall': fetchall})

def add_emp_personal(request):
    if request.method == "POST":
        emp_name = request.POST.get('emp_name', '')
        emp_martial = request.POST.get('emp_status', '')
        emp_dob = request.POST.get('dob', '')
        emp_age = request.POST.get('emp_age', '')
        emp_blood_grp = request.POST.get('emp_blood', '')
        emp_gender = request.POST.get('gender', '')
        emp_activities = request.POST.get('emp_act', '')
        emp_disability = request.POST.get('emp_pys', '')
        emp_country = request.POST.get('emp_countrys', '')
        emp_state = request.POST.get('emp_states', '')
        emp_district = request.POST.get('emp_district', '')
        emp_buildno = request.POST.get('emp_bild', '')
        emp_street = request.POST.get('emp_street', '')
        emp_area = request.POST.get('emp_area', '')
        emp_pincode = request.POST.get('emp_pin', '')
        emp_p_country = request.POST.get('emp_p_countrys', '')
        emp_p_state = request.POST.get('emp_p_states', '')
        emp_p_district = request.POST.get('emp_p_districts', '')
        emp_p_buildno = request.POST.get('emp_p_bild', '')
        emp_p_street = request.POST.get('emp_p_street', '')
        emp_p_area = request.POST.get('emp_p_area', '')
        emp_p_pincode = request.POST.get('emp_p_pin', '')

        # if emp_name != '' and emp_martial != '' and emp_dob != '' and emp_age != '' and emp_blood_grp != '' and emp_gender != '' and emp_activities != '' and emp_disability != '' and emp_country != '' and emp_state != '' and emp_district != '' and emp_buildno != '' and emp_street != '' and emp_area != '' and emp_pincode != ''and emp_p_country != '' and emp_p_state != '' and emp_p_district != '' and emp_p_buildno != '' and emp_p_street != '' and emp_p_area != '' and emp_p_pincode != '':
        #     create_data = personal_emp_det.objects.create(
        #         emp_name=emp_name, martial=emp_martial, date_of_birth=emp_dob, emp_age=emp_age,
        #         blood_grp=emp_blood_grp, gender=emp_gender, activities=emp_activities, disability=emp_disability,
        #         emp_country=emp_country, emp_state=emp_state, emp_district=emp_district, buliding_no=emp_buildno,
        #         emp_street=emp_street, emp_area=emp_area, emp_pincode=emp_pincode, emp_p_country=emp_p_country,
        #         emp_p_state=emp_p_state, emp_p_district=emp_p_district, p_buliding_no=emp_p_buildno,
        #         emp_p_street=emp_p_street, emp_p_area=emp_p_area, emp_p_pincode=emp_p_pincode
        #     )
        #     messages.success(request, 'Employee personal details stored successfully.')

    context = {
        'gender' : ['Male','Female', 'Other'],
        'm_status' : ['Married', 'Un-Married', 'Divorced'],
        'blood_grp' : ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
        'emp_physical' : ['None', 'Blindness','Low-vision','Leprosy Cured Persons',
                          'Hearing Impairment','Locomotor Disability','Dwarfism',
                          'Intellectual Disability','Mental Illness'],
        'countrys' : ['India'],
        'states' : ['Andhra Pradesh', 'Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa',
                   'Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra',
                   'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim',
                   'Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','Gairsain','West Bengal'],
        'districts' :['Ariyalur','Coimbatore','Cuddalore','Dharmapuri','Dindigul','Erode','Kancheepuram','Kanniyakumari',
                      'Karur','Krishnagiri','Madurai','Nagapattinam','Namakkal','Perambalur','Pudukkottai','Ramanathapuram',
                      'Salem','Sivaganga','Thanjavur','The Nilgiris','Theni','Thiruvallur','Thiruvarur','Thoothukkudi',
                      'Tiruchirappalli','Tirunelveli','Tiruppur','Tiruvannamalai','Vellore','Viluppuram','Virudhunagar']
    }
    return render(request,'add_emp_personal.html',context)

def view_emp_dte(request, id):
    if 'uname' in request.session:
        view = masterPage.objects.filter(id=id).first()
        return render(request,'view_page.html',{'view':view})
    else:
        return redirect('/')

def type_create(request):
    if 'uname' in request.session:
        fetchall = typeCreate.objects.all().values
        return render(request,'type_create.html', {'items': fetchall})
    else:
        return redirect('/')

def create_type_dte(request):
    if 'uname' in request.session:
        if request.method == "POST":
            type = request.POST.get('item_type')
            rate = request.POST.get('item_rate')
            code = request.POST.get('item_code')
            desc = request.POST.get('item_desc')

            if request.method == "POST":
                create_type = typeCreate.objects.create(Item_type=type,Item_rate=rate,Item_code=code,Description=desc)
            else:
                return HttpResponse('KeyError')
        return render(request,'create_type_dte.html')
    else:
        return redirect('/')

def update_type_dte(request, id):
    if 'uname' in request.session:
        data = typeCreate.objects.get(id=id)
        if request.method == "POST":
            type = request.POST.get('item_type')
            rate = request.POST.get('item_rate')
            code = request.POST.get('item_code')
            desc = request.POST.get('item_desc')
            if request.method == "POST":    
                data.Item_type = type
                data.Item_rate = rate
                data.Item_code = code
                data.Description = desc
                data.save()
                return redirect('/type_create')
            else:
                return HttpResponse('Faild')
        context = {
            'data' :data,
        }
        return render(request,'update_type_dte.html', context)
    else:
        return redirect('/')

def del_type_dte(request, id):
    if 'uname' in request.session:
        delete_data = typeCreate.objects.filter(id=id)
        if delete_data:
            delete_data.delete()
            return redirect('/type_create')
        else:
            return HttpResponse('False')
    else:
        return redirect('/')
    
def view_type_dte(request,id):
    if 'uname' in request.session:
        view = typeCreate.objects.filter(id=id).first()
        return render(request,'view_type_dte.html',{'view':view})
    else:
        return redirect('/')

random_number = random.randint(1,1000)
def billing(request):
    if 'uname' in request.session:
        data = masterPage.objects.all().values
        item_types = typeCreate.objects.all().values

        if request.method == "POST":
            invoice_no = request.POST.get('invoice','')
            name_id = request.POST.get('emp_name')
            bill_date = request.POST.get('bill_date','')
            all_qty = 'NONE'
            all_total = 'NONE'
            if name_id != '':
                create_date = Invoice_Details(Random_Number_beta=random_number,
                                    Invoice_Number_beta=invoice_no,
                                    Name_ID_beta=name_id,
                                    Bill_Date_beta=bill_date,
                                    All_Quantity_beta=all_qty,
                                    All_Total_beta=all_total)
                create_date.save()
                return redirect('/sales_home')
            else:
                return HttpResponse('Empty Values')


        def generate_order_number():
            current_year = datetime.datetime.now().year % 100
            if not hasattr(generate_order_number, 'current_year') or generate_order_number.current_year != current_year:
                generate_order_number.current_year = current_year
                generate_order_number.counter = read_counter_from_file()  # Read the counter value from a file

            sequential_number = str(generate_order_number.counter).zfill(3)  # 001
            order_number = f"SAI-{sequential_number}-{current_year:02d}"
            generate_order_number.counter += 1
            write_counter_to_file(generate_order_number.counter)  # Write the updated counter value to the file

            return order_number

        def read_counter_from_file():
            # Read the counter value from the file
            try:
                with open('counter.txt', 'r') as file:
                    return int(file.read().strip())
            except FileNotFoundError:
                return 1  # Return 1 if the file doesn't exist

        def write_counter_to_file(counter):
            # Write the counter value to the file
            with open('counter.txt', 'w') as file:
                file.write(str(counter))

        order1 = generate_order_number()    
        context = {
            'data' : data,
            'order1' : order1,
            'item_types' : item_types,
        }

        return render(request,'Billing.html', context)
    else:
        return redirect('/')


# This is a update id get into set the fileds in ajax
def update_sales_dte(request):
    if 'uname' in request.session:
        my_id = request.GET.get('my_id')
        update_id = mainBill.objects.get(id=my_id)
        response = {
            'message': 'Data received successfully',
            'my_id': my_id,
            'item_type' : update_id.Item_Type,
            'item_code' : update_id.Item_Code,
            'item_rate' : update_id.Item_Rate,
            'Quentity' : update_id.Quantity_alpha,
            'Total' : update_id.Total_alpha,
            'Get_id' : update_id.id

        }
        return JsonResponse(response)
    else:
        return redirect('/')

def del_sales_dte(request, id):
    if 'uname' in request.session:
        try:
            item = mainBill.objects.get(id=id)
            item.delete()
            return HttpResponse('Deleted')
        except mainBill.DoesNotExist:
            return HttpResponse('False')
    else:
        return redirect('/')

# This is a update id get into update the fileds and create new updated table in ajax
def update_dte(request):
    if 'uname' in request.session:
        if request.method == "POST":
            my_id = request.POST.get('my_id')
            invoice_id = request.POST.get('invoice_id')
            type = request.POST.get('type')
            code = request.POST.get('code')
            rate = request.POST.get('rate')
            qty = request.POST.get('qty')
            tol = request.POST.get('tol')
            create_data = mainBill.objects.filter(id=my_id).update(
                Item_Type=type,Item_Code=code,
                Item_Rate=rate,Quantity_alpha=qty,
                Total_alpha=tol)
            # I newly get the id in POST in the AJAX
            bill_items = mainBill.objects.filter(Invoice_Number = invoice_id)
            table_html = ''
            for index, item in enumerate(bill_items, start=1):
                table_html += f'<tr data-id="{ item.id }"><td>{index}</td><td>{item.Invoice_Number}</td><td>{item.Item_Type}</td><td>{item.Item_Code}</td><td>{item.Item_Rate}</td><td>{item.Quantity_alpha}</td><td> &#8377; {item.Total_alpha}</td><td style="display:flex;justify-content:center;"><a onclick="UpdateItem({item.id})"><i class="fas fa-edit"></i></a><a onclick="return confirm(\'Are you sure you want to delete this record?\') ? deleteItem({item.id}) : false;"><i class="fas fa-trash"></i></a></td></tr>'

            return HttpResponse(table_html)

        else:
            # Return an error response if the request method is not POST
            response = 'Invalid request method'
            return HttpResponse(response)
    else:
        return redirect('/')

    

def fetch_data(request):
    selected_id = request.GET.get('selected_id')
    
    master_entry = masterPage.objects.get(id=selected_id)
    site_name = master_entry.site_name
    response_data = {
        'site_name': site_name,
        'emp_gst': master_entry.emp_shift,
        'emp_country': master_entry.emp_country,
        'emp_state': master_entry.emp_state,
        'emp_district': master_entry.emp_district,
        'building_no': master_entry.buliding_no,
        'emp_street': master_entry.emp_street,
        'emp_area': master_entry.emp_area,
        'emp_pincode': master_entry.emp_pincode
    }
    
    return JsonResponse(response_data)
    

def fetch_type_data(request):
    selected_id = request.GET.get('selected_id')
    
    type_entry = typeCreate.objects.get(Item_type=selected_id)
    item_code = type_entry.Item_code
    item_rate = type_entry.Item_rate
    response_data = {
        'item_code': item_code,
        'item_rate': item_rate,
    }
    
    return JsonResponse(response_data)

def get_item_details(request):
    if request.method == 'POST':
        # Retrieve the item details from the request
        invoice_id = request.POST.get('invoice')
        name_id = request.POST.get('name_id')
        bill_date = request.POST.get('bill_date')


        item_type = request.POST.get('item_type')
        item_code = request.POST.get('item_code')
        item_rate = request.POST.get('item_rate')
        item_qty = request.POST.get('item_qty')
        total = request.POST.get('total')
        # Perform any validation or data manipulation as needed
        # Create a new Bill_create object to store the item details
        bill_item = mainBill(
            Random_Number_alpha = random_number,
            Invoice_Number = invoice_id,
            Name_ID = name_id,
            Bill_Date_alpha = bill_date,
            Item_Type=item_type,
            Item_Code=item_code,
            Item_Rate=item_rate,
            Quantity_alpha=item_qty,
            Total_alpha = total)
        bill_item.save()

        input = invoice_id
        # Retrieve all Bill_create objects from the database
        bill_items = mainBill.objects.filter(Invoice_Number = input)

        # Generate the table HTML using the retrieved data
        table_html = ''
        for index, item in enumerate(bill_items, start=1):
            table_html += f'<tr data-id="{ item.id }"><td>{index}</td><td>{item.Invoice_Number}</td><td>{item.Item_Type}</td><td>{item.Item_Code}</td><td>{item.Item_Rate}</td><td>{item.Quantity_alpha}</td><td> &#8377; {item.Total_alpha}</td><td style="display:flex;justify-content:center"><a onclick="UpdateItem({item.id})"><i class="fas fa-edit"></i></a><a onclick="return confirm(\'Are you sure you want to delete this record?\') ? deleteItem({item.id}) : false;"><i class="fas fa-trash"></i></a></td></tr>'


        # Return the table HTML as the HTTP response
        return HttpResponse(table_html)
    else:
        # Return an error response if the request method is not POST
        response = 'Invalid request method'
        return HttpResponse(response)

def sales_home(request):
    if 'uname' in request.session:
        
        data = Invoice_Details.objects.all()  # Replace with your queryset or list
        items_per_page = 5
        paginator = Paginator(data, items_per_page)
        page_number = request.GET.get('page')  # Retrieve the page number from the URL query parameter
        page_obj = paginator.get_page(page_number)
        items = page_obj.object_list

        # fetchall = masterPage.objects.all().values

        fetchall = Invoice_Details.objects.all().values
        dataD = masterPage.objects.all().values
        get_data = masterPage.objects.values_list('emp_name')

        fetch_id = masterPage.objects.values_list('id', flat=True)
        fetch_name_id = Invoice_Details.objects.values_list('Name_ID_beta', flat=True)
        get_name = []

        for set_value in fetch_name_id:
            set_value_int = int(set_value) 
            
            for get in fetch_id:
                if  get == set_value_int:
                    val = get
                    get_name += masterPage.objects.filter(id=val)
        context = {
            'data':dataD,
            'get_name' : get_name,
            'fetchall' : fetchall,
            'items':data,
            'page_obj':page_obj

        }
        return render(request, 'sales_home_page.html', context)
    else:
        return redirect('/')

def update_sales_page(request,id):
    if 'uname' in request.session:
        item_types = typeCreate.objects.all().values
        data_id = Invoice_Details.objects.get(id=id)
        int_name = Invoice_Details.objects.values_list('Name_ID_beta')
            
        data = masterPage.objects.all().values
        main_table = mainBill.objects.all().values
        # Submit Button is disable
        if request.method == "POST":
            invoice_no = request.POST.get('invoice','')
            name_id = request.POST.get('emp_name')
            bill_date = request.POST.get('bill_date','')
            all_qty = 'NONE'
            all_total = 'NONE'
            if name_id != '':
                set = Invoice_Details.objects.get(Invoice_Number_beta=invoice_no)
                set.Random_Number_beta=random_number
                set.Invoice_Number_beta=invoice_no
                set.Name_ID_beta = name_id
                set.Bill_Date_beta=bill_date
                set.All_Quantity_beta=all_qty
                set.All_Total_beta=all_total
                set.save()
                return redirect('/sales_home')
            else:
                return HttpResponse('Your operation error')
            # else:
            #     return HttpResponse('Empty Values')

        context = {
            'data' : data,
            'data_id':data_id,
            'int_name':int_name,
            'main_table':main_table,
            'item_types':item_types
        }
        return render(request, 'update_sales_page.html', context)
    else:
        return redirect('/')

def get_item_table(request):
    if request.method == 'POST':
        invoice_id = request.POST.get('invoice_id')
        input = invoice_id
        bill_items = mainBill.objects.filter(Invoice_Number = input)

        table_html = ''
        for index, item in enumerate(bill_items, start=1):
            table_html += f'<tr data-id="{ item.id }"><td>{index}</td><td>{item.Invoice_Number}</td><td>{item.Item_Type}</td><td>{item.Item_Code}</td><td>{item.Item_Rate}</td><td>{item.Quantity_alpha}</td><td> &#8377; {item.Total_alpha}</td><td style="display:flex;justify-content:center"><a onclick="UpdateItem({item.id})"><i class="fas fa-edit"></i></a><a onclick="return confirm(\'Are you sure you want to delete this record?\') ? deleteItem({item.id}) : false;"><i class="fas fa-trash"></i></a></td></tr>'


        return HttpResponse(table_html)
    else:
        response = 'Invalid request method'
        return HttpResponse(response)

def update_item_dte(request):
    my_id = request.GET.get('my_id')
    update_id = mainBill.objects.get(id=my_id)
    response = {
        'message': 'Data received successfully',
        'my_id': my_id,
        'item_type' : update_id.Item_Type,
        'item_code' : update_id.Item_Code,
        'item_rate' : update_id.Item_Rate,
        'Quentity' : update_id.Quantity_alpha,
        'Total' : update_id.Total_alpha,
        'Get_id' : update_id.id

    }
    return JsonResponse(response)

def edit_item_dte(request):
    if request.method == "POST":
        my_id = request.POST.get('my_id')
        invoice_id = request.POST.get('invoice_id')
        type = request.POST.get('type')
        code = request.POST.get('code')
        rate = request.POST.get('rate')
        qty = request.POST.get('qty')
        tol = request.POST.get('tol')
        create_data = mainBill.objects.filter(id=my_id).update(
            Item_Type=type,Item_Code=code,
            Item_Rate=rate,Quantity_alpha=qty,
            Total_alpha=tol)
        # I newly get the id in POST in the AJAX
        bill_items = mainBill.objects.filter(Invoice_Number = invoice_id)
        table_html = ''
        for index, item in enumerate(bill_items, start=1):
            table_html += f'<tr data-id="{ item.id }"><td>{index}</td><td>{item.Invoice_Number}</td><td>{item.Item_Type}</td><td>{item.Item_Code}</td><td>{item.Item_Rate}</td><td>{item.Quantity_alpha}</td><td> &#8377; {item.Total_alpha}</td><td style="display:flex;justify-content:center"><a onclick="UpdateItem({item.id})"><i class="fas fa-edit"></i></a><a onclick="return confirm(\'Are you sure you want to delete this record?\') ? deleteItem({item.id}) : false;"><i class="fas fa-trash"></i></a></td></tr>'


        return HttpResponse(table_html)

    else:
        # Return an error response if the request method is not POST
        response = 'Invalid request method'
        return HttpResponse(response)
    
def del_sales_page(request, id):
    if 'uname' in request.session:
        item_main = mainBill.objects.filter(Invoice_Number=id)
        item_sub = Invoice_Details.objects.filter(Invoice_Number_beta=id)
        if item_main:
            item_main.delete()
        if item_sub:
            item_sub.delete()
        return redirect('/sales_home')
    else:
        return redirect('/')

def del_list_item(request, id):
    item_main = mainBill.objects.get(id=id)
    if item_main:
        item_main.delete()
        return HttpResponse('Deleted')

def select2DDL(request):
    products = ProductsModel.objects.all()
    items = ItemModel.objects.all()
    
    context = {
        'Products': products,
        'Items': items
    }
    return render(request, 'practies/select2ddl.html', context)

def dropdownlist(request):
    product_id = request.GET.get('product_id')
    items = ItemModel.objects.filter(P_Id=product_id)

    optionhtml = ''
    for index, item in enumerate(items, start=1):
        optionhtml += f'<option value="{item.Item_Id}">{item.Item_Name}</option>'
    return HttpResponse(optionhtml)

def dropdownlistnext(request):
    item_id = request.GET.get('item_id')
    items = AccessoriesModel.objects.filter(Item_Id=item_id)

    optionhtml = ''
    for index, item in enumerate(items, start=1):
        optionhtml += f'<option value="{item.Acc_Id}">{item.Acc_Name}</option>'
    return HttpResponse(optionhtml)

def setsession(request):
    request.session['name'] = 'Shanmugam'
    request.session.set_expiry(20)
    return render(request,'practies/setsession.html')

def getsession(request):
    if 'name' in request.session:
        name = request.session.get('name')
        return render(request,'practies/getsession.html', {'name' : name})
    else:
        return HttpResponse('Expired')

def delsession(request):
    request.session.flush()
    return render(request,'practies/delsession.html')

def fileconvert(request):
    fetchall = masterPage.objects.all().values
    return render(request,'practies/importandexport.html',{'fetchall' : fetchall})

# def nxt_billing(request):
#     ran_id = random.randint(124,999)
#     data = masterPage.objects.all()
#     def generate_order_number():
#         current_year = datetime.datetime.now().year % 100
#         if not hasattr(generate_order_number, 'current_year') or generate_order_number.current_year != current_year:
#             generate_order_number.current_year = current_year
#             generate_order_number.counter = 1

#         # sequential_number = str(generate_order_number.counter).zfill(3) #001
#         order_number = f"SAI-{ran_id}-{current_year:02d}"
#         generate_order_number.counter += 1

#         return order_number
    

#     order1 = generate_order_number()
    

#     context = {
#         'order1' : order1,
#         'data' : data
#     }

#     return render(request,'nxt_billing.html',context)

# from .models import Form1Data, Form2Data

# def my_form_view(request):
#     if request.method == 'POST':
#         # Retrieve the form-1 data
#         invoice = request.POST.get('invoice')
#         bill_date = request.POST.get('bill_date')
#         emp_name = request.POST.get('emp_name')
#         site_name = request.POST.get('site_name')
#         item_address = request.POST.get('item_address')
#         gst_no = request.POST.get('gst_no')

#         # Perform any validation or data manipulation as needed
       
#         # Redirect to a success page or perform any other desired action
#         return redirect('/')

#     return render(request, 'add_invoice_item.html')


class generator(View):
    def get(self, request, *args, **kwargs):
        try:
            data = masterPage.objects.all().values()
            current_date = datetime.datetime.now()
            context = {
                'data': data,
                'current_date': current_date
            }
            pdf = render_to_pdf('download_file/customer_list_pdf.html', context)
            response = HttpResponse(pdf, content_type='application/pdf')

            if request.GET.get('pdf', ''):  
                filename = 'customer_details_report.pdf'
                content = 'attachment; filename="%s"' % filename
            else:
                filename = 'customer_details_report_printing.pdf'
                content = 'inline; filename="%s"' % filename

            response['Content-Disposition'] = content
            return response
                
        except Exception as e:
            return HttpResponse(str(e))

