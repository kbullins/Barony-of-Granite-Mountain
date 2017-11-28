from django.conf.urls import include, url
from django.contrib import admin, auth
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from BGM.views import *
from . import views

# from django.contrib import admin

urlpatterns = [
   url(r'^$', index, name='index'),
   url(r'^home', home, name='home'),
   url(r'^calendar', calendar, name='calendar'),
   url(r'^awards', awards, name='awards'),
   url(r'^officers', officers, name='officers'),
   url(r'^contact/$', contact, name='contact'),
   url(r'^thankyou/', thankyou, name='thankyou'),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^newsletter/$', newsletter, name='newsletter'),
   url(r'^links/$', links, name='links'),
	   #Authentication Pages
   #url(r'^login/$', djangocontrib.auth.views.login),
   #url(r'^logout/$', djangocontrib.auth.views.logout),
   url(r'^login/$', auth_views.login, name='login'),
   url(r'^logout/$', auth_views.logout, name='logout'),

   #Activities Pages
   url(r'^armouredcombat/$', armouredcombat, name='armouredcombat'),
   url(r'^rapiercombat/$', rapiercombat, name='rapiercombat'),
   url(r'^artsciences/$', artsciences, name='artsciences'),
   url(r'^scriptorium/$', scriptorium, name='scriptorium'),
   url(r'^meeting/$', meeting, name='meeting'),
   url(r'^archery/$', archery, name='archery'),
   url(r'^thrownweapons/$', thrownweapons, name='thrownweapons'),
	   #About Us Pages
   url(r'^history', history, name='history'),
   url(r'^bgmcourt', bgmcourt, name='bgmcourt'),
   url(r'^bgmchamp', bgmchamp, name='bgmchamp'),
]
