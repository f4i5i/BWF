import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date
from datetime import timedelta
import re
from .models import Error
from .scraper import *


def scrape():

    liston = [['PERODUA Malaysia Masters 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=6D74F318-A951-4C8F-9451-5DA3F33DF6C3'],
             ['PRESIDENT CUP Nepal Junior International Series 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=99F48C9E-1C30-4A2C-841B-07871AE75ABC'],
             ['YONEX Estonian International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=6D70113B-5B61-4FE1-845D-BFC95C2D7747'],
             ['DAIHATSU Indonesia Masters 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=2FFEF920-EE97-42C3-B885-2CF80505A03C'],
             ['PZU VICTOR Polish Junior 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=B5F7B508-DCC3-4E23-A576-6C1010E6DA3F'],
             ['VICTOR Swedish Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=4CF5DAEE-C1E6-4C65-A4EB-6B6D59DF0B26'],
             ['Princess Sirivannavari Thailand Masters 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=D5E5610C-87CD-4B0B-991A-44DBFC1F59E2'],
             ['RSL Iceland International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=4685C3C3-BD07-4A23-B559-E8497C869911'],
             ['Swedish Junior 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=3FC49352-37A2-452E-92F0-3DA5D02BDD76'],
             ['Swedish U17 International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=72054EDD-0891-4AD5-B68E-B5A7835DB899'],
             ['The 29th Fajr Badminton International Challenge 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=8D445218-F62D-40CB-8BC2-9C2454D4FF28'],
             ['10th MULTI ALARM Hungarian International Junior Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=94E45878-F696-4A48-A3B6-0BADB764EEEE'],
             ['Spanish U17 Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=AE415141-F670-4E23-B028-E69809ED4940'],
             ['VICTOR Oceania Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=CE703801-9D7C-472D-A03F-0487801B578E'],
             ["All Africa Men's & Women's Team Championships 2020",
              'https://bwf.tournamentsoftware.com/sport/tournament?id=1A6378A1-00EB-405C-AB38-DE1D9C5EB339'],
             ["2020 European Men's & Women's Team Championships",
              'https://bwf.tournamentsoftware.com/sport/tournament?id=D912EA28-F825-469A-8FB4-5E4137C7B7D7'],
             ['Badminton Asia Team Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=AD641BA1-C5A5-4F18-8813-A8384C09D9AD'],
             ["VICTOR Oceania Men's and Women's Team Championships 2020",
              'https://bwf.tournamentsoftware.com/sport/tournament?id=137CAD95-8371-469D-8635-E8637CC32992'],
             ['Male & Female Pan Am Team Continental Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=6D80370D-963F-4635-968E-EBF2477F6CD4'],
             ['2020 European U15 Championships',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=84DA0B90-1E7E-4D3A-8E86-77D7EE3D68AF'],
             ['All Africa Individual Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=0A75BDDE-1961-4042-B4F8-748AF942AE2F'],
             ['YONEX France U17 Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=29A5E3D7-25C7-48E3-BBBE-DB982046EC91'],
             ['Barcelona Spain Masters 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=E8551F1E-6F4D-491C-861A-AF65C3831B49'],
             ['BEERLAO International Series 2020 (Cancelled)',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=D0460BCC-4056-4550-A5ED-A1C67262F0A4'],
             ['Austrian Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=B4CEC666-2D9C-4F6F-8F3F-63DE57484477'],
             ['Uganda International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=85D8EDE9-109B-4C28-9981-8E6C4509DED8'],
             ['DECATHLON PERFLY Italian Junior 2020 (Suspended)',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=966E2805-3517-4C66-989B-279B19586765'],
             ['FZ FORZA Slovak Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=4340E7EB-6C17-4C02-B69C-0E8B2C148129'],
             ['YONEX Dutch Junior International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=645F6C26-8F9F-4146-8403-FA639C26511A'],
             ['Kenya International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=9CAB388C-F79F-4020-BCDF-848A2BA2F67C']]
    
    Words = ["suspended", "cancelled", "junior", "postponed", "u17"]
    for j in range(len(liston)):
        text_io = liston[j][0].lower()
        if not any(x in text_io for x in Words):
            get_tourn_info(liston[j][1])

