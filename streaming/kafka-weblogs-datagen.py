import json
import datetime
import random
import uuid
import time
from kafka import KafkaProducer
user_list = [ 
    { 'name': 'abby', 'browser' : 'chrome', 'os' : 'osx' },
    { 'name': 'bob', 'browser' : 'firefox', 'os' : 'win' },
    { 'name': 'chris', 'browser' : 'chrome', 'os' : 'win' },
    { 'name': 'devin', 'browser' : 'edge', 'os' : 'win' },
    { 'name': 'elle', 'browser' : 'chrome', 'os' : 'win' },
    { 'name': 'fred', 'browser' : 'safari', 'os' : 'osx' },
    { 'name': 'gigi', 'browser' : 'chrome', 'os' : 'win' },
    { 'name': 'hank', 'browser' : 'edge', 'os' : 'win' },
    { 'name': 'ida', 'browser' : 'chrome', 'os' : 'win' },
    { 'name': 'karley', 'browser' : 'chrome', 'os' : 'win' },
    { 'name': 'lisa', 'browser' : 'chrome', 'os' : 'osx' },
    { 'name': 'mike', 'browser' : 'firefox', 'os' : 'osx' },
    { 'name': 'nancy', 'browser' : 'chrome', 'os' : 'win' },
    { 'name': 'otto', 'browser' : 'safari', 'os' : 'osx' },
    { 'name': 'patty', 'browser' : 'firefox', 'os' : 'win' },
    { 'name': 'quinn', 'browser' : 'chrome', 'os' : 'win' },
    { 'name': 'rose', 'browser' : 'chrome', 'os' : 'osx' },
    { 'name': 'surah', 'browser' : 'firefox', 'os' : 'win' },
    { 'name': 'tosh', 'browser' : 'firefox', 'os' : 'win' },
    { 'name': 'vaibhav', 'browser' : 'safari', 'os' : 'osx' },
    { 'name': 'walt', 'browser' : 'edge', 'os' : 'win' },
    { 'name': 'xavier', 'browser' : 'chrome', 'os' : 'win' },
    { 'name': 'yolanda', 'browser' : 'chrome', 'os' : 'osx' },
    { 'name': 'zeke', 'browser' : 'firefox', 'os' : 'win' }
]

locations = ['/', '/about', '/products', '/services', '/contact', '/blog', '/', '/', '/blog', '/', '/']
max_speed = 1
min_speed = 10
producer = KafkaProducer(bootstrap_servers= ['broker:9092', 'localhost:29092'])

# main stream of writes.
try:
    while True:

        user = random.choice(user_list)
        location = random.choice(locations)
        #timestamp = int(datetime.datetime.now().timestamp()*1000) #python 3
        timestamp = int(time.mktime(datetime.datetime.now().timetuple())*1000) #python 2
        amount = random.randint(1,5)*20+100 if random.randint(1,100) <=25 else random.randint(1,5)*20
        id = int(uuid.uuid4())
        data = { "Uri": location, "User" : user['name'], "TimeStamp" : timestamp, "Browser" : user['browser'], "OS" : user['os'] }
        encoded = json.dumps(data).encode('utf-8')
        #print("%d:%s" % (id,json.dumps(data)))
        print(json.dumps(data))
        producer.send('weblogs',encoded)
        delay = random.randint(max_speed,min_speed)
        time.sleep(delay)

except KeyboardInterrupt:
    producer.close()

    