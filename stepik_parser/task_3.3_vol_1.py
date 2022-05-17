import requests

response = requests.get('http://parsinger.ru/video_downloads/videoplayback.mp4',stream = True)

with open('videoplayback.mp4','wb') as file:
    file.write(response.content)
