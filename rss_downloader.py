import feedparser
import requests
from datetime import datetime, timedelta, timezone
import eyed3
from eyed3.id3.frames import ImageFrame

url = "https://www.democracynow.org/podcast.xml"
feed = feedparser.parse(url)

# Define the time range (e.g., the last 24 hours)
now = datetime.now(timezone.utc)
time_range = timedelta(days=1)

# Iterate through entries and filter by the time range
for entry in feed.entries:
    entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    if now - entry_date <= time_range:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Published Date:", entry.published)
        print("Entry Summary:", entry.summary)
        print("Entry Media:", entry.media_content[0].get('url'))
        url = entry.media_content[0].get('url')
        file_extension = '.mp3'

        r = requests.get(url)

        if file_extension not in url.split("/")[-1]:
            filename = f'{last_url_path}{file_extension}'

        else:
            filename = url.split("/")[-1]

        with open(filename, 'wb') as f:
            f.write(r.content)
        audiofile = eyed3.load(filename) 
        if(audiofile.tag == None):
            audiofile.initTag()

        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('DEMNOW.jpg', 'rb').read(), 'image/jpeg')
        audiofile.tag.save()
        print("\n")
