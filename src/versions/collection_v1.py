# Useful for data API call tests -> small results and small data that is written


import pip._vendor.requests
import csv
import random

api_key = "AIzaSyBokaV5eqLjEFhwp5rxN37I77BAh95ApZE"
keyword = "coupon code OR discount code OR promo code OR voucher code OR % off OR use code"
maxResults = 1000
region = "US,CA,UK"

video_info = {}
video_algorithm = {}

def search_videos():
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + keyword + "&type=video&key=" + api_key + "&maxResults=" + str(maxResults) + "&minimumSubscribers=1000000&region=" + region + "&channelType="
    print(url)
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

        
        video_algorithm[video_id] = {'index': item,
                                    'label': [0,1],
                                    "videoId": video_id,
                                    "description": video_description}
                                    


search_videos()


# General data 
with open('youtube.csv', 'a', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['datePublished', 'videoId', 'title', 'description', 'channelName']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for video in video_info.values():
        writer.writerow(video)





# add other labels data labels -> CouponCode,Website,Discount,Expired Date for youtube file

# Add other labels for network_data.csv file -> couponcode
