from django.shortcuts import render
from django.http import Http404  , HttpResponse , HttpResponseNotFound ,HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

from django.shortcuts import render

def starting_page (request):
    return render (request , "blog/index.html")

def posts (request):
    return render (request,"blog/all-posts.html" )

def single_post(request):
    pass
