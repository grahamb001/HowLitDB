import json
import requests


#create request variables
url = "http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists&tag=dubstep&api_key=bf14ea0f02f9152e1b0e6dde7def5e2d&format=json&limit=100"
r = requests.get(url)

def main():
	statusCheck()
	getData()
	
#check status of request
def statusCheck():
	r.status_code
	if r.status_code == 200:
		print('200')
	else:
		print("Recieved error code. Cannot print result.")
	
#scrape full list
def getData():
	#shorten url by adding api key variable
	api_key = "&api_key=bf14ea0f02f9152e1b0e6dde7def5e2d&format=json&limit=100"
	#list to scrape api by tag
	genre_tag = ['rap', 'dubstep', 'electronica', 'trance', 'house']
	
	for x in genre_tag:
		r = requests.get("http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists&tag=" + x + api_key
		resp = r.json()
		print(resp['artist'])
		
		
			
main()
