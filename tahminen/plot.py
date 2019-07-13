import numpy as np
import pandas as pd
from bokeh.core.properties import value
from bokeh.plotting import figure, show, output_file
from bokeh.palettes import brewer
from bokeh.models.annotations import Title
from datetime import datetime
import os 
from lxml import etree
         
path='db/mgm/2019/temmuz'

title = ""

merkez_adi = ""

def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None
 
#dfcols = ['il', 'gun', 'gercek', '-1gun', '-2gun', '-3gun','-4gun','-5gun']
dfcols = ['gun', 'max', 'max_gort', 'max_g', 'min', 'min_gort', 'min_g']
df_xml = pd.DataFrame(columns=dfcols)

for filename in os.listdir(path):
    if filename.endswith(".xml"):
        # TODO: dosya 1 kere açılıp okunsun her merkez için açılmasın
        #for merkez in self.merkezler:
        root = etree.parse(path +'/'+ filename)
        for merkezde_gunderece in root.xpath("item/merkezde_gunderece[merkez_id=34]"): 
            
            merkez_adi = getvalueofnode(merkezde_gunderece.find('merkez_adi'))
            kayit_tarih_temp = getvalueofnode(merkezde_gunderece.find('kayit_tarih'))
            if (kayit_tarih_temp!=None):
                kayit_tarih = datetime.strptime(kayit_tarih_temp, '%d/%m/%Y-%H:%M:%S')
                for value in merkezde_gunderece.find('gunderece'):
                    #print(etree.tostring(value))
                    temp = getvalueofnode(value.find('gun'))
                    if (temp!=None):
                        gun = datetime.strptime(temp, "%d/%m/%Y")
                    else:
                        gun = None
                    temp = getvalueofnode(value.find('max'))
                    if (temp!=None):
                        max = int(temp)
                    else:
                        max = None
                    temp = getvalueofnode(value.find('max_gort'))
                    if (temp!=None):
                        max_gort = float(temp.replace(",", "."))
                    else:
                        max_gort = None
                    temp = getvalueofnode(value.find('max_g'))
                    if (temp!=None):
                        max_g = float(temp.replace(",", "."))
                    else:
                        max_g = None
                    temp = getvalueofnode(value.find('min'))
                    if (temp!=None):
                        min = int(temp)
                    else:
                        min = None
                    temp = getvalueofnode(value.find('min_gort'))
                    if (temp!=None):
                        min_gort = float(temp.replace(",", "."))
                    else:
                        min_gort = None
                    temp = getvalueofnode(value.find('min_g'))
                    if (temp!=None):
                        min_g = float(temp.replace(",", "."))
                    else:
                        min_g = None
                    print(filename + "->" + str(kayit_tarih) + "->" + str(gun) + " -> " + str(max) + " -> [" + str(max_gort)+ "," +  str(max_g) + "]" + " -> " + str(min) + " -> [" + str(min_gort)+ "," +  str(min_g) + "]")
                    if (gun is not None):
                        diff = gun - kayit_tarih
                        if(diff.days == 0 ):
                            df_xml = df_xml.append(pd.Series([gun, max, max_gort, max_g, min, min_gort, min_g], index=dfcols),ignore_index=True)

df_xml.sort_values(by='gun',inplace=True)
print(df_xml)
p = figure(plot_width=800, plot_height=400,x_axis_type="datetime", x_range=(datetime.strptime("08/07/2019", "%d/%m/%Y"), datetime.strptime("15/07/2019", "%d/%m/%Y")), y_range=(20, 40))
p.grid.minor_grid_line_color = '#eeeeee'
#p.varea_stack(stackers=['max_gort', 'max_g'], x='gun', color=('grey','lightgrey'), legend=['Geçmiş en yüksek', 'Geçmiş En yüksek ort.'], source=df_xml)
w = 12*60*60*1000 # half day in ms
p.circle_x(x='gun', y='max', size=20, color="#DD1C77", fill_alpha=0.2, source=df_xml)
p.circle_x(x='gun', y='min', size=20, color="blue", fill_alpha=0.2, source=df_xml)
#p.vbar(x='gun', top='max', width=5000, bottom=0, color="blue", source=df_xml)
#p.line(x='gun', y='max_gort', color="red", source=df_xml)
p.segment(x0='gun', y0='max_gort', x1='gun', y1='min_gort', color="black", source=df_xml)
t = Title()
t.text = merkez_adi
p.title = t
#p.vline_stack(stackers=['max','max_gort'] , x='gun', color=('red','blue') ,  source=df_xml)
output_file('stacked_area.html')

# reverse the legend entries to match the stacked order
#p.legend[0].items.reverse()

#color=brewer['Spectral'][1], legend=[value(x) for x in dfcols],
show(p)


 #'''\
#		<?xml version="1.0"?>
#		<items>
#		<item><merkezde_gunderece><kayit_url>https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Bitlis</kayit_url><kayit_tarih>10/07/2019-12:04:51</kayit_tarih><merkez_adi>Bitlis</merkez_adi><merkez_id>13</merkez_id><gunderece><value><gun>10/07/2019</gun><max>28</max><min>14</min><aciklama>EN_YUKSEK</aciklama><min_g>9</min_g><max_g>34,4</max_g><min_gort>14,1</min_gort><max_gort>30</max_gort></value><value><gun>11/07/2019</gun><max>30</max><min>15</min><aciklama>EN_YUKSEK</aciklama><min_g>8,7</min_g><max_g>35,3</max_g><min_gort>14,4</min_gort><max_gort>30,2</max_gort></value><value><gun>12/07/2019</gun><max>29</max><min>16</min><min_g>11</min_g><max_g>35</max_g><min_gort>15,9</min_gort><max_gort>30,8</max_gort><aciklama>EN_YUKSEK</aciklama></value><value><gun>13/07/2019</gun><max>27</max><min>15</min><min_g>11</min_g><max_g>34,6</max_g><min_gort>15,8</min_gort><max_gort>31</max_gort><aciklama>EN_YUKSEK</aciklama></value><value><gun>14/07/2019</gun><max>27</max><min>14</min><min_g>9,4</min_g><max_g>36,2</max_g><min_gort>15,7</min_gort><max_gort>31,2</max_gort><aciklama>EN_YUKSEK</aciklama></value></gunderece></merkezde_gunderece></item>
#		</items>
#		root = etree.XML(xml_content.strip())
#		print(etree.tostring(root)) '''


# #out_df = parse_XML(filename, ["name", "email", "grade", "age"])
# def parse_XML(xml_file, df_cols): 
#     """Parse the input XML file and store the result in a pandas DataFrame 
#     with the given columns. The first element of df_cols is supposed to be 
#     the identifier variable, which is an attribute of each node element in 
#     the XML data; other features will be parsed from the text content of 
#     each sub-element. """
    
#     xtree = et.parse(xml_file)
#     xroot = xtree.getroot()
#     out_df = pd.DataFrame(columns = df_cols)
    
#     for node in xroot: 
#         res = []
#         res.append(node.attrib.get(df_cols[0]))
#         for el in df_cols[1:]: 
#             if node is not None and node.find(el) is not None:
#                 res.append(node.find(el).text)
#             else: 
#                 res.append(None)
#         out_df = out_df.append(pd.Series(res, index = df_cols), ignore_index=True)
        
#     return out_df