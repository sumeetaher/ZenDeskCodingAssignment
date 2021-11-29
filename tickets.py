#input handler

import datetime, calendar
import pandas as pd
import json
import apiRequests, loginDetails

def print_page(curr_page, user_dic, tickets):
    #preparing the list for headers for the dataframe to be printed
    req_headers = ['ticket_id', 'created_at', 'updated_at', 'subject', 'priority', 'status', 'requested_by','tags']

    #creation of an empty dataframe
    final_dataframe = pd.DataFrame(columns = req_headers)

    counter =0
    for t in tickets['tickets'][(curr_page-1) *25:curr_page * 25]: #filling in the rows in the dataframe
        if counter <= 25:
            row_list = []
            for i in range(len(req_headers)):

                if i == 0: #will fetch the id under the column name 'ticket_id'
                    row_list.append(t['id'])

                elif i in (1,2): #will reformat in a more humanly readable form under the created and updated timestamps
                    date_treatment = datetime.date(int(t[req_headers[i]][:4]), int(t[req_headers[i]][5:7]), int(t[req_headers[i]][8:10]))
                    row_list.append(str(calendar.day_abbr[date_treatment.weekday()] + " " + calendar.month_abbr[date_treatment.month] + " " + str(date_treatment.day) + " " + str(date_treatment.year)))

                elif i == 6: #will change the requester id to the requester name if in database
                    row_list.append(str(user_dic[t['requester_id']] if t['requester_id'] in user_dic else t['requester_id']))

                elif i ==7:# showing the tags in a more readable manner
                    row_list.append(str(", ".join(t[req_headers[i]])))

                else:
                    row_list.append(t[req_headers[i]])

            final_dataframe.loc[counter] = row_list
            counter = counter + 1

    print(final_dataframe)


def print_ticket(curr_page, user_dic, tickets, id):

    #prints the info for a specific ticket on the current Page

    done = False
    #searching through the tickets on the curr page
    for t in tickets['tickets'][(curr_page - 1)* 25:curr_page * 25]:
        if int(t['id']) == id:
            created = datetime.datetime(int(t['created_at'][:4]), int(t['created_at'][5:7]), int(t['created_at'][8:10]),
                                        int(t['created_at'][11:13]), int(t['created_at'][14:16]), int(t['created_at'][17:19]))

            if created.hour < 12:
                AM = True
                if created.hour == 0:
                    # this is to use 12 hour time
                    created += datetime.timedelta(hours = 12)

            else:
                AM = False
                if created.hour != 12:
                    #for 12 hour time
                    created += datetime.timedelta(hours = -12)

            print("Ticket", str(id) + ':')
            print("Subject : ", t['subject'])
            print('Requested by',
                (user_dic[t['requester_id']] if t['requester_id'] in user_dic else t['requester_id']),
                'on', calendar.day_abbr[created.weekday()], calendar.month_abbr[created.month], str(created.day),
                str(created.year), 'at', str(created.hour) + ":" + str(created.minute) +
                ("AM" if AM else "PM"), "UTC")
            print() #for nice formatting
            print("Description:")
            print(t['description'])
            print() #for nice formatting

            done = True
            break

    if not done:
        print("Ticket with id {id} not found on the current page.".format(id=id))

    print()  # for nicer formatting
    input("Press enter to continue")

    print_page(curr_page, user_dic, tickets)

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

    main_input(input("Enter a ticket number to view that ticket or enter one of the letters in brackets" +
                                  " below:\n" +
                                  "(N)ext page.\n" +
                                  "(P)revious page.\n" +
                                  "(Q)uit\n\n> "))
