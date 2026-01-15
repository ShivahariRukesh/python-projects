import csv
from bs4 import BeautifulSoup

from website import website_keywords_list


fields = ['no','website_url']
extracted_website_list=[]


def enter_websites_url(website_list):
    with open("websites.csv", "w", newline='') as csv_website_file:
        csv_writer = csv.writer(csv_website_file)
        csv_writer.writerow(fields)
        for index,i in enumerate(website_list):
            csv_writer.writerow([index+1,i])


def read_all_website_url():
    with open("websites.csv", "r") as csv_website_file:
        csv_reader = csv.reader(csv_website_file)
        next(csv_reader)

        for row in csv_reader:
           extracted_website_list.append(row[1])


def scrap_json(website_url,res,results,website_dir):
    res_json = res.json()
    website_name =(website_url.split('/')[2]).split('.')[1] + 'json'
    print(website_name)
    if not website_name in website_dir:
        website_dir[website_name] =[]
    for item in res_json:
        website_dir[website_name].append(item["title"])





def scrap_html(website_url,res,results,website_dir):
    website_code = res.text
    soup = BeautifulSoup(website_code, 'html.parser')
    website_name =(website_url.split('/')[2]).split('.')[0]
    content = soup.find_all()[0]
    print(website_name)

    # print(soup.find_all())
    # cc=""
    # for i in soup.find_all()[0].text:
    #     if (i == "\n"):
    #         cc =cc
    #     else:
    #         cc = cc + i

    # print(cc)

    regex_symbols = set('\r|()\n')
    filtered_text=''.join(ch for ch in content.text if ch not in regex_symbols)
    filtered_text_list = filtered_text.split(' ')
    # print(filtered_text_list)

    for word,index in enumerate(filtered_text_list):
        if word in website_keywords_list:
            if not word in results:
                results[word] = []
            # results[word].append(text[:29])
            results[word] = [*results[word], word + filtered_text_list[index+1]]
            

        website_dir[website_name] = results





if __name__ =="__main__":
    enter_websites_url()
    read_all_website_url()
    scrap_json()
    scrap_html()    