from django.shortcuts import render

def post_list(request) : 
	return render(request, 'Request_of_Customer/post_list.html',{})
	
def practice (request) :
	return render(request, 'Request_of_Customer/practice.html',{})
# Create your views here.
