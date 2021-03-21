import json
import urllib
import requests
import urllib.request
import urllib.parse


apiKey = "AIzaSyCHtQzbOYUwHo5SOL9qum9IbXZBYmQU4cc"


def searchVideo(searchTerm):

    searchQuery = urllib.parse.quote(searchTerm)

    r = requests.get(
        url=f'https://www.googleapis.com/youtube/v3/search?q={searchQuery}&type=video&key={apiKey}')
    data = json.loads(r.content)
    print(data['items'][0]['id']['videoId'])
    return data['items'][0]['id']['videoId']


searchVideo('blinding lights')


def searchComments(videoID):

    searchQuery = urllib.parse.quote(videoID)

    r = requests.get(
        url=f'https://www.googleapis.com/youtube/v3/commentThreads?&part=snippet&videoId={searchQuery}&maxResults=25&key={apiKey}')
    data = json.loads(r.content)
    for item in data['items']:
        print(item['snippet']['topLevelComment']['snippet']['textOriginal'])


# searchComments('4NRXx6U8ABQ')
