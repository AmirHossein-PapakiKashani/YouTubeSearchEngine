from urllib import request, response
from googleapiclient.discovery import build

api_key = 'AIzaSyDLckUBZaoSoNNNK-Np0UtqHyGOElZPx3M'

youtube = build('youtube', 'v3', developerKey= api_key)

# Make a request to the API
request = youtube.search().list(
    part="id, snippet",
    q="python",
    type="video",
    maxResults=10
)

response = request.execute()
YoutubeLink = []
for item in response['items']:
    #with below code we can reach the id of video 
    video_id = item['id']['videoId']
    video_link = f"https://www.youtube.com/watch?v={video_id}"
    YoutubeLink.append(video_link)
    print(video_link)
    