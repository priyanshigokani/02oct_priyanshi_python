from django.contrib import admin
from django.urls import path,include
from apiapp import views


urlpatterns = [
    path('getAll',views.getAll),
    path('getId/<int:id>',views.getId),
    path('deleteId/<int:id>',views.deleteId),
    path('inData/',views.inData),
    path('updata/<int:id>',views.updata),
]