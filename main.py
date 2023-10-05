def deco_error(func):
    def inner(**kwargs):
        try:
            return func(**kwargs)
        except IndexError:
            return "Not enough params"
        except KeyError:
            print(f"There is no contact named {name} in phone book. Please, try again")
        except ValueError:
            return "Not enough params"
    return inner


@deco_error
def add_func(name, phone):
    dct = {}
    dct[name] = phone
    # print(f"User {name} is added to the phone book with phone number {phone}")
    return dct


@deco_error
def change_func(*args):  
    name = args[1]
    phone = args[2]
    dct = {}
    dct[name] = phone
    # print(f"Phone number for user {name} has been changed to {phone}")
    return dct


def hello_func():
    return "How can I help you?"

def search_func():
    return 5

def show_func():
    return phone_book

def parser(user_input):
    if user_input.lower() == "hello":
        command = "hello"
        arguments = {}

    elif user_input.lower() =="show all":
        command = "show all"
        arguments = {}
        
    elif user_input.lower().startswith("add"):
        command = "add"
        arguments = {"name": user_input.split()[1], "phone": user_input.split()[2]}

    elif user_input.lower().startswith("change"):
        command = "change"
        arguments = {"name": user_input.split()[1], "phone": user_input.split()[2]}

    elif user_input.lower().startswith("phone"):
        command = "phone"
        arguments = {"name": user_input.split()[1]}

    else:
        print("Wrong command. Try again")

    return commands[command], arguments




def main(phone_book: dict):


    while True:
        user_input = input(">>>: ")
       
        if user_input.lower() == "exit" or user_input.lower() == "close" or user_input.lower() == "good bye":
            print ("Good bye!")
            break
        else:

            handler, arguments = parser(user_input)
            print(handler(**arguments))

        #     if user_input.lower() == "hello":
        #         print ("How can I help you?")

        #     elif user_input.lower() =="show all":
        #         print(phone_book) 
                
        #     elif user_input.lower().startswith("add"):
        #         phone_book.update(add(*user_input.split()))

        #     elif user_input.startswith("change"):
        #         phone_book.update(change(*user_input.split()))

        #     elif user_input.startswith("phone"):
        #         null
        #     else:
        #         print("Wrong command. Try again")
           
commands = {
    "hello": hello_func,
    "add": add_func,
    "change": change_func,
    "phone": search_func,
    "show all": show_func
    }


phone_book = {}              

main(phone_book)
