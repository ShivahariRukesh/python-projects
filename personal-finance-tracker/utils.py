from datetime import datetime
DATE_FORMAT = "%Y-%m-%d"
CATEGORY_OPTIONS = {'I':"Income",'E':"Expense",'T':"Transfer"}

def enter_date():
    date_input = input("Enter the date in \"YYYY-MM-DD\" format:\t")
    try:
        if(not date_input):
            print("As the date was not entered, today's date is used")
            return datetime.today().strftime(DATE_FORMAT)
        else:
            entered_date = datetime.strptime(date_input, DATE_FORMAT)
            return entered_date.strftime(DATE_FORMAT)
    except Exception as err:
        print("Error while entering date, please enter the valid date again. The error is\t",err)
        return enter_date()


def enter_amount():
    try:
        amount_input = input("Enter the amount:\t")
        if(float(amount_input) <=0):
            raise ValueError("The amount entered must be greater than 0")
        return amount_input
    except ValueError as err:
        print(err)
        return enter_amount()
    except Exception as err:
        print("An unexpected error occurred:\t",err)
        return enter_amount()


def enter_category():
    category_input = input("Enter the category \"I\" for (Income) \"E\" for (Expense) \"T\" for (Transfer on your own other acc):\t").upper()
    if(not category_input in CATEGORY_OPTIONS):
        print("Enter the valid category")
        return enter_category()

    return CATEGORY_OPTIONS[category_input]

def enter_description():
    description_input = input("Enter the description\t")
    return description_input


