from bs4 import BeautifulSoup
import requests
import os
from utils import enter_websites_url,read_all_website_url
from website import  website_list,website_keywords_list


# headers = {
#     "User-Agent": "KimiNoNawa/1.0"
# }



results={}

# enter_websites_url(website_list)
read_all_website_url()


print("Scraping the web.....\nPlease stay tuned!!!")

def scrap_json(i):
    res_json = res.json()
    website_name =(i.split('/')[2]).split('.')[0]
    print(website_name)
    for item in res_json:
        results.append(item["title"])

def scrap_html(i):
    website_code = res.text
    soup = BeautifulSoup(website_code, 'html.parser')
    website_name =(i.split('/')[2]).split('.')[0]
    print(website_name)



    for i in soup.find_all():
        text = i.get_text()
        for word in text.split(' '):
            if word in website_keywords_list:
    
                if not word in results:
                    results[word] = []
                # results[word].append(text[:29])
                results[word] = [*results[word], text[:29]]

                

# Trying to crawl and scrap all the website

for i in website_list:

    res = requests.get(i)

    scrap_json(i) if (res.headers.get('Content-Type').split(';')[0] == "application/json") else scrap_html(i)
###
    
print("Successfully extracted the web. Here's the result\n")
# print(results)







