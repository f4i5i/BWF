from django.shortcuts import render, HttpResponse
import django_rq
import requests
# Create your views here.
from .scraper import *
from .tasks import scrape


def Country_Data(request):
    queue = django_rq.get_queue('default', is_async=True, default_timeout=30000)
    queue.enqueue(get_country)
    return HttpResponse("Scraping Country's..........")


def Scrape_Data(request):
    queue = django_rq.get_queue(
        'default', is_async=True, default_timeout=30000)
    queue.enqueue(scrape)
    return HttpResponse("Scraping Tournamet and tours details..........")
