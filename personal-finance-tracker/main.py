import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = 'finance.csv'
    FINANCE_CSV_COLUMNS = ["date","category","amount","description"]
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            print("csv file was not found when initializing so creating one ......")
            df = pd.DataFrame(columns =["date","category","amount","description"])
            df.to_csv(cls.CSV_FILE,index=False)
            print("....Successfully create the csv file")

    @classmethod
    def   write_to_csv(cls,category,amount,description):
        try:
            current_time = datetime.now()
            new_record ={
                "date":"{} {}:{}:{}".format(current_time.date(),current_time.hour, current_time.minute,current_time.second),
                "category":category,
                "amount":amount,
                "description":description
            }

            with open(cls.CSV_FILE, "a") as csv_file:
                csv_dict_writer = csv.DictWriter(csv_file, cls.FINANCE_CSV_COLUMNS)
                csv_dict_writer.writerow(new_record)
                print("An record is written successfully")

        except err:
            print("Error while writing the data to the csv file\t",err)


obj1 = CSV()
obj1.initialize_csv()

obj1.write_to_csv("income",1000000000,"Lucrative outcome from concert in europe")
