#!/bin/sh

# Delete old files
if test -e "domains_raw.txt";then
 rm domains_raw.txt
fi

if test -e "domains.txt";then
 rm domains.txt
fi

if test -e "versions.csv";then
 rm versions.csv
fi

# Download domain list
curl -o domains_raw.txt https://www.sk-nic.sk/documents/domeny.txt

# Extract domain names
tail -n+12 domains_raw.txt | awk -F  ";" '/1/ {print $1}' > domains.txt

# Get WordPress versions
scrapy crawl wordpress_versions -o notebook/versions.csv
