from bs4 import BeautifulSoup
import requests
import lxml

import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136'}

l1 = []
l2 = []
new_data = {}
link = f"https://www.amazon.in/Amozo-Cover-iPhone-Polycarbonate-Transparent/product-reviews/B09J2MM5C6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=1"
site = BeautifulSoup(requests.get(link,headers=headers).content,features="lxml")

title = site.findAll("a", {"href" : "/Amozo-Cover-iPhone-Polycarbonate-Transparent/dp/B09J2MM5C6/ref=cm_cr_arp_d_product_top?ie=UTF8"})
for i in range(1):
    t = str(title[i]).split(">")[1].split("<")[0]
new_data["PRODUCT NAME - "] = str(t)

prod_link = site.findAll("a", {"data-hook" : "product-link"})
z = "https://www.amazon.in/"
z += str(prod_link).split("href=\"")[1].split("\">")[0]
new_data["link to the product - "] = str(z)

rating = site.findAll("span", {"class" : "a-size-medium a-color-base"})
rating = str(rating).split("text\">")[1].split("<")[0]
total_ratings = site.findAll("span", {"class" : "a-size-base a-color-secondary"})
total_ratings = str(total_ratings).split("secondary\">")[1].split("<")[0]
new_data[rating] = total_ratings

top = site.findAll("span", {"class" : "a-size-base review-title a-text-bold"})
top_comment = site.findAll("div", {"class" : "a-row a-spacing-top-mini"})
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
