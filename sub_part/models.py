from django.db import models

# Create your models here.
class contact_table(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()	
	phone=models.CharField(max_length=15)
	message=models.TextField()

	def __str__(self):
		return self.name


class signup_table(models.Model):
	username=models.CharField(max_length=15)
	email=models.EmailField()
	password=models.CharField(max_length=100)
	picture=models.FileField(upload_to='profile_picture', null='True')

	def __str__(self):
		return self.username


class add_feedback_table(models.Model):
	date=models.CharField(max_length=15)
	rating=models.IntegerField()
	name=models.CharField(max_length=100)
	description=models.TextField()
	logger_id=models.IntegerField()

	def __str__(self):
		return self.name

class add_cart_table(models.Model):
	item=models.CharField(max_length=100)
	cost=models.IntegerField()
	quantity=models.CharField(max_length=50)
	price=models.IntegerField()
	logger_id=models.IntegerField()

	def __str__(self):
		return self.item

class add_drive_table(models.Model):
	drive=models.CharField(max_length=100)
	transaction=models.CharField(max_length=50)
	tid=models.CharField(max_length=50)
	doc=models.CharField(max_length=50)
	address=models.CharField(max_length=70)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.drive

class add_report_table(models.Model):
	date=models.CharField(max_length=20)
	type=models.CharField(max_length=50)
	description=models.CharField(max_length=50)
	status=models.CharField(max_length=50)
	username=models.CharField(max_length=70)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.username

class add_payment_table(models.Model):
	name=models.CharField(max_length=50)
	crop=models.CharField(max_length=50)
	cost=models.IntegerField()
	date=models.CharField(max_length=20)
	income=models.IntegerField()
	logger_id=models.IntegerField()

	def __str__(self):
		return self.name

class add_booking_table(models.Model):
	pname=models.CharField(max_length=20)
	pcode=models.CharField(max_length=10)
	customer=models.CharField(max_length=50)
	pdate=models.CharField(max_length=20)
	status=models.CharField(max_length=50)
	tid=models.CharField(max_length=10)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.pname

class add_land_table(models.Model):
	ltype=models.CharField(max_length=20)
	cost=models.IntegerField()
	benefits=models.CharField(max_length=150)
	drawbacks=models.CharField(max_length=150)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.ltype

class add_charge_table(models.Model):
	ename=models.CharField(max_length=20)
	color=models.CharField(max_length=20)
	price=models.IntegerField()
	time=models.CharField(max_length=15)
	total=models.IntegerField()
	quantity=models.IntegerField()
	logger_id=models.IntegerField()

	def __str__(self):
		return self.ename


class add_duration_table(models.Model):
	ename=models.CharField(max_length=20)
	color=models.CharField(max_length=20)
	price=models.IntegerField()
	time=models.CharField(max_length=15)
	total=models.IntegerField()
	quantity=models.IntegerField()
	logger_id=models.IntegerField()

	def __str__(self):
		return self.ename

class add_equipment_table(models.Model):
	ename=models.CharField(max_length=20)
	color=models.CharField(max_length=20)
	price=models.IntegerField()
	time=models.CharField(max_length=15)
	total=models.IntegerField()
	quantity=models.IntegerField()
	logger_id=models.IntegerField()

	def __str__(self):
		return self.ename


class add_farmer_table(models.Model):
	fname=models.CharField(max_length=20)
	mobile=models.CharField(max_length=20)
	adhar=models.CharField(max_length=12)
	password=models.CharField(max_length=16)
	address=models.CharField(max_length=50)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.fname

class add_vendor_table(models.Model):
	vname=models.CharField(max_length=20)
	contact=models.CharField(max_length=20)
	vid=models.CharField(max_length=6)
	location=models.CharField(max_length=50)
	adhar=models.CharField(max_length=12)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.vname

class add_vehicle_table(models.Model):
	vname=models.CharField(max_length=20)
	color=models.CharField(max_length=20)
	rent=models.IntegerField()
	condition=models.CharField(max_length=10)
	company=models.CharField(max_length=30)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.vname

class add_fertilizer_table(models.Model):
	fname=models.CharField(max_length=20)
	supplier=models.CharField(max_length=20)
	weight=models.CharField(max_length=20)
	price=models.IntegerField()
	company=models.CharField(max_length=20)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.fname

class add_pesticide_table(models.Model):
	pname=models.CharField(max_length=20)
	supplier=models.CharField(max_length=20)
	weight=models.CharField(max_length=20)
	price=models.IntegerField()
	company=models.CharField(max_length=20)
	logger_id=models.IntegerField()

	def __str__(self):
		return self.pname
