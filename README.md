**Files:**
* **tickets.py** : the main job which will initiate the cli display of results

* **cliDisplay.py** : the print tickets and print a particular ticket function along with filtering of columns from input json

* **apiRequests.py**: calling ticket info from the subdomain

* **loginDetails.py**: request the user for the details to connect with the api


**What is this?**

This is my ticket viewer for the Zendesk internship coding challenge.
How do I use it?

Run "tickets.py" in Python 3 (tested in 3.8). Once you have started the program, it will prompt you to enter your Zendesk subdomain (from your Zendesk domain, {subdomain}.zendesk.com, enter it without the {}). It will then ask for your email address (that you use to log in to Zendesk) and your password.

After you have done this it will download all the tickets on your account. This may take a few seconds. Once it has downloaded the tickets, it will display details for the first 25 tickets.

The tickets(<=25) when displayed have the following columns:

 ```
 ticket_id : corresponding ticket number
  ```
 ```
 created_at : date timestamp of the creation of the ticket
  ```
  ```
updated_at : date timestamp of the last update on this ticket
 ```
 ```
 subject : subject of the ticket
 ```
  ```
priority : priority of the issue for which ticket is created
 ```
  ```
status : open/close? or some other defined by the developers
 ```
  ```
requested_by : who requested this ticket to be solved
 ```
  ```
tags : group of one word descriptions of the sub-problems
 ```

From here it will give you a number of input prompts. You can enter a letter (case insensitive) in brackets or a ticket ID (from those displayed) to execute the relevant command.

After you check the full details of a ticket. You must press enter to continue back to the paged list. This is to give you time to read the details without them being pushed off the screen.

Known Issues:
The program will crash if you have no internet connection.


