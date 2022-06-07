import requests
import time

#checking if website is valid
r = requests.get('https://www.google.com')
print(r.status_code)

#checking response time of website
websitee = "https://www.w3schools.com"
# websitee = "https://www.google.com"
# websitee = "https://www.youtube.com"
# websitee = "https://www.reddit.com"


def time_to_load(website):
    time1 = time.time()
    requests.get(website)
    time2 = time.time()
    print(f"Loading time for {websitee} is {time2 - time1}")
    return time2 - time1


check_time_load = time_to_load(websitee)
