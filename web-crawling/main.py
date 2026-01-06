from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import csv
from website import  website_list


fields = ['no','website_url']
load_dotenv()

headers = {
    "User-Agent": "KimiNoNawa/1.0"
}

def enter_websites_url():
    with open("websites.csv", "w", newline='') as csv_website_file:
        writer = csv.writer(csv_website_file)
        writer.writerow(fields)
        for index,i in enumerate(website_list):
            writer.writerow([index,i+1])



website_url = os.getenv('URL')
website_code = requests.get(website_url, headers=headers).text
soup = BeautifulSoup(website_code, 'html.parser')


words_list =[]
words_count_dict ={}

for i in soup.find_all(title=True):
    title_sentence=i.text.lower()

    for word in title_sentence.split():
        words_list.append(word)

special_characters_string = "!@#$%^&*()_-+={[}]|\\;:\"<>?/.,"
for word in words_list:
    for s in special_characters_string:
        if s in word:
            word.replace(s,'')  

        if (not word in words_count_dict):
            words_count_dict[word] = 1
        else:
            words_count_dict[word] +=1


# To show all the repeated words of the text which is inside the element that has "title" attribute

for word in words_count_dict:
    print(f"\n The word \"{word}\"'s count is {words_count_dict[word]}")    





