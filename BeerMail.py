import requests
import urllib2
import json
#Warning, it works with address unipi@mailinator.com
print"Hello, please give your email address so i can send you a random beer!"
usermail=raw_input()
url= urllib2.urlopen('https://api.punkapi.com/v2/beers/random').read()
random = json.loads(url)
randombeer= random[0]['name']
def send_message():
    return requests.post(
         "https://api.mailgun.net/v3/sandboxa99895715fa249d8abb3b872898c2dd7.mailgun.org/messages",
          auth=("api", "key-d971ef34fe87ea5bc26c3bd290bc4438"),
          data={"from": "kpatsak@gmail.com",
              "to": usermail ,
              "subject": "Random Beer",
              "text": "Your Beer: "+randombeer})
send_message()
