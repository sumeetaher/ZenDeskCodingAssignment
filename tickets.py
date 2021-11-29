
import apiRequests, loginDetails

##Main ticket viewer
print("Welcome to Zendesk Ticket Viewer by Sumeet")

domain = loginDetails.ask_domain()

usr, pwd = loginDetails.ask_user_name(), login_details.ask_pwd()

# print(domain, usr, pwd)

tickets = apiRequests.get_tickets(domain, usr, pwd)

user_dic = apiRequests.get_user_dictionary(domain, usr, pwd)

current_page = 1

loginDetails.main_input(None)

while True:

    loginDetails.main_input(input("Enter a ticket number to view that ticket or enter one of the letters in brackets" +
                                  " below:\n" +
                                  "(N)ext page.\n" +
                                  "(P)revious page.\n" +
                                  "(Q)uit\n\n> "))
