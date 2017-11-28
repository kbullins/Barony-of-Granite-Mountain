from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from django.conf import settings
from django.conf.urls.static import static
from . import views

# from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'BGM.views.index', name='index'),
    url(r'^home', 'BGM.views.home', name='home'),
    url(r'^calendar', 'BGM.views.calendar', name='calendar'),
	url(r'^awards', 'BGM.views.awards', name='awards'),
	url(r'^officers', 'BGM.views.officers', name='officers'),
    url(r'^contact/$', 'BGM.views.contact', name='contact'),
	url(r'^thankyou/', 'BGM.views.thankyou', name='thankyou'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^newsletter/$', 'BGM.views.newsletter', name='newsletter'),
	url(r'^links/$', 'BGM.views.links', name='links'),
	#Authentication Pages
	url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
	#Activities Pages
    url(r'^armouredcombat/$', 'BGM.views.armouredcombat', name='armouredcombat'),
	url(r'^rapiercombat/$', 'BGM.views.rapiercombat', name='rapiercombat'),
	url(r'^artsciences/$', 'BGM.views.artsciences', name='artsciences'),
	url(r'^scriptorium/$', 'BGM.views.scriptorium', name='scriptorium'),
	url(r'^meeting/$', 'BGM.views.meeting', name='meeting'),
	url(r'^archery/$', 'BGM.views.archery', name='archery'),
	url(r'^thrownweapons/$', 'BGM.views.thrownweapons', name='thrownweapons'),
	#About Us Pages
	url(r'^history', 'BGM.views.history', name='history'),
	url(r'^bgmcourt', 'BGM.views.bgmcourt', name='bgmcourt'),
	url(r'^bgmchamp', 'BGM.views.bgmchamp', name='bgmchamp'),
) 
