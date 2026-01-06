import csv
def enter_websites_url():
    with open("websites.csv", "w", newline='') as csv_website_file:
        csv_writer = csv.writer(csv_website_file)
        csv_writer.writerow(fields)
        for index,i in enumerate(website_list):
            csv_writer.writerow([index,i+1])


def read_all_website_url(extracted_website_list):
    with open("websites.csv", "r") as csv_website_file:
        csv_reader = csv.reader(csv_website_file)
        next(csv_reader)

        for row in csv_reader:
           extracted_website_list.append(row[1])




if __name__ =="__main__":
    enter_websites_url()
    read_all_website_url()