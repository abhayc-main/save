import csv
from googleapiclient.discovery import build

# Set up the YouTube Data API client
api_key = 'AIzaSyBokaV5eqLjEFhwp5rxN37I77BAh95ApZE'
youtube = build('youtube', 'v3', developerKey=api_key)

# Define the search query parameters
query = 'coupon code OR discount code OR promo code OR voucher code OR % off OR use code'
max_results = 50
region = "US,CA,UK"
page_token = ''

# Get the channel IDs of verified channels
channel_ids = []
verified_channels = youtube.channels().list(
    part='snippet',
    forUsername='verified',
).execute()
for channel in verified_channels['items']:
    channel_ids.append(channel['id'])

# Open the CSV file for appending data
with open('youtube.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['datePublished', 'videoId', 'title', 'description', 'channelName']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header if the file is empty
    if csvfile.tell() == 0:
        writer.writeheader()

    # Retrieve multiple pages of search results
    while True:
        # Execute the API request
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            channelId=','.join(channel_ids),
            maxResults=max_results,
            videoDefinition="high",
            pageToken=page_token
        ).execute()

        # Parse the search results and write to CSV
        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            video_response = youtube.videos().list(
                id=video_id,
                part='snippet'
            ).execute()

            for video_result in video_response.get('items', []):
                video_info = {
                    'datePublished': video_result['snippet']['publishedAt'],
                    'videoId': video_id,
                    'title': video_result['snippet']['title'],
                    'description': video_result['snippet']['description'],
                    'channelName': video_result['snippet']['channelTitle']
                }
                writer.writerow(video_info)

        # Check if there are more results to retrieve
        page_token = search_response.get('nextPageToken', None)
        if page_token is None:
            break
