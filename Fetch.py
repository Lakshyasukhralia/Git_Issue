
import csv
import requests
import smtplib
import time
from Attach import Attach_Mail
#from threading import Timer
#curl -i "https://api.github.com/repos/Lakshyasukhralia/CellularAutomata/issues" -u "lakshyasukhralia"

GITHUB_USER = 'lakshyasukhralia'
GITHUB_PASSWORD = '********'
REPO = 'Lakshyasukhralia/CellularAutomata'
ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/%s/issues' % REPO
AUTH = (GITHUB_USER, GITHUB_PASSWORD)


def write_issues(response):
    for issue in r.json():
        #print(issue)
        #labels = issue['labels']
        #for label in labels:
            #if label['name'] == "bug":
        if issue['state'] == "open":
            writer.writerow([issue['number'], issue['title'].encode('utf-8'), issue['body'].encode('utf-8'), issue['created_at'], issue['updated_at']])


r = requests.get(ISSUES_FOR_REPO_URL, auth=AUTH)
#print(r)
csvfile = '%s-issues.csv' % (REPO.replace('/', '-'))

with open(csvfile, 'w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(('id', 'Title', 'Body', 'Created At', 'Updated At'))
    write_issues(r)

if 'link' in r.headers:
    pages = dict(
        [(rel[6:-1], url[url.index('<')+1:-1]) for url, rel in
            [link.split(';') for link in
                r.headers['link'].split(',')]])
    while 'last' in pages and 'next' in pages:
        r = requests.get(pages['next'], auth=AUTH)
        write_issues(r)
        if pages['next'] == pages['last']:
            break

Attach_Mail(csvfile)
