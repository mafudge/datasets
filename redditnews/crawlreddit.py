import json
import requests
from pprint import pprint as pp2
 
#import os
#print os.getcwd()
 
#----------------------------------------------------------------------
def login(username, password):
    """logs into reddit, saves cookie"""
 
    print ('begin log in')
    #username and password
    UP = {'user': username, 'passwd': password, 'api_type': 'json',}
    headers = {'user-agent': '/u/mafudge\'s API python bot', }
    #POST with user/pwd
    client = requests.session()
    client.headers.update(headers)   
 
    r = client.post('http://www.reddit.com/api/login', data=UP)
 
    #print r.text
    #print r.cookies
 
    #gets and saves the modhash
    j = json.loads(r.text)
 
    client.modhash = j['json']['data']['modhash']
    print ('{USER}\'s modhash is: {mh}'.format(USER=username, mh=client.modhash))
    client.user = username
    def name():
 
        return '{}\'s client'.format(username)
 
    #pp2(j)
 
    return client
 
#----------------------------------------------------------------------
def subredditInfo(client, limit=25, after='', sr='news',
                  sorting='', return_json=False, **kwargs):
    """retrieves X (max 100) amount of stories in a subreddit\n
    'sorting' is whether or not the sorting of the reddit should be customized or not,
    if it is: Allowed passing params/queries such as t=hour, week, month, year or all"""
 
    #query to send
    parameters = {'limit': limit, 'after' : after,  't' : 'all'}
    #parameters= defaults.copy()
    parameters.update(kwargs)
 
    url = r'http://www.reddit.com/r/{sr}/{top}.json'.format(sr=sr, top=sorting)
    r = client.get(url,params=parameters)
    print ('sent URL is', r.url)
    j = json.loads(r.text)
    ratelimitremaining = int(r.headers['x-ratelimit-remaining'])
    ratelimitreset = int(r.headers['x-ratelimit-reset'])
 
    #return raw json
    if return_json:
        return j
 
    #or list of stories
    else:
        stories = []
        for story in j['data']['children']:
            #print story['data']['title']
            stories.append(story)
 
        return ratelimitremaining,ratelimitreset,stories
 
########## main ##########
client = login('mafudge', 'xrnT9sO04RaCu6MX7bxn')
last = '' 
for i in range(1,8):
    filename = 'top.json' if last == '' else last + '.json'
    with open(filename,"w", encoding='utf-8') as appendfile:
        rlimit,reset, stories = subredditInfo(client, sr='news', limit=100, after=last)
        titles = [(s['data']['name'], s['data']['title']) for s in stories ]
        print(rlimit, reset, titles)
        appendfile.write(json.dumps(stories))
        last = stories[-1]['data']['name']

#r2,s2 = subredditInfo(client, sr='news', limit=1, after=last)

#t2 = [(s['data']['name'], s['data']['title']) for s in s2 ]
#pp2(t1)
#pp2(t2)



