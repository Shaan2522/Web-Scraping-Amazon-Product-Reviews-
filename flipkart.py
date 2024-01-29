import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136'}

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [f"https://www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYSCIIOB&marketplace=FLIPKART&page={i}" for i in range(1, 11)]
    l1 = []
    l2 = []
    new_data = {}

    async with aiohttp.ClientSession(headers=headers) as session:
        htmls = await asyncio.gather(*[fetch(session, url) for url in urls])
        for html in htmls:
            site = BeautifulSoup(html, features="lxml")

            # Parsing code
            username = site.findAll("p", {"class" : "_2sc7ZR _2V5EHH"})
            review = site.findAll("div", {"class" : "t-ZTKy"})

            for i in range(len(review)):
                name = str(username[i]).split(">")[1].split("<")[0]
                rev = str(review[i]).split("class=\"\">")[1].split("<")[0]
                l1.append(str(name))
                l2.append(str(rev))

        for k in range(len(l1)):
            new_data[l1[k]] = l2[k]

    # top 100 comments
    with open("m4.json", "w") as f:
        json.dump(new_data, f, indent = 2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())