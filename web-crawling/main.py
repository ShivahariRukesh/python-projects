from bs4 import BeautifulSoup
import requests
import os
from website import  website_list
from utils import enter_websites_url,read_all_website_url

fields = ['no','website_url']
extracted_website_list=[]
# headers = {
#     "User-Agent": "KimiNoNawa/1.0"
# }





read_all_website_url(extracted_website_list)


website_code = requests.get(website_list[0]).text
print(website_code)
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




