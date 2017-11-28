from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

#def index(request):
    #return render_to_response('index.html', context_instance=RequestContext(request))
#    return render(request, 'index.html', {})

def index(request):
	return render(request, 'index.html')


def home(request):
	if request.user.is_authenticated():
		# Do something for authenticated users.
		return render(request, 'index.html', {})
	else:
		# Do something for anonymous users.
		return render(request, 'index.html', {})

def calendar(request):
    return render(request, 'calendar.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})
	
def awards(request):
	return render(request, 'awards.html', {})
	
def officers(request):
	return render(request, 'officers.html', {})

#Activities Views
def armouredcombat(request):
    return render(request, 'activities/armouredcombat.html', {})

def rapiercombat(request):
    return render(request, 'activities/rapiercombat.html', {})

def artsciences(request):
    return render(request, 'activities/artsciences.html', {})
	
def scriptorium(request):
	return render(request, 'activities/scriptorium.html', {})

def meeting(request):
	return render(request, 'activities/meeting.html', {})

def archery(request):
	return render(request, 'activities/archery.html', {})
	
def thrownweapons(request):	
	return render(request, 'activities/thrownweapons.html', {})

#About Us Views	
def history(request):
    return render(request, 'aboutus/history.html', {})

def bgmcourt(request):
	return render(request, 'aboutus/bgmcourt.html', {})

def bgmchamp(request):
    return render(request, 'aboutus/bgmchamp.html', {})
	
def contact(request):	
	return render(request, 'contact.html', {})
	
def newsletter(request):	
	return render(request, 'newsletter.html', {})

def links(request):	
	return render(request, 'links.html', {})

