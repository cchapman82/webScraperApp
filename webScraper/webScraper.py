import requests
from bs4 import BeautifulSoup
import re
import pandas

r = requests.get("https://www.century21.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class" : "property-card-primary-info"})

all[0]

#page_nr = soup.find_all("a", {"clas": "Page"})[-1].text find last page in series of web pages
#all[0].find("a", {"class":"listing-price"}).text.replace("\n", "").replace(" ","")
#base_url = "http..." -- crawling through web pages
#for page in range(0, int(page_nr)*10, 10):
 #   print(base_url+str(page))
  #  r= requests.get(base_url+str(page))
   # c= r.content
    #soup = BeautifulSoup(c."html.parser")
 #all = soup.find_all("dif, {"class" : ""property-card-primary-info""}")
l = []
for item in all:
    d = {}
    d["Address"] = item.find("div", {"class":"property-address"}).text.replace("\n", "").strip()
    d["Locality"] = item.find("div", {"class":"property-city"}).text.replace("\n", "").strip()
    d["Price"]=item.find("a", {"class":"listing-price"}).text.replace("\n", "").replace(" ","")
    try:
        d["Beds"] = item.find("div", {"class":"property-beds"}).find("strong").text
    except:
        d["Beds"] = None
    try:
        d["Area"] = item.find("div", {"class":"property-sqft"}).find("strong").text
    except:
        d["Area"] = None
    try:
        d["Baths"] = item.find("div", {"class":"property-baths"}).find("strong").text
    except:
        d["Baths"] = None
    try:
        d["Half-Baths"] = item.find("div", {"class":"property-half-baths"}).find("strong").text
    except:
        d["Half-Baths"] = None
    l.append(d)
df = pandas.DataFrame(l)
df.to_csv("Output.csv")
print(df)