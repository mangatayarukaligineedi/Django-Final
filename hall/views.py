from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from hall.forms import Usregis,halldetails,Bookhall
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from final import settings
from django.core.mail import send_mail
from hall.models import hall_details,Book_hall

# Create your views here.


def home(request):
	return render(request,'sa/home.html')

def contact(request):
	return render(request,'sa/contact.html')


def regis(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			sb = "Testing Email to register for Worklog Project"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				y.save()
				messages.success(request,"please check your {}  for login creadentials".format(rc))
				return redirect('/lg')
				messages.danger(request,"please check your {}  for login creadentials".format(rc))
		else:
			return HttpResponse('invalid')
	y = Usregis()
	return render(request,'sa/register.html',{'t':y})



@login_required
def prfle(request):
	return render(request,'sa/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd) 
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'ht/updateprofile.html',{'r':p,'q':t}) 

@login_required
def halls(request):
	x = hall_details.objects.all()
	halls = []
	for i in x:
		if not Book_hall.objects.filter(room_no=i):
			halls.append(i)
	return render(request,'sa/halls.html',{'halls':halls})

@login_required
def book_hall(request,hall):
	form = Bookhall(request.POST or None)
	if form.is_valid():
		t = form.save(commit=False)
		t.room_no = hall_details.objects.get(number=hall)
		t.guest = request.user
		t.save()
		halldetails = hall_details.objects.get(number=hall)
		halldetails.booked = True
		halldetails.save()
		return redirect('/halls')
	return render(request,'sa/book_hall.html',{'form':form})

@login_required
def myhalls(request,id):
	halls = Book_hall.objects.filter(guest = request.user)
	return render(request,'sa/myhalls.html',{'halls':halls})

def vacate(request,hall):
	hall = Book_hall.objects.filter(room_no = hall_details.objects.get(number=hall))
	hall.delete()
	return redirect('halls')