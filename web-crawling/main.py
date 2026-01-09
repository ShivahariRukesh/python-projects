from bs4 import BeautifulSoup
import requests
import os
from utils import enter_websites_url,read_all_website_url
from website import  website_list,website_keywords_list


# headers = {
#     "User-Agent": "KimiNoNawa/1.0"
# }



results={}

enter_websites_url(website_list)
read_all_website_url()


res = requests.get(website_list[8])


def scrap_json():
    res_json = res.json()

    for item in res_json:
        results.append(item["title"])

def scrap_html():
    website_code = res.text
    soup = BeautifulSoup(website_code, 'html.parser')

    print(type(website_code))


    for i in soup.find_all():
        text = i.get_text()
        for word in text.split(' '):
            if word in website_keywords_list:
    
                if not word in results:
                    results[word] = []
                # results[word].append(text[:29])
                results[word] = [*results[word], text[:29]]
                    

scrap_json() if (res.headers.get('Content-Type').split(';')[0] == "application/json") else scrap_html()
    

print(results)







