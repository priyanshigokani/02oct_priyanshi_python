from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',views.index,name='/'),
path('signup/',views.usersignup,name='usersignup'),
path('signin/',views.signin,name='signin'), 
path('student/',views.student,name='student'),
path('teacher/',views.teacher,name='teacher'),
path('base/',views.base,name='base'),
path('addTea/',views.addTEA,name='addTEA'),
path('addStud/',views.addStud,name='addStud'),
path('adminn/',views.adminn,name='adminn'),
path('library/',views.library,name='library'),
path('addBooks/',views.addBooks,name='addBooks'),
path('addEvent/',views.addEvent,name='addEvent'),
path('upd/',views.upd,name='upd'),
path('event/', views.event, name='event'),
path('deleteTea/<int:id>',views.deleteTea),
path('deleteStu/<int:id>',views.deleteStu),
path("userlogout/", views.userlogout),
path('forgotPass/',views.forgotPass),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)