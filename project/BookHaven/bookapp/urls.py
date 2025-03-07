from django.contrib import admin
from django.urls import path,include
from bookapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('',views.index,name='/'),
  path('log_in/',views.log_in,name='log_in'),
  path('addbook/',views.addbook,name='addbook'),
  path('sign_up/',views.sign_up,name='sign_up'),
  path('books/<str:genre>/',views.showbook, name='showbook'),
  path('search/',views.search,name='search'),
  path('author_apply/',views.author_apply),
  path('logout/',views.userlogout),
   
   
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)