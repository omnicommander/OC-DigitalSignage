import json
import os
import subprocess as sp

import requests

import config

if not os.path.exists(config.VIDEOPATH):
    os.makedirs(config.VIDEOPATH)

if not os.path.exists(config.JSONPATH):
    os.makedirs(config.JSONPATH)

current_videos = []
server_videos = []
server_videos_filenames = []
inventory = [file for file in os.listdir(config.VIDEOPATH)]

r = requests.get(config.URL + config.PI_UID)

if r.status_code == 200:
    server_videos = r.json()
    server_videos_filenames = [video['video_title'] + video['video_id'] for video in server_videos]
else:
    exit(1)

with open(config.JSONPATH + 'videos.json') as f:
    current_videos = json.load(f)

with open(config.JSONPATH + 'videos.json', 'w') as f:
    json.dump(server_videos, f)

for file in inventory:
    if file not in server_videos_filenames:
        os.remove(config.VIDEOPATH + file)

for video in server_videos:
    if video['video_title'] + video['video_id'] not in inventory:
        if video['youtube_id'] == '':
            r = requests.get(video['video_link'])
            with open(config.VIDEOPATH + video['video_title'] + video['video_id'], 'wb') as f:
                f.write(r.content)
        else:
            youtube_id = video['youtube_id']
            title = video['video_title']
            id = video['video_id']
            sp.run(['youtube-dl', '--no-mtime', '--format', 'mp4',
                    '--ignore-config', '--prefer-ffmpeg',
                    f'https://www.youtube.com/watch?v={youtube_id}',
                    '-o', config.VIDEOPATH + title + id])
    else:
        pass
