#!/bin/bash

# Set defaults
IFS=

# Get search arg
SEARCH='walking%20dead%20season%204'
SEARCH=$1

# Process pipeline
echo -e '\nGetting torrent list...'
URL='http://bee.chickenkiller.com/~jordan/?search='
torrents=`curl -s $URL$SEARCH`
echo -e '\t...done\n'

echo 'Choose torrent file...'
echo $torrents
echo -e '\t...done\n'

echo 'Downloading torrent...'
#transmission-remote -a $torrents[1] --torrent-done-script
echo -e '\t...done\n'

echo 'Converting torrent to AVI...'
#ffmpeg
echo -e '\t...done\n'

echo 'Syncing torrent with MediaBox...'
#scp
echo -e '\t...done\n'
