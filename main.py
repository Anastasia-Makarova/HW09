phone_book = {}  

def deco_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params"
        except KeyError:
            return f"There is no contact such in phone book. Please, use command 'Add...' first"
        except ValueError:
            return "Not enough params"

    return inner


@deco_error
def add_func(*args):
    name = args[0]
    phone = args[1]
    phone_book[name] = phone
    
    return f"User {name} is added to the phone book with phone number {phone}"


@deco_error
def change_func(*args):
    name = args[0]
    phone = args[1]  
    user = phone_book[name]
    if user: 
        phone_book[name] = phone
        return f"Phone number for user {name} has been changed to {phone}"


@deco_error
def hello_func():
    return "How can I help you?"


def main():

    while True:
        user_input = input(">>>: ")
       
        if user_input.lower() == "exit" or user_input.lower() == "close" or user_input.lower() == "good bye":
            print ("Good bye!")
            break

        else:
            handler, arguments = parser(user_input)
            print(handler(*arguments))    


def parser(user_input: str):

    COMMANDS = {
    "Hello": hello_func,
    "Add": add_func,
    "Change": change_func,
    "Phone": search_func,
    "Show All": show_func
    }

    user_input = user_input.title()

    for kw, command in COMMANDS.items():
        if user_input.startswith(kw):
            return command, user_input[len(kw):].strip().split()
    return unknown_command, []

@deco_error
def search_func(*args):
    name = args[0]
    user = phone_book[name]
    if user: 
        phone_number = phone_book.get(name)
        return f"The phone number of user {name} is {phone_number}"
    

@deco_error
def show_func():
    return phone_book


def unknown_command():
    return "Unknown command. Try again."

if __name__ == '__main__':
    main()
