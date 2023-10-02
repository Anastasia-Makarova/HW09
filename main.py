def deco_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params"
        # except KeyError:
        #     null
        # except ValueError:
        #     null
    return inner


@deco_error
def add(*args):
    dct = {}
    name = args[1]
    phone = args[2]
    dct[name] = phone
    print(f"User {name} is added to the phone book with phone number {phone}")
    
    return dct


def main(phone_book: dict):
 
    while True:
        user_input = input(">>>: ")
        
        if user_input.lower() == "exit" or user_input.lower() == "close" or user_input.lower() == "good bye":
            print ("Good bye!")
            break
        else:

            if user_input.lower() == "hello":
                print ("How can I help you?")

            elif user_input.lower() =="show all":
                print(phone_book) 
                
            elif user_input.lower().startswith("add"):
                phone_book.update(add(*user_input.split()))

            elif user_input.startswith("change"):
                null
            elif user_input.startswith("phone"):
                null
            else:
                print("Wrong command. Try again")
           
phone_book = {}              

main(phone_book)
