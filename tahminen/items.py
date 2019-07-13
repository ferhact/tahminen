# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MerkezItem(scrapy.Item):
  
  isim = scrapy.Field()
  id = scrapy.Field()
  isimUzun = scrapy.Field()
  ilMerkezi = scrapy.Field()
  kafz = scrapy.Field()

#  def __repr__(self):
#    return "Merkez([{0}:{1}:{2}:{3}])".format(self.plaka, self.isim, self.isimUzun, self.ilMerkezi)
  
class MerkezdeGundereceItem(scrapy.Item):
  merkez_id = scrapy.Field()
  merkez_adi = scrapy.Field()
  kayit_url = scrapy.Field()
  kayit_tarih = scrapy.Field()
  gunderece = scrapy.Field()

class GundereceItem(scrapy.Item):
  gun = scrapy.Field()
  max = scrapy.Field()
  min = scrapy.Field()
  aciklama = scrapy.Field()
  min_g = scrapy.Field()
  max_g = scrapy.Field()
  min_gort = scrapy.Field()
  max_gort = scrapy.Field()

   
# class TahminItem(scrapy.Item):
  
#   hedef_tarih = scrapy.Field()
#   merkezi = scrapy.Field()
#   deger = scrapy.Field()
#   tahmin_kaynagi = scrapy.Field()
#   uzaklik = scrapy.Field()

#  def __repr__(self):
#   return "Tahmin([{0}:{1}:{2}:{3}:{4}])".format(self.hedefTarih, self.merkezi, self.deger, self.tahminKaynagi,self.uzaklik)

