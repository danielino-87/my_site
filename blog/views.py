from django.shortcuts import render
from django.http import Http404  , HttpResponse , HttpResponseNotFound ,HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "uva-e-terreno",
        "image": "uva-fragolino.jpg",
        "author": "Daniele",
        "date": date(2021, 7, 21),
        "title": "Le nostre Uve e il nostro Terreno",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "produrre-il-vino",
        "image": "uva_fragola_bianca.jfif",
        "author": "Daniele",
        "date": date(2022, 3, 10),
        "title": "Produzione del Vino : Tutti i passaggi",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "marmellata-uva",
        "image": "marmellata-uva-fragola.jfif",
        "author": "Daniele",
        "date": date(2020, 8, 5),
        "title": "Ricetta :  Marmellata di Uva Fragola",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(pippo):
    return pippo['date']


def starting_page (request):
    sorted_posts = sorted (all_posts , key=get_date)
    latest_posts = sorted_posts[-3:]
    return render (request , "blog/index.html" , {
        "posts": latest_posts
    })

def posts (request):
    return render (request,"blog/all-posts.html" )

def single_post(request,slug):
    return render (request , "blog/post-detail.html")
