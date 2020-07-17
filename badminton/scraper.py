import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date
from datetime import timedelta
from players.models import *
from badminton.models import *
import re


HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.16 Safari/537.36"}
url = "https://bwf.tournamentsoftware.com/find?StartDate=2020-01-01&EndDate=2020-01-31&page=2"
# s_date = str(date.today())
# e_date = str(date.today() + timedelta(days=13))
# url = "https://bwf.tournamentsoftware.com/find?StartDate=" +s_date+"&EndDate="+e_date+"&page=2"


def get_tourn_urls(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        full_data = driver.find_elements_by_css_selector("ul#searchResultArea")
        lists = []
        for item in full_data:
            li = item.find_elements_by_tag_name("li")
            for li_item in li:
                name_trn = li_item.find_elements_by_css_selector("a.media__link")
                for na_tr in name_trn:
                    lists.extend([na_tr.get_attribute('title'),na_tr.get_attribute('href')])

    except Exception as e:
        error, _ = Error.objects.get_or_create(url=url,error=e,extra_info="The function emiting the error is get_tourn_urls in tasks.py file badminton app")
    
    return lists



def get_tourn_info(links):
    print(links, "Recevie")
    tourn_url = requests.get(links).text
    source = BeautifulSoup(tourn_url, 'html.parser')
    dive = source.find('div', class_='media__content')
    Trnment_name = dive.find('h2', class_='media__title--large')
    location = dive.find('img', class_='icon-lang')
    dates = dive.find('small', class_="media__subheading--muted")
    tour_name = dive.find('li', class_='list__item')
    events = source.find('table', class_='tournamentevents')
    gender = {}
    gender = set()
    typee = {}
    typee = set()
    td = events.find('td')
    tags = td.find_all('a')
    for i in tags:
        gender.add((i.text)[0])
        typee.add((i.text)[1])
    tourn_name = Trnment_name.text
    trn_pat = tsna_pat = re.compile('\w[A-Za-z]+')
    trn = trn_pat.findall(tourn_name)
    trn_name = " "
    trn_name = trn_name.join(trn)
    tsna_pat = re.compile('\w[a-z]+')
    ts = tsna_pat.findall(tourn_name)
    ts_name = " "
    ts_name = ts_name.join(ts)
    tourn_id = links.split('=')[1]
    seas_pat = re.compile('\d{4}$')
    seas_year = seas_pat.findall(tourn_name)
    country = location.get('title')
    start_date = dates.find_all('time')[0].text
    end_date = dates.find_all('time')[1].text
    tour_name = tour_name.text
    
    cnt = Country.objects.get(name=country)
    sport = Sport.objects.get(pk=8)
    #Tours Entry
    tours, tours_not = Tours.objects.get_or_create(name=tour_name)

    #Seasons Entry
    season, season_ = Season.objects.get_or_create(name=str(seas_year[0]))

    #Tournaments Entry
    tourn, tourn_ = Tournament.objects.get_or_create(trnname=str(trn_name), sptid=sport,cntid=cnt ,turid=tours, snid=season)
    
    #Tournaments_Seasons Entry
    tseason, tseason_ = Tournament_Season.objects.get_or_create(snid=season, tsname=str(ts_name))

    #BWF_Tournaments Entry
    bwfcomp, bwfcomp_ = BWFTournament.objects.get_or_create(tourn_id=str(tourn_id), tournament_id=tourn, gender=str(gender), m_type=str(typee), startdate=str(start_date), enddate=str(end_date))

    #Event Entry
    # eve, eve_ = Event.objects.get_or_create(champ_events=bwfcomp,event_key=)


def get_country():
    C_url = "https://countrycode.org/"
    req = requests.get(C_url, headers=HEADERS, timeout=60).text
    soup = BeautifulSoup(req, 'html.parser')
    table = soup.find_all('tr')
    for i in range(1,240):
        name_td = table[i].find_all('td')
        c_name = name_td[0].text
        f_code = name_td[2].text
        s_code = f_code.split('/')
        iso_code = s_code[1]
        print(c_name, iso_code)
        cou_name = Country.objects.get_or_create(name=c_name, code=iso_code)


def get_draws(tmn_id):
    tourn_url = requests.get("https://bwf.tournamentsoftware.com/sport/draws.aspx?id="+tmn_id)
    soup = BeautifulSoup(tourn_url.content, 'lxml')
    table = soup.find('table', class_="ruler")
    rows = table.find_all('tr')
    draw_list = []
    spurl = "https://bwf.tournamentsoftware.com/sport/"
    for row in rows[1::]:
        tds = row.find_all('td')
        draw_list.extend([tds[0].text, tds[2].text, spurl+tds[0].a.get('href')])
    return draw_list
