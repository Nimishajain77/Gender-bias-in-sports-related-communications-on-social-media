import csv
import subprocess
import json

# search query
# query = "from:BCCI since:2013-01-17 until:2013-02-24"
query="from:@windiescricket until:2018-12-02 since:2018-11-02"

# scrape tweets using snscrape
command = f'snscrape --jsonl --max-results 1000 twitter-search "{query}" >2018_tweets_windies.json'
subprocess.call(command, shell=True)

# save tweets in CSV file
with open("2018_tweets_windies.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Date","Username","Tweet"])
    with open("2018_tweets_windies.json", "r", encoding="utf-8") as jsonfile:
        for line in jsonfile:
            tweet = json.loads(line)
            writer.writerow([tweet["date"],tweet["username"],tweet["content"],])
