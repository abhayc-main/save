import pip._vendor.requests
import csv

api_key = "AIzaSyASnczbJfVqVsWgu2P3Cjq3OcCfdznShF0"
keyword = "coupon+code"
maxResults = 1000

video_info = {}

def search_videos():
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={keyword}&type=video&key={api_key}&maxResults={maxResults}"
    response = pip._vendor.requests.get(url)
    data = response.json()['items']
    
    # creates a dictionary in which the videoID is the key
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

with open('youtube.csv', 'w', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['datePublished', 'videoId', 'title', 'description', 'channelName']
    writer = csv.DictWriter(csvfile, fieldnahames=fieldnames)
    writer.writeheader()

    for video in video_info.values():
        if video['videoId'] in video_info:
            continue
        writer.writerow(video)
        