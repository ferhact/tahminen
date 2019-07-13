# -*- coding: utf-8 -*-
import scrapy
import csv
from datetime import datetime
from tahminen.items import MerkezItem, GundereceItem, MerkezdeGundereceItem
from scrapy_splash import SplashRequest

class MerkezdegunderecemgmSpider(scrapy.Spider):
  name = 'spiders/MerkezdeGundereceMGM'
  allowed_domains = ['mgm.gov.tr']

  merkezler = []
  mgm_anaurl = 'https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il='

  def start_requests(self):
       with open("db/mgm/merkezler.csv") as csvfile:
           reader = csv.reader(csvfile) # change contents to floats
           for row in reader: # each row is a list
               merkez = MerkezItem()
               merkez['id'] = int(row[0])
               merkez['isim'] = row[1]
               merkez['isimUzun'] = row[2]
               merkez['ilMerkezi'] = False
               if row[3]=='kafz':
                 merkez['kafz'] = True
               else
                 merkez['kafz'] = False
               self.merkezler.append(merkez)
               url = self.mgm_anaurl + '' + merkez['isim']
               yield SplashRequest(url, callback = self.parse, 
          args={
          # optional; parameters passed to Splash HTTP API
          'wait': 1,

          # 'url' is prefilled from request url
          # 'http_method' is set to 'POST' for POST requests
          # 'body' is set to request body for POST requests
            },
            # endpoint='render.json', # optional; default is render.html
            # splash_url='<url>',     # optional; overrides SPLASH_URL
            # slot_policy=scrapy_splash.SlotPolicy.PER_DOMAIN,  # optional
            )
   
  def convertDate(self, d_str):
      d_list = d_str.split()
      aylar = {'Ocak': 1, 'Şubat': 2, 'Mart': 3, 'Nisan': 4, 'Mayıs': 5, 'Haziran': 6, 'Temmuz': 7, 'Ağustos': 8, 'Eylül': 9, 'Ekim': 10, 'Kasım': 11, 'Aralık': 12 }
      ay = aylar.get(d_list[1], 'default')
      date_string = d_list[0] + "/" + str(ay) + "/" + "2019"
      date_obj = datetime.strptime(date_string, "%d/%m/%Y")
      return date_obj.strftime("%d/%m/%Y")

  def getPlaka(self, il_adi):
      for x in self.merkezler:
          if x['isim'] == il_adi:
              return x['id']
      return 0

  def parse(self, response):
       
      mgd = MerkezdeGundereceItem()
       
      try:

        mgd['kayit_url'] = response.url 
        mgd['kayit_tarih'] = datetime.today().strftime('%d/%m/%Y-%H:%M:%S') 
         
        merkez_adi = response.css('h1#sfB::text').extract_first().strip()
        mgd['merkez_adi'] = merkez_adi
        mgd['merkez_id'] = self.getPlaka(merkez_adi)

        tarihler = response.css("#_4_5gunluk .ng-binding:nth-child(1)::text").getall()
        print(tarihler)
        maxler = response.css(".xTt::text").getall()
        minler = response.css(".nTt::text").getall()
        gler = response.css(".Gd::text").getall()
        print(maxler)
        print(minler)
        gd1 = GundereceItem()
        gd1['gun'] = self.convertDate(tarihler[0])
        gd1['max'] = maxler[0]
        gd1['min'] = minler[0]
        gd1['aciklama'] = "EN_YUKSEK"
        gd1['min_g'] = gler[0]
        gd1['max_g'] = gler[1]
        gd1['min_gort'] = gler[2]
        gd1['max_gort'] = gler[3]
        gd2 = GundereceItem()
        gd2['gun'] = self.convertDate(tarihler[1])
        gd2['max'] = maxler[1]
        gd2['min'] = minler[1]
        gd2['aciklama'] = "EN_YUKSEK"
        gd2['min_g'] = gler[4]
        gd2['max_g'] = gler[5]
        gd2['min_gort'] = gler[6]
        gd2['max_gort'] = gler[7]
        gd3 = GundereceItem()
        gd3['gun'] = self.convertDate(tarihler[2])
        gd3['max'] = maxler[2]
        gd3['min'] = minler[2]
        gd3['min_g'] = gler[8]
        gd3['max_g'] = gler[9]
        gd3['min_gort'] = gler[10]
        gd3['max_gort'] = gler[11]
        gd3['aciklama'] = "EN_YUKSEK"
        gd4 = GundereceItem()
        gd4['gun'] = self.convertDate(tarihler[3])
        gd4['max'] = maxler[3]
        gd4['min'] = minler[3]
        gd4['min_g'] = gler[12]
        gd4['max_g'] = gler[13]
        gd4['min_gort'] = gler[14]
        gd4['max_gort'] = gler[15]
        gd4['aciklama'] = "EN_YUKSEK"
        gd5 = GundereceItem()
        gd5['gun'] = self.convertDate(tarihler[4])
        gd5['max'] = maxler[4]
        gd5['min'] = minler[4]
        gd5['min_g'] = gler[16]
        gd5['max_g'] = gler[17]
        gd5['min_gort'] = gler[18]
        gd5['max_gort'] = gler[19]
        gd5['aciklama'] = "EN_YUKSEK"

        mgd['gunderece'] = [gd1,gd2,gd3,gd4,gd5]

        yield {
          'merkezde_gunderece' : mgd, 
        }

      except Exception as e:
        raise
      else:
        pass
      finally:
        pass     
