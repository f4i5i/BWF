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


liston = [['PERODUA Malaysia Masters 2020',
           'https://bwf.tournamentsoftware.com/sport/tournament?id=6D74F318-A951-4C8F-9451-5DA3F33DF6C3', '6D74F318-A951-4C8F-9451-5DA3F33DF6C3'],
          ['PRESIDENT CUP Nepal Junior International Series 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=99F48C9E-1C30-4A2C-841B-07871AE75ABC', '99F48C9E-1C30-4A2C-841B-07871AE75ABC'],
          ['YONEX Estonian International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=6D70113B-5B61-4FE1-845D-BFC95C2D7747', '6D70113B-5B61-4FE1-845D-BFC95C2D7747'],
          ['DAIHATSU Indonesia Masters 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=2FFEF920-EE97-42C3-B885-2CF80505A03C', '2FFEF920-EE97-42C3-B885-2CF80505A03C'],
          ['PZU VICTOR Polish Junior 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=B5F7B508-DCC3-4E23-A576-6C1010E6DA3F', 'B5F7B508-DCC3-4E23-A576-6C1010E6DA3F'],
          ['VICTOR Swedish Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=4CF5DAEE-C1E6-4C65-A4EB-6B6D59DF0B26', '4CF5DAEE-C1E6-4C65-A4EB-6B6D59DF0B26'],
          ['Princess Sirivannavari Thailand Masters 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=D5E5610C-87CD-4B0B-991A-44DBFC1F59E2', 'D5E5610C-87CD-4B0B-991A-44DBFC1F59E2'],
          ['RSL Iceland International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=4685C3C3-BD07-4A23-B559-E8497C869911', '4685C3C3-BD07-4A23-B559-E8497C869911'],
          ['Swedish Junior 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=3FC49352-37A2-452E-92F0-3DA5D02BDD76', '3FC49352-37A2-452E-92F0-3DA5D02BDD76'],
          ['Swedish U17 International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=72054EDD-0891-4AD5-B68E-B5A7835DB899', '72054EDD-0891-4AD5-B68E-B5A7835DB899'],
          ['The 29th Fajr Badminton International Challenge 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=8D445218-F62D-40CB-8BC2-9C2454D4FF28', '8D445218-F62D-40CB-8BC2-9C2454D4FF28'],
          ['10th MULTI ALARM Hungarian International Junior Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=94E45878-F696-4A48-A3B6-0BADB764EEEE', '94E45878-F696-4A48-A3B6-0BADB764EEEE'],
          ['Spanish U17 Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=AE415141-F670-4E23-B028-E69809ED4940', 'AE415141-F670-4E23-B028-E69809ED4940'],
          ['VICTOR Oceania Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=CE703801-9D7C-472D-A03F-0487801B578E', 'CE703801-9D7C-472D-A03F-0487801B578E'],
          ["All Africa Men's & Women's Team Championships 2020",
              'https://bwf.tournamentsoftware.com/sport/tournament?id=1A6378A1-00EB-405C-AB38-DE1D9C5EB339', '1A6378A1-00EB-405C-AB38-DE1D9C5EB339'],
          ["2020 European Men's & Women's Team Championships",
              'https://bwf.tournamentsoftware.com/sport/tournament?id=D912EA28-F825-469A-8FB4-5E4137C7B7D7', 'D912EA28-F825-469A-8FB4-5E4137C7B7D7'],
          ['Badminton Asia Team Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=AD641BA1-C5A5-4F18-8813-A8384C09D9AD', 'AD641BA1-C5A5-4F18-8813-A8384C09D9AD'],
          ["VICTOR Oceania Men's and Women's Team Championships 2020",
              'https://bwf.tournamentsoftware.com/sport/tournament?id=137CAD95-8371-469D-8635-E8637CC32992', '137CAD95-8371-469D-8635-E8637CC32992'],
          ['Male & Female Pan Am Team Continental Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=6D80370D-963F-4635-968E-EBF2477F6CD4', '6D80370D-963F-4635-968E-EBF2477F6CD4'],
          ['2020 European U15 Championships',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=84DA0B90-1E7E-4D3A-8E86-77D7EE3D68AF', '84DA0B90-1E7E-4D3A-8E86-77D7EE3D68AF'],
          ['All Africa Individual Championships 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=0A75BDDE-1961-4042-B4F8-748AF942AE2F', '0A75BDDE-1961-4042-B4F8-748AF942AE2F'],
          ['YONEX France U17 Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=29A5E3D7-25C7-48E3-BBBE-DB982046EC91', '29A5E3D7-25C7-48E3-BBBE-DB982046EC91'],
          ['Barcelona Spain Masters 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=E8551F1E-6F4D-491C-861A-AF65C3831B49', 'E8551F1E-6F4D-491C-861A-AF65C3831B49'],
          ['BEERLAO International Series 2020 (Cancelled)',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=D0460BCC-4056-4550-A5ED-A1C67262F0A4', 'D0460BCC-4056-4550-A5ED-A1C67262F0A4'],
          ['Austrian Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=B4CEC666-2D9C-4F6F-8F3F-63DE57484477', 'B4CEC666-2D9C-4F6F-8F3F-63DE57484477'],
          ['Uganda International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=85D8EDE9-109B-4C28-9981-8E6C4509DED8', '85D8EDE9-109B-4C28-9981-8E6C4509DED8'],
          ['DECATHLON PERFLY Italian Junior 2020 (Suspended)',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=966E2805-3517-4C66-989B-279B19586765', '966E2805-3517-4C66-989B-279B19586765'],
          ['FZ FORZA Slovak Open 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=4340E7EB-6C17-4C02-B69C-0E8B2C148129', '4340E7EB-6C17-4C02-B69C-0E8B2C148129'],
          ['YONEX Dutch Junior International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=645F6C26-8F9F-4146-8403-FA639C26511A', '645F6C26-8F9F-4146-8403-FA639C26511A'],
          ['Kenya International 2020',
              'https://bwf.tournamentsoftware.com/sport/tournament?id=9CAB388C-F79F-4020-BCDF-848A2BA2F67C', '9CAB388C-F79F-4020-BCDF-848A2BA2F67C']]


liston1 = [['PRINCESS SIRIVANNAVARI Thailand Masters 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=28E9DAAF-158B-4759-96F5-79B323E83F9C',
            '28E9DAAF-158B-4759-96F5-79B323E83F9C'],
           ['YONEX Estonian International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=82C1AB6C-5651-4E01-B529-A36C20E7866D',
            '82C1AB6C-5651-4E01-B529-A36C20E7866D'],
           ['PERODUA Malaysia Masters 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=736FF7F1-4E8D-470A-BE0B-4E3BA6DF7521',
            '736FF7F1-4E8D-470A-BE0B-4E3BA6DF7521'],
           ['RSL Swedish Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=47BF3706-AC2C-41EE-851D-2227F3DF1688',
            '47BF3706-AC2C-41EE-851D-2227F3DF1688'],
           ['VICTOR Polish Junior 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=61655554-6A72-492A-A33F-17D057395E96',
            '61655554-6A72-492A-A33F-17D057395E96'],
           ['DAIHATSU Indonesia Masters 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=1739CF17-112E-4664-829D-24650DAF4096',
            '1739CF17-112E-4664-829D-24650DAF4096'],
           ['Iceland International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=438BD7DB-30A7-4E3D-A900-BC2C91E2FE30',
            '438BD7DB-30A7-4E3D-A900-BC2C91E2FE30'],
           ['Swedish Junior 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=ABAED216-8F60-4C8B-B0B9-E1A25B4B5B5F',
            'ABAED216-8F60-4C8B-B0B9-E1A25B4B5B5F'],
           ['Swedish U17 International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=6A6FC63B-75A6-4CC8-83D1-91DBAFF63F3A',
            '6A6FC63B-75A6-4CC8-83D1-91DBAFF63F3A'],
           ['The 28th Iran Fajr International Challenge 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=05076907-BD2F-4F6A-AECC-613367365893',
            '05076907-BD2F-4F6A-AECC-613367365893'],
           ['9th MULTI ALARM Hungarian International Junior Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=B9128F5C-021C-4FFE-AA3B-1343C4A07FFA',
            'B9128F5C-021C-4FFE-AA3B-1343C4A07FFA'],
           ['VICTOR Oceania Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=C78B4E3F-87DA-49D9-A178-8BE8EC07C847',
            'C78B4E3F-87DA-49D9-A178-8BE8EC07C847'],
           ['VICTOR Oceania Junior Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=5A231A14-63EF-4A3E-9554-BCCAA382B25E',
            '5A231A14-63EF-4A3E-9554-BCCAA382B25E'],
           ['2019 European Mixed Team Championships',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=0CF2AF97-D399-4AA4-B60D-698FE28E40EB',
            '0CF2AF97-D399-4AA4-B60D-698FE28E40EB'],
           ['XXIII Pan Am Mixed Team Continental  Championships',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=7554C0F1-FC34-45EE-A204-5AEBA25187FE',
            '7554C0F1-FC34-45EE-A204-5AEBA25187FE'],
           ['VICTOR Oceania Junior Mixed Team Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=8879514A-E428-40A7-B1BC-3518FB6ADD36',
            '8879514A-E428-40A7-B1BC-3518FB6ADD36'],
           ['VICTOR Oceania Mixed Team Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=8341A3D8-C292-48C9-B76A-F9527BFFFCC8',
            '8341A3D8-C292-48C9-B76A-F9527BFFFCC8'],
           ['XIII IBERDROLA Spanish Junior International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=BCEF007D-C05B-4ACB-AA2B-3661D4F2B56D',
            'BCEF007D-C05B-4ACB-AA2B-3661D4F2B56D'],
           ['YONEX France U17 Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=B8F8BAE2-7000-4F74-B119-F353FE160C83',
            'B8F8BAE2-7000-4F74-B119-F353FE160C83'],
           ['Barcelona Spain Masters 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=277815DE-0F9F-4BB4-842F-AE0AF0496ACF',
            '277815DE-0F9F-4BB4-842F-AE0AF0496ACF'],
           ['BEER LAO International Series 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=256313FF-17D5-4518-A808-AEF21C029B38',
            '256313FF-17D5-4518-A808-AEF21C029B38'],
           ['Austrian Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=31E42D1D-ABB0-46C5-A247-927A9890DC2A',
            '31E42D1D-ABB0-46C5-A247-927A9890DC2A'],
           ['Uganda International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=5C44AE6A-5982-4828-8CB4-2038CEA330D6',
            '5C44AE6A-5982-4828-8CB4-2038CEA330D6'],
           ['YONEX Italian Junior 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=4A992ADB-1E74-43C4-83AA-801234F2F12F',
            '4A992ADB-1E74-43C4-83AA-801234F2F12F'],
           ['YONEX German Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=444F7F0E-65BC-4F1E-A602-08ED7B5962A4',
            '444F7F0E-65BC-4F1E-A602-08ED7B5962A4'],
           ['FZ FORZA Slovak Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=23011C9F-D6D9-4EC3-8D2F-D06B4B6C745C',
            '23011C9F-D6D9-4EC3-8D2F-D06B4B6C745C'],
           ['YONEX Dutch Junior International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=7B266DB0-03A3-4395-98A1-DA5ED7CCA4E7',
            '7B266DB0-03A3-4395-98A1-DA5ED7CCA4E7'],
           ['Kenya international 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=5A56305A-841C-48AD-88D3-553D311F10A1',
            '5A56305A-841C-48AD-88D3-553D311F10A1']]



def scrape():
    liston1 = [['PRINCESS SIRIVANNAVARI Thailand Masters 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=28E9DAAF-158B-4759-96F5-79B323E83F9C',
            '28E9DAAF-158B-4759-96F5-79B323E83F9C'],
           ['YONEX Estonian International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=82C1AB6C-5651-4E01-B529-A36C20E7866D',
            '82C1AB6C-5651-4E01-B529-A36C20E7866D'],
           ['PERODUA Malaysia Masters 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=736FF7F1-4E8D-470A-BE0B-4E3BA6DF7521',
            '736FF7F1-4E8D-470A-BE0B-4E3BA6DF7521'],
           ['RSL Swedish Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=47BF3706-AC2C-41EE-851D-2227F3DF1688',
            '47BF3706-AC2C-41EE-851D-2227F3DF1688'],
           ['VICTOR Polish Junior 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=61655554-6A72-492A-A33F-17D057395E96',
            '61655554-6A72-492A-A33F-17D057395E96'],
           ['DAIHATSU Indonesia Masters 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=1739CF17-112E-4664-829D-24650DAF4096',
            '1739CF17-112E-4664-829D-24650DAF4096'],
           ['Iceland International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=438BD7DB-30A7-4E3D-A900-BC2C91E2FE30',
            '438BD7DB-30A7-4E3D-A900-BC2C91E2FE30'],
           ['Swedish Junior 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=ABAED216-8F60-4C8B-B0B9-E1A25B4B5B5F',
            'ABAED216-8F60-4C8B-B0B9-E1A25B4B5B5F'],
           ['Swedish U17 International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=6A6FC63B-75A6-4CC8-83D1-91DBAFF63F3A',
            '6A6FC63B-75A6-4CC8-83D1-91DBAFF63F3A'],
           ['The 28th Iran Fajr International Challenge 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=05076907-BD2F-4F6A-AECC-613367365893',
            '05076907-BD2F-4F6A-AECC-613367365893'],
           ['9th MULTI ALARM Hungarian International Junior Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=B9128F5C-021C-4FFE-AA3B-1343C4A07FFA',
            'B9128F5C-021C-4FFE-AA3B-1343C4A07FFA'],
           ['VICTOR Oceania Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=C78B4E3F-87DA-49D9-A178-8BE8EC07C847',
            'C78B4E3F-87DA-49D9-A178-8BE8EC07C847'],
           ['VICTOR Oceania Junior Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=5A231A14-63EF-4A3E-9554-BCCAA382B25E',
            '5A231A14-63EF-4A3E-9554-BCCAA382B25E'],
           ['2019 European Mixed Team Championships',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=0CF2AF97-D399-4AA4-B60D-698FE28E40EB',
            '0CF2AF97-D399-4AA4-B60D-698FE28E40EB'],
           ['XXIII Pan Am Mixed Team Continental  Championships',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=7554C0F1-FC34-45EE-A204-5AEBA25187FE',
            '7554C0F1-FC34-45EE-A204-5AEBA25187FE'],
           ['VICTOR Oceania Junior Mixed Team Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=8879514A-E428-40A7-B1BC-3518FB6ADD36',
            '8879514A-E428-40A7-B1BC-3518FB6ADD36'],
           ['VICTOR Oceania Mixed Team Championships 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=8341A3D8-C292-48C9-B76A-F9527BFFFCC8',
            '8341A3D8-C292-48C9-B76A-F9527BFFFCC8'],
           ['XIII IBERDROLA Spanish Junior International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=BCEF007D-C05B-4ACB-AA2B-3661D4F2B56D',
            'BCEF007D-C05B-4ACB-AA2B-3661D4F2B56D'],
           ['YONEX France U17 Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=B8F8BAE2-7000-4F74-B119-F353FE160C83',
            'B8F8BAE2-7000-4F74-B119-F353FE160C83'],
           ['Barcelona Spain Masters 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=277815DE-0F9F-4BB4-842F-AE0AF0496ACF',
            '277815DE-0F9F-4BB4-842F-AE0AF0496ACF'],
           ['BEER LAO International Series 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=256313FF-17D5-4518-A808-AEF21C029B38',
            '256313FF-17D5-4518-A808-AEF21C029B38'],
           ['Austrian Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=31E42D1D-ABB0-46C5-A247-927A9890DC2A',
            '31E42D1D-ABB0-46C5-A247-927A9890DC2A'],
           ['Uganda International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=5C44AE6A-5982-4828-8CB4-2038CEA330D6',
            '5C44AE6A-5982-4828-8CB4-2038CEA330D6'],
           ['YONEX Italian Junior 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=4A992ADB-1E74-43C4-83AA-801234F2F12F',
            '4A992ADB-1E74-43C4-83AA-801234F2F12F'],
           ['YONEX German Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=444F7F0E-65BC-4F1E-A602-08ED7B5962A4',
            '444F7F0E-65BC-4F1E-A602-08ED7B5962A4'],
           ['FZ FORZA Slovak Open 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=23011C9F-D6D9-4EC3-8D2F-D06B4B6C745C',
            '23011C9F-D6D9-4EC3-8D2F-D06B4B6C745C'],
           ['YONEX Dutch Junior International 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=7B266DB0-03A3-4395-98A1-DA5ED7CCA4E7',
            '7B266DB0-03A3-4395-98A1-DA5ED7CCA4E7'],
           ['Kenya international 2019',
            'https://bwf.tournamentsoftware.com/sport/tournament?id=5A56305A-841C-48AD-88D3-553D311F10A1',
            '5A56305A-841C-48AD-88D3-553D311F10A1']]
    
    Words = ["suspended", "cancelled", "junior", "postponed", "u17","u15"]
    for j in range(len(liston1)):
        text_io = liston1[j][0].lower()
        if not any(x in text_io for x in Words):
            if "team" in text_io:
                print(liston1[j][1], "Team Links")
                get_Ttourn_info(liston1[j][1])
            else:
                get_Ptourn_info(liston1[j][1])


def draw_extract():
    for draw in liston:
        name = draw[0]
        if 'Team' in name:
            Team_draw = get_draws(draw[2])
            for item in Team_draw:
                draw_nam = item[0].split('–')[1:3]
                drname = " "
                drname = drname.join(draw_nam)
                Draw_Type = item[1]
                Draw_Url = item[2]
                Match_Type = "Team"
                Draw_evkey = BWFTournament.objects.get(tourn_id=draw[2])
                #Team Draw entry
                Tdraw, Tdraw_ = Draw.objects.get_or_create(Draw_event_key=Draw_evkey,draw_name=drname ,draw_type=Draw_Type, draw_url=Draw_Url, match_type=Match_Type)

        else:
            Player_draw = get_draws(draw[2])
            for item in Player_draw:
                Draw_Name = item[0].split('-')[0]
                Draw_Type = item[1].split(' ')[0]
                Draw_Url = item[2]
                Match_Type = "Player"
                Draw_evkey = BWFTournament.objects.get(tourn_id=draw[2])
                Tdraw, Tdraw_ = Draw.objects.get_or_create(Draw_event_key=Draw_evkey, draw_name=Draw_Name , draw_type=Draw_Type, draw_url=Draw_Url, match_type=Match_Type)


        
