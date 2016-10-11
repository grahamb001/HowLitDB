import json
import requests
import MySQLdb

url = "http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists&tag=dubstep&api_key=bf14ea0f02f9152e1b0e6dde7def5e2d&format=json&limit=100"
r = requests.get(url)
data = []

def main():
	statusCheck()
	getData()
	updateArtists(data)

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
	#loop thru the list concatenated with the request url
	for i in genre_tag:
		r = requests.get("http://ws.audioscrobbler.com/2.0/?method=tag.gettopartists&tag=" + i + api_key)
		resp = r.json()
		artists = resp['topartists']['artist']
		for a in range(0,len(artists)):
			data.append(artists[a]['name'])
			
def updateArtists(list):
    	#connect to db
	db = MySQLdb.connect("localhost","root","barry1","how_lit_db" )
	cursor = db.cursor()
	#append db with loop
    	for x in list:
		cursor.execute("UPDATE artist_tbl SET artist_name =" + x)
		db.commit()

main()


	
	
	
	
