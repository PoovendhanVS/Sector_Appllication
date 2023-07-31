from django.db import models

# Create your models here.

class dashbd(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)


class masterPage(models.Model):
    choices = [
        ('skill A', 'skill A'),
        ('skill B', 'skill B'),
        ('skill C', 'skill C'),
        ('skill D', 'skill D'),
        ('skill E', 'skill E'),
    ]
    emp_gender = models.CharField(max_length=50)
    emp_name = models.CharField(max_length=100)
    date_of_join =models.DateField()
    role =models.CharField(max_length=100)
    site_name =models.CharField(max_length=100)
    emp_shift =models.CharField(max_length=100)
    emp_cate =models.CharField(max_length=100)
    emp_bio =models.CharField(max_length=100)
    emp_head =models.CharField(max_length=100)
    emp_skill =models.CharField(max_length=100)
    
    emp_skill = models.CharField(max_length=255, choices=choices, blank=True, null=True)
    emp_img =models.ImageField(upload_to='static/img/')
    
    martial = models.CharField(max_length=100)
    date_of_birth =models.DateField()
    emp_age = models.CharField(max_length=100)
    blood_grp = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    activities = models.CharField(max_length=100)
    disability = models.CharField(max_length=100)
    emp_country = models.CharField(max_length=100)
    emp_state = models.CharField(max_length=100)
    emp_district = models.CharField(max_length=100)
    buliding_no = models.CharField(max_length=100)
    emp_street = models.CharField(max_length=100)
    emp_area = models.CharField(max_length=100)
    emp_pincode = models.CharField(max_length=100)
    emp_p_country = models.CharField(max_length=100)
    emp_p_state = models.CharField(max_length=100)
    emp_p_district = models.CharField(max_length=100)
    p_buliding_no = models.CharField(max_length=100)
    emp_p_street = models.CharField(max_length=100)
    emp_p_area = models.CharField(max_length=100)
    emp_p_pincode = models.CharField(max_length=100)

class typeCreate(models.Model):
    Item_type = models.CharField(max_length=100)
    Item_rate = models.CharField(max_length=100)
    Item_code = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    
class Invoice_Details(models.Model):
    Random_Number_beta = models.CharField(max_length=100)
    Invoice_Number_beta = models.CharField(max_length=100)
    Name_ID_beta = models.IntegerField(max_length=100)
    Bill_Date_beta = models.DateField()
    All_Quantity_beta = models.CharField(max_length=100)
    All_Total_beta = models.CharField(max_length=100)
    
class mainBill(models.Model):
    Random_Number_alpha = models.CharField(max_length=100)
    Invoice_Number = models.CharField(max_length=100)
    Name_ID = models.IntegerField(max_length=100)
    Bill_Date_alpha = models.DateField()
    Item_Type = models.CharField(max_length=100)
    Item_Code = models.CharField(max_length=100)
    Item_Rate = models.CharField(max_length=100)
    Quantity_alpha = models.CharField(max_length=100)
    Total_alpha = models.CharField(max_length=100)

class addCountryModel(models.Model):
    Country_Id = models.IntegerField(primary_key=True)
    Country_Name = models.CharField(max_length=100)

class addStateModel(models.Model):
    State_Id = models.IntegerField(primary_key=True)
    State_Name = models.CharField(max_length=100)
    Country_Id = models.IntegerField()

class addDistrictModel(models.Model):
    District_Id = models.IntegerField(primary_key=True)
    District_Name = models.CharField(max_length=100)
    State_Id = models.IntegerField()

class ProductsModel(models.Model):
    P_Id = models.IntegerField(primary_key=True)
    Product_Name = models.CharField(max_length=100)

class ItemModel(models.Model):
    Item_Id = models.IntegerField(primary_key=True)
    Item_Name = models.CharField(max_length=100)
    P_Id = models.IntegerField()

class AccessoriesModel(models.Model):
    Acc_Id = models.IntegerField(primary_key=True)
    Acc_Name = models.CharField(max_length=100)
    Item_Id = models.IntegerField()
    
class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
    