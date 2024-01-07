from django.db import models

STATE_CHOICE =(
("Arunachal Pradesh ","Arunachal Pradesh "),
("Assam","Assam"),
("Bihar","Bihar"),
("Chhattisgarh","Chhattisgarh"),
("Goa","Goa"),
("Gujarat","Gujarat"),
("Haryana","Haryana"),
("Himachal Pradesh","Himachal Pradesh"),
("Jammu and Kashmir ","Jammu and Kashmir "),
("Jharkhand","Jharkhand"),
("Karnataka","Karnataka"),
("Kerala","Kerala"),
("Madhya Pradesh","Madhya Pradesh"),
("Maharashtra","Maharashtra"),
("Manipur","Manipur"),
("Meghalaya","Meghalaya"),
("Mizoram","Mizoram"),
("Nagaland","Nagaland"),
("Odisha","Odisha"),
("Punjab","Punjab"),
("Rajasthan","Rajasthan"),
("Sikkim","Sikkim"),
("Tamil Nadu","Tamil Nadu"),
("Telangana","Telangana"),
("Tripura","Tripura"),
("Uttar Pradesh","Uttar Pradesh"),
("Uttarakhand","Uttarakhand"),
("West Bengal","West Bengal"),
("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
("Chandigarh","Chandigarh"),
("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
("Daman and Diu","Daman and Diu"),
("Lakshadweep","Lakshadweep"),
("National Capital Territory of Delhi","National Capital Territory of Delhi"),
("Puducherry","Puducherry"))


# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=80)
    date=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=80)
    locality=models.CharField(max_length=80)
    city=models.CharField(max_length=80)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=80)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=80)
    profile_image=models.ImageField(upload_to='myimage', blank=True) # whereever using imagrfield we have to install pillow package
    my_file=models.FileField(upload_to='doc',blank=True)

