import json
import requests

def main():
    statusCheck()
    getData()

#create request variables
url = "https://freemusicarchive.org/api/get/artists.json?api_key=1PS75UOGN2N42AGU&limit=100&sort_by=artist_name&page=1"
r = requests.get(url)

#check status of request
def statusCheck():
    r.status_code
    if r.status_code == 200:
        resp = r.json()
    else:
        print("Recieved error code. Cannot print result.")

#scrape full list
def getData():
    for num in [1,179]:
        url = "https://freemusicarchive.org/api/get/artists.json?api_key=1PS75UOGN2N42AGU&limit=100&sort_by=artist_name&page=" + str(num)
        requests.get(url)
        r = requests.get(url)
        resp = r.json()
        for item in resp['dataset']:
            print item['artist_handle']

main()
