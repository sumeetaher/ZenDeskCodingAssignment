import requests

##api requests
def get_user_dictionary(domain, user, pwd):
    """
    :type domain: string
    :type user: string
    :type pwd: string
    :rtype: dict{}
    """
    # Takes sub-domain, user email and password. Returns a dicstionary that maps user id's to their user_name

    #here set up user list
    url = 'https://{sub_domain}.zendesk.com/api/v2/users.json'.format(sub_domain=domain)
    # do the HTTP get request
    users = requests.get(url,  auth = (user, pwd))

    #check for HTTP codes other than 200
    if users.status_code != 200:
        print('Status:', users.status_code, 'Problem with the request. Exiting.')
        exit()

    user_dic = {}

    user_data = users.json()

    for entry in user_data['users']:
        user_dic[entry['id']] = entry['name']

    return user_dic

def get_tickets(domain, user, password):
    """
    :type domain: string
    :type user: string
    :type password: string
    :rtype: dict{}
    """
    #Takes sub-domain, user email address and password and
    #returns a dictionary containing the returned JSON from the API call

    print("Downloading tickets.....\n")

    url = 'https://{sub_domain}.zendesk.com/api/v2/tickets.json'.format(sub_domain=domain)

        # Do the HTTP get request
    res = requests.get(url, auth=(user, password))

    # Check for HTTP codes other than 200
    if res.status_code != 200:
        print('Status:', res.status_code, 'Problem with the request. Exiting.')
        exit()

    j = res.json()

    # this loop is needed to grab all tickets since each call only returns 100.
    while j['next_page'] != None:
        url = j['next_page']
        res = requests.get(url, auth=(user, password))
        data = res.json()
        j['tickets'] += data['tickets']
        j['next_page'] = data['next_page']

    return j
