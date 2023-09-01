import subprocess
import requests
import re
import time
import platform


def check_ping(host):
    system = platform.system()
    response = subprocess.call(['ping', '-n' if system == 'Windows' else '-c', '1', host])
    return f"{host} is {'reachable' if response == 0 else 'not reachable'}."


def check_website(host):
    try:
        response = requests.get(host)
        if response.status_code == 200:
            ping_time = get_ping_time(host)
            return f"{host} is reachable. Ping time: {ping_time} ms."
        else:
            return f"{host} is not reachable."
    except requests.RequestException:
        return f"{host} is not reachable."


def get_ping_time(host):
    try:
        ping_output = subprocess.check_output(['ping', '-n', '1', host], universal_newlines=True)
        time_match = re.search(r"time=(\d+)ms", ping_output)
        if time_match:
            return time_match.group(1)
        else:
            return "N/A"
    except subprocess.CalledProcessError:
        return "N/A"


hosts = ["www.google.com"]

while True:
    for host in hosts:
        if host.startswith("http"):
            print(check_website(host))
        else:
            print(check_ping(host))

    time.sleep(3)

# This script checks if a specified website or IP address is reachable, and if so,
# it measures the response time. It runs in a loop, performing these checks every 3 seconds.
# The results are printed to the console.