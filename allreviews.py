from bs4 import BeautifulSoup
import requests
import lxml

import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

l1 = []
l2 = []
new_data = {}
link = f"https://www.amazon.in/Amozo-Cover-iPhone-Polycarbonate-Transparent/product-reviews/B09J2MM5C6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=1"
site = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")

top = site.findAll("span", {"class" : "a-size-base review-title a-text-bold"})
# print(top)
top_comment = site.findAll("div", {"class" : "a-row a-spacing-top-mini"})
print(top_comment)
for i in range(2):
    t = str(top[i]).split("-title\">")[1].split("<")[0]
    b = str(top_comment[i]).split("base\">")[1].split("<")[0]
    if(i==0):
        new_data["TOP POSITIVE COMMENTS - "] = str(t), str(b)
    elif(i==1):
        new_data["TOP CRITICAL COMMENTS - "] = str(t), str(b)

for page_num in range(1,11):
    link = f"https://www.amazon.in/Amozo-Cover-iPhone-Polycarbonate-Transparent/product-reviews/B09J2MM5C6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber={page_num}"
    print(link)

    site = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")

    username = site.findAll("span", {"class" : "a-profile-name"})
    review = site.findAll("div", {"class" : "a-row a-spacing-small review-data"})

    for i in range(len(review)):
        name = str(username[i]).split(">")[1].split("<")[0]
        rev = str(review[i]).split("span>")[1].split("<")[0]
        l1.append(str(name))
        l2.append(str(rev))

    top = site.findAll("span", {"class" : "a-size-base review-title a-text-bold"})
    top_comment = site.findAll("span", {"class" : "a-size-base"})
    critical_voice = site.findAll("span", {"class" : "a-size-base review-title a-text-bold"})
    bottom_comment = site.findAll("span", {"class" : "a-size-base"})

for k in range(len(l1)):
    new_data[l1[k]] = l2[k]


# top 100 comments
with open("m2.json", "w") as f:
    json.dump(new_data, f, indent = 2)