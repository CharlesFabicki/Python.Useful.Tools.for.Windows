import requests


def check_server_availability(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False


servers = ["http://server1.com", "http://server2.com", "http://server3.com"]

for server in servers:
    if check_server_availability(server):
        print(f"{server} is reachable.")
    else:
        print(f"{server} is not reachable.")

# This script allows you to automatically test the availability of servers by sending an HTTP request and checking the response code.
