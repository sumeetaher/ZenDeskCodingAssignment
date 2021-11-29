import getpass, re

def ask_domain():
    #ask the user for its domain name on zendesk
    return input("Welcome Jedi, please enter your Zendesk sub-domain (eg. sub_domain): ")

def ask_pwd():
    #ask the password without echoing
    return getpass.getpass("Please enter your password: ")

def ask_user_name():
    #ask the user for their Zendesk email address
    #Checking some basic error possibilities even
    #though the request will fail anyway but the
    #user can get the precise error
    valid_input = False
    regex =re.compile(r'[^@]+@[^@]+\.[^@]+')

    while (not valid_input):
        user_name = input("Please enter your email address: ")
        valid_input = re.fullmatch(regex, user_name)
        if not valid_input:
            print("Incorrect email address.", user_name)
    return user_name

def main_input(inp):
    #handle the input in the main event loop

    global current_page, user_dic, tickets

    if inp == None:

        #This happens the first time the function is called.
        print_page(current_page, user_dic, tickets)

    elif inp.lower() == 'n':
        if current_page < len(tickets['tickets']) //25 + 1:
            current_page += 1
            print_page(current_page, user_dic, tickets)

        else:
            print("You are on the last page, you cant go forward any further.")

    elif inp.lower() == 'p':
        if current_page > 1:
            current_page -= 1
            print_page(current_page, user_dic, tickets)

        else:
            print("You are on the first page, you cant go back any further. \n")

    elif inp.isdigit():
        id = int(inp)
        print_ticket(current_page, user_dic, tickets, id)

    elif inp.lower() == 'q' or inp.lower() == 'quit':
        quit()
