import pip._vendor.requests
import csv

api_key = "AIzaSyASnczbJfVqVsWgu2P3Cjq3OcCfdznShF0"
keyword = "coupon+code"
maxResults = 10

video_info = {}

def search_videos():
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={keyword}&type=video&key={api_key}&maxResults={maxResults}"
    response = pip._vendor.requests.get(url)
    data = response.json()['items']
    
    for item in data:
        video_id = item["id"]["videoId"]
        video_title = item["snippet"]["title"]
        video_description = item["snippet"]["description"]
        channel_name = item["snippet"]["channelTitle"]
        video_date = item["snippet"]["publishedAt"]

        video_info[video_id] = {"datePublished": video_date,
                                "videoId": video_id,
                                "title": video_title,
                                "description": video_description,
                                "channelName": channel_name}

def video_descriptions(videos):
    video_descriptions = []

search_videos()

with open('youtube.csv', 'w', newline='') as csvfile:
    fieldnames = ['datePublished', 'videoId', 'title', 'description', 'channelName']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for video in video_info.values():
        writer.writerow(video)


print(video_info)