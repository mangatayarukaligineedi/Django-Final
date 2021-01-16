from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Upd(models.Model):
	g = [('M',"Male"),('F',"Female")]
	age = models.IntegerField(default=18)
	gender = models.CharField(max_length=7,choices=g)
	im = models.ImageField(upload_to="Image",default="avathar.png")
	p = models.OneToOneField(User,on_delete=models.CASCADE)
class hall_details(models.Model):

	tp=[('AC','AC'),('NON-AC','NON-AC')]
	number = models.IntegerField(default=101,unique=True)
	hall_type = models.CharField(max_length=12,choices=tp)
	capacity = models.IntegerField(default=100)
	cost = models.IntegerField(default=2000)
	image = models.ImageField(upload_to="Image/",default="avathar.png")

	def __str__(self):
		return str(self.number)


class Book_hall(models.Model):
    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room_no = models.ForeignKey(hall_details, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.guest.username