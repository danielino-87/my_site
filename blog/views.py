from django.shortcuts import render
from django.http import Http404  , HttpResponse , HttpResponseNotFound ,HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date

from django.shortcuts import render

posts = [
      {
          "slug" : "hike-in-the-mountains",
          "image" : "uva-fragolino.jpg",
          "author" : "Daniele",
          "date" : date(2021 , 10 ,  25),
      }
]

def starting_page (request):
    return render (request , "blog/index.html")

def posts (request):
    return render (request,"blog/all-posts.html" )

def single_post(request,slug):
    return render (request , "blog/post-detail.html")
