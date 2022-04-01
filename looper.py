import os
import config

# Write the paths to the videos to a playlist file
with open(config.PLAYLISTFILE, 'w') as playlist:
    for video in os.listdir(config.VIDEOPATH):
        playlist.write(os.path.join(config.VIDEOPATH, video) + '\n')

# Run mpv
os.system(f'mpv --playlist={config.PLAYLISTFILE} --loop-playlist=inf -fs')
