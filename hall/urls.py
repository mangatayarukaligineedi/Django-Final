from django.urls import path
from hall import views
from django.contrib.auth import views as v 

urlpatterns = [
    path('',views.home,name="hm"),
	# path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.regis,name="regi"),
	path('pf/',views.prfle,name="pfe"),
	path('upf/',views.updf,name="upfe"),
	path('lg/',v.LoginView.as_view(template_name="sa/login.html"),name="lgn"), 
    path('logout/',v.LogoutView.as_view(template_name="sa/logout.html"),name="logout"),
    path('halls/',views.halls,name='halls'),
    path('book_hall/<int:hall>/',views.book_hall,name="book_hall"),
    path('myhalls/<int:id>/',views.myhalls,name="myhalls"),
    path('vacate/<int:hall>',views.vacate,name='vacate'),
]