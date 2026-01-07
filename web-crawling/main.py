from bs4 import BeautifulSoup
import requests
import os
from utils import enter_websites_url,read_all_website_url
from website import  website_list,website_keywords_list


# headers = {
#     "User-Agent": "KimiNoNawa/1.0"
# }



results=[]

enter_websites_url(website_list)
read_all_website_url()


website_code = requests.get(website_list[13])


def scrap_json():
    res = website_code.json()

    for item in res:
        results.append(item["title"])

scrap_json() if (website_code.headers.get('Content-Type').split(';')[0] == "application/json") else scrap_html()
    
def scrap_html():

    soup = BeautifulSoup(website_code, 'html.parser')

    print(type(website_code))

    words_count_dict ={}

    for i in soup.find_all():
        text = i.get_text()
        if text in website_keywords_list:
            results.append(text)








