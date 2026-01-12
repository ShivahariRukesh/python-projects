from bs4 import BeautifulSoup
import requests
import os
from utils import enter_websites_url,read_all_website_url,scrap_json
from website import  website_list,website_keywords_list


# headers = {
#     "User-Agent": "KimiNoNawa/1.0"
# }



results={}
website_dir={}

# enter_websites_url(website_list)
read_all_website_url()


print("Scraping the web.....\nPlease stay tuned!!!")





                

# Trying to crawl and scrap  first two  websites

for i in website_list[:2]:

    res = requests.get(i)

    scrap_json(i,res,results,website_dir) if (res.headers.get('Content-Type').split(';')[0] == "application/json") else scrap_html(i,res,results,website_dir)
###
    
print("Successfully extracted the web. Here's the result\n")

# Here need to remove new line formatter symbol
print(website_dir)







