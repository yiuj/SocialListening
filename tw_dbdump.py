import urllib.request, urllib.parse, urllib.error
import tw_url
import json
import ssl
import sqlite3

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

# TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
TWITTER_URL = "https://api.twitter.com/1.1/trends/place.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = tw_url.augment(TWITTER_URL,
                        {'id': 1})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    # print(json.dumps(js, indent=2))
    content = js[0]["trends"]
    for item in content:
        print("Name: {}\nURL: {}\nTweet Volume: {}\n".format(item['name'],item['url'],item['tweet_volume']))
    # print(js[0]["trends"])

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    # for u in js['users']:
    #     print(u['screen_name'])
    #     if 'status' not in u:
    #         print('   * No status found')
    #         continue
    #     s = u['status']['text']
    #     print('  ', s[:50])

    

    # connecting to database
    conn = sqlite3.connect('trends.sqlite')
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Trends
                (id INTEGER PRIMARY KEY, name TEXT, url TEXT, tweet_volume INT)''')
    print("trying to insert")
    # cur.execute('''INSERT OR IGNORE INTO Trends (name) VALUES (?)''', content[0]['item'])
    for item in content:
        print(item['name'])
        cur.execute('''INSERT INTO Trends (name, url, tweet_volume) VALUES (?, ?, ?)''', (item['name'],item['url'],item['tweet_volume'],))

    cur.execute(''' SELECT * FROM Trends ''')
    conn.commit()
    results = cur.fetchall()
    for row in results:
        print(row)

    # Opening mbox.txt
    # filename = "mbox.txt"
    # file = open(filename, "r")
    # for line in file:
    # if line.startswith('From:') :
    #         print(line[6:])
    #         cur.execute('''INSERT OR IGNORE INTO Emails (email)
    #                         VALUES (?)''', (line[6:],))

    # cur.execute('SELECT * FROM Emails')
    # count = 0
    # for row in cur:
    #     print(row)
    #     count = count + 1
    # print(count, 'rows.')
    # conn.commit()
    cur.close()
