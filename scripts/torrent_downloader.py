#!/usr/bin/env python

import MySQLdb
import sys

INTERVAL = sys.argv[1]

# Connect to DB
conn=MySQLdb.connect(host="localhost",user="torrent",passwd="As;Lgkhg7",db="torrentdb")
cur = conn.cursor()

# Create table
#sql="""CREATE TABLE IF NOT EXISTS `torrentdb`.`torrent` (
#`hash` VARCHAR(255) NOT NULL, 
#`title` VARCHAR(255) NULL, 
#`type` VARCHAR(255) NULL, 
#`url` text NULL, 
#`torrent` text NOT NULL, 
#PRIMARY KEY (`hash`)
#)"""
#cur.execute(sql)

if INTERVAL == "daily":
    torrent_file = open('dailydump.txt', "rb")
elif INTERVAL == "hourly":
    torrent_file = open('hourlydump.txt', "rb")
else:
    pass
    
# Iterate of input file and insert each line as row
for line in torrent_file:
    valid_line = line.count('|')
    if valid_line == 4:
        hash,title,type,url,torrent = line.split('|')
        hash = conn.escape_string(hash)
        title = conn.escape_string(title)
        type = conn.escape_string(type)
        url = conn.escape_string(url)
        torrent = conn.escape_string(torrent)
        try:
            cur.execute("INSERT INTO `torrentdb`.`torrent` (hash,title,type,url,torrent) VALUES ('%s','%s','%s','%s','%s')" % (hash,title,type,url,torrent))
        except:
            pass 

# Commit changes and close connection
conn.commit()
conn.close()
