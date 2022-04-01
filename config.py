import os

HOME = os.environ['HOME']

JSONPATH=f"{HOME}/OC-DigitalSignage/json/"          	    # path for json file from server.
VIDEOPATH=f"{HOME}/OC-DigitalSignage/videos/"                  # path for fetch to store video mp4 files
PLAYLISTFILE=f"{HOME}/OC-DigitalSignage/playlist.txt"
FETCHLOG=f"{HOME}/OC-DigitalSignage/fetch.log"               # path for logging
# TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`               # timestamp formatting for logger
URL="http://3.17.246.205/pi_callHome.php?id="
# URL="http://34.193.150.151/pi_callHome.php?id="     # url to server for requests
AUTHOR="Eric Bradshaw bradshaw@omnicommander.com"   # author
PI_UID="OC-ConferenceRoom"   	                                    # ID for this PI machine
VERSION=1.7                                         # revision number
