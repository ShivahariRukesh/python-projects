import csv

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


def scrap_json(i,res,results,website_dir):
    res_json = res.json()
    website_name =(i.split('/')[2]).split('.')[0]
    print(website_name)

    for item in res_json:
         results.append(item["title"])
    website_dir[website_name] = results

if __name__ =="__main__":
    enter_websites_url()
    read_all_website_url()
    scrap_json()




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

    website_dir[website_name] = results