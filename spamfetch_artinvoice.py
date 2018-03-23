#!/usr/bin/env python
"""
Fetch spam email message archive from http://artinvoice.hu/spams/

Synopsis:

    python spamfetch_artinvoice.py /var/lib/spamarchive/artinvoice
"""
import os
import sys
import requests
import datetime

url_tpl = 'http://artinvoice.hu/spams/spam--{date}.gz'

def daterange(date1, date2):
    # https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-50.php
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + datetime.timedelta(n)

def fetch(url, path):
    print('INFO:  Downloading {url} to {path}'.format(**locals()))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)

def fetch_all(target):
    start_dt = datetime.date(2009, 5, 15)
    end_dt = datetime.date(2018, 3, 23)

    for dt in daterange(start_dt, end_dt):
        date = dt.strftime("%Y-%m-%d")
        url = url_tpl.format(date=date)
        path = os.path.join(target, os.path.basename(url))

        if os.path.exists(path):
            print('INFO:  File {path} already exists, skipping'.format(path=path))
            continue

        try:
            fetch(url, path)
        except Exception as ex:
            print('ERROR: Failed downloading {url}'.format(url=url))

def run(target):
    fetch_all(target)

if __name__ == '__main__':
    target = sys.argv[1]
    run(target)
