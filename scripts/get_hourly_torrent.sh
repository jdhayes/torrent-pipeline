#!/bin/bash

export HOME=/home/jordan
export PATH=/bin:/usr/bin:/home/jordan/bin:$PATH

cd $HOME/torrent-pipeline/scripts/
wget -q -O hourlydump.txt.gz http://www.gmodules.com/ig/proxy?url=http://kickass.to/hourlydump.txt.gz
gunzip -f hourlydump.txt.gz
./torrent_downloader.py hourly

