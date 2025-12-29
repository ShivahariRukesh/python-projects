import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from utils import enter_date,enter_amount,enter_category,enter_description,DATE_FORMAT


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
    def   write_to_csv(cls,date,category,amount,description):
        try:
            current_time = datetime.now()
            new_record ={
                # "date":"{} {}:{}:{}".format(current_time.date(),current_time.hour, current_time.minute,current_time.second),
               "date":date,
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

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=DATE_FORMAT)
        start_date = datetime.strptime(start_date, DATE_FORMAT)
        end_date = datetime.strptime(end_date, DATE_FORMAT)

        mask = (df["date"] >= start_date) & (df["date"]<= end_date)

        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("The transactions was not found in the given data range")

        else:
            print(f"Lists of transactions from {start_date.strftime(DATE_FORMAT)} to {end_date.strftime(DATE_FORMAT)}")

            print(filtered_df.to_string(index=False, formatters={"date":lambda x:x.strftime(DATE_FORMAT)}))
            return filtered_df




def graph_plot_transaction_records(data):
    df = data
    print("Th data", data)
    df.set_index("date", inplace=True)

    income_df = (df[df["category"]== "Income"].resample("D").sum().reindex(df.index, fill_value=0))
    expense_df = (df[df["category"]== "Expense"].resample("D").sum().reindex(df.index, fill_value=0))
    transfer_df = (df[df["category"]== "Transfer"].resample("D").sum().reindex(df.index, fill_value=0))


    plt.figure(figsize=(20,20))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.plot(transfer_df.index, transfer_df["amount"], label="Transfer", color="y")
   
    plt.title("Graph Tracking of your Income, Expense and Transfer")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.legend()
    plt.show()

def add_transaction():
    obj1 = CSV()
    obj1.initialize_csv()
    obj1.write_to_csv(enter_date(),enter_category(),enter_amount(),enter_description())
 
def main():
    while True:
        print("1.Add a new transaction")
        print("2. View transaction and summary within a date range")
        print("3. Exit")

        option = input("Enter you option from above:\t")

        if( option == "1"):
            add_transaction()
        elif(option =="2"):
            transaction_results =CSV.get_transactions("2019-01-22","2026-01-21")
            if (input("There is the graph plotted for your financial transaction records. So do you wanna see it with great visuals? (Y/N)").upper()=="Y"):
                graph_plot_transaction_records(transaction_results)
        elif option == "3":
            print("Thank you! See you around")
            break
        else:
            print("Invalid option. Please enter 1/2/3 according to the below options")

if __name__=="__main__":
    main()