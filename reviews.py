from bs4 import BeautifulSoup
import requests
import lxml

import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

link = f"https://www.amazon.in/Amozo-Cover-iPhone-Polycarbonate-Transparent/dp/B09J2MM5C6/ref=sr_1_3?keywords=iphone+cover&qid=1705170057&sr=8-3"
print(link)

site = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")

price_data = site.findAll("span", {"class" : "a-profile-name"})
name_data = site.findAll("div", {"data-hook" : "review-collapsed"})


new_data = {}

for i in range(len(name_data)):
    name_med = str(name_data).split("span>")[1].split("</span")[0]
    price = str(price_data[i]).split("name\">")[1].split("</span")[0]
    new_data[str(price)] = str(name_med)

with open("m1.json", "w") as f:
    json.dump(new_data, f, indent = 2)