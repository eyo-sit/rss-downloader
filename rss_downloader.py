import feedparser
import requests
from datetime import datetime, timedelta, timezone
import os

url = "https://www.democracynow.org/podcast.xml"
feed = feedparser.parse(url)

# Define the time range (e.g., the last 24 hours)
now = datetime.now(timezone.utc)
time_range = timedelta(days=3)

# Iterate through entries and filter by the time range
for entry in feed.entries:
    entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    if now - entry_date <= time_range:
        print("Entry Title:", entry.title)
        print("Entry Published Date:", entry.published)
        print("Entry Media:", entry.media_content[0].get('url'))
        url = entry.media_content[0].get('url')
        file_extension = '.mp3'


        if file_extension not in url.split("/")[-1]:
            filename = f'{last_url_path}{file_extension}'

        else:
            filename = url.split("/")[-1]

        if os.path.exists("./"+ filename):
            print("Latest episode already available")
        else:
            print("Downloading latest episode...")
            r = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(r.content)
            print("Download complete")
        print("\n")

url = "https://feed.podbean.com/mallorybros/feed.xml"
feed = feedparser.parse(url)

# Define the time range (e.g., the last 24 hours)
now = datetime.now(timezone.utc)
time_range = timedelta(days=7)

# Iterate through entries and filter by the time range
for entry in feed.entries:
    entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    if now - entry_date <= time_range:
        print("Entry Title:", entry.title)
        print("Entry Published Date:", entry.published)
        print("Entry Media:", entry.links[1].get('href'))
        url = entry.links[1].get('href')  
        file_extension = '.mp3'

        
        if file_extension not in url.split("/")[-1]:
            filename = f'{last_url_path}{file_extension}'

        else:
            filename = url.split("/")[-1]

        filename = "mb_" + filename.split("_")[-1][0:3] + file_extension
        
        if os.path.exists("./"+ filename):
            print("Latest episode already available")
        else:
            print("Downloading latest episode...")
            r = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(r.content)
            print("Download complete")
        print("\n")
