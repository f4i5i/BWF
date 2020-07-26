from django.urls import path
from .views import *

urlpatterns = [
    path('country',Country_Data,name='country_data'),
    path('tours',Scrape_Data, name='scrape_data'),
    path('draws', Draw_Data, name='Draw_data')
]
