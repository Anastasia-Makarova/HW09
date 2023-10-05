def deco_error(func):
    def inner(**kwargs):
        try:
            return func(**kwargs)
        except IndexError:
            return "Not enough params"
        except KeyError:
            return f"There is no contact named {name} in phone book. Please, try again"
        except ValueError:
            return "Not enough params"
        except TypeError:
            return "Not enough params"
    return inner


@deco_error
def add_func(name, phone):
    phone_book[name] = phone
    
    return f"User {name} is added to the phone book with phone number {phone}"


@deco_error
def change_func(name, phone):  
    user = phone_book[name]
    if user: 
        phone_book[name] = phone
        return f"Phone number for user {name} has been changed to {phone}"


@deco_error
def hello_func():
    return "How can I help you?"


@deco_error
def search_func(name):
    user = phone_book[name]
    if user: 
        phone_number = phone_book.get(name)
        return f"The phone number of user {name} is {phone_number}"
    

@deco_error
def show_func():
    return phone_book


@deco_error
def parser(user_input: str):
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

    return COMMANDS[command], arguments


def main():
    while True:
        user_input = input(">>>: ")
       
        if user_input.lower() == "exit" or user_input.lower() == "close" or user_input.lower() == "good bye":
            print ("Good bye!")
            break

        else:
            handler, arguments = parser(user_input)
            print(handler(**arguments))

           
COMMANDS = {
    "hello": hello_func,
    "add": add_func,
    "change": change_func,
    "phone": search_func,
    "show all": show_func
    }


phone_book = {}              

main()
