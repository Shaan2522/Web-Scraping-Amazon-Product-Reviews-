from bs4 import BeautifulSoup
import requests
import lxml

import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

link = f"https://www.amazon.in/Amozo-Cover-iPhone-Polycarbonate-Transparent/dp/B09J2MM5C6/ref=sr_1_3?keywords=iphone+cover&qid=1705170057&sr=8-3"
print(link)

site = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")

username = site.findAll("span", {"class" : "a-profile-name"})
review = site.findAll("div", {"class" : "a-row a-spacing-small review-data"})


new_data = {}

for i in range(len(review)):
    name = str(username[i]).split(">")[1].split("<")[0]
    rev = str(review[i]).split("span>")[1].split("<")[0]
    new_data[str(name)] = str(rev)
    # print(str(rev), str(name))

with open("m2.json", "w") as f:
    json.dump(new_data, f, indent = 2)
