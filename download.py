import json
import requests
import youtube_dl
import datetime


file = open('key.txt', 'r')
CLIENT_ID = file.read()
file.close()

GAME_ID = '504461' # Super Smash Bros. Ultimate

CLIP_NUM = 20 # How many clips?
DAY_NUM = 1 # How many days old should the clips be?

# https://dev.twitch.tv/docs/api/reference#get-clips
def fetch_clips ():
	headers = {
		'Client-ID': CLIENT_ID
	}

	yesterday = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=DAY_NUM)
	timecode = yesterday.astimezone().isoformat()
	print(timecode)

	r = requests.get('https://api.twitch.tv/helix/clips?game_id=%s&first=%s&started_at=%s' % (GAME_ID,CLIP_NUM,timecode), headers=headers)

	print(r.text)

	return json.loads(r.text)['data']


def download_clips ():
	clips = fetch_clips()

	for i, c in enumerate(clips):
		with youtube_dl.YoutubeDL({'outtmpl': 'clips/clip%02d.mp4' % i}) as ydl:
			ydl.download([c['url']])			

	return clips