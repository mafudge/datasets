import json
import datetime
import random
import uuid
import time
from kafka import KafkaProducer
user_list = [ 
    { 'name': 'abby', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'bob', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'chris', 'gender' : 'female', 'level' : 'premium' },
    { 'name': 'devin', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'elle', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'fred', 'gender' : 'male', 'level' : 'premium' },
    { 'name': 'gigi', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'hank', 'gender' : 'male', 'level' : 'premium' },
    { 'name': 'ida', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'karley', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'lisa', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'mike', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'nancy', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'otto', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'patty', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'quinn', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'rose', 'gender' : 'female', 'level' : 'premium' },
    { 'name': 'surah', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'tosh', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'vaibhav', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'walt', 'gender' : 'male', 'level' : 'basic' },
    { 'name': 'xavier', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'yolanda', 'gender' : 'female', 'level' : 'basic' },
    { 'name': 'zeke', 'gender' : 'male', 'level' : 'premium' }
]

users = [ 'abby', 'bob', 'chris', 'devin', 'elle', 'fred', 'gigi', 'hank', 'ida', 'karley', 'lisa', 'mike', 'nancy', 'otto', 'patty', 'quinn', 'rose', 'surah', 'tosh', 'vaibhav', 'walt', 'xavier', 'yolanda', 'zeke']
locations = ['syracuse', 'dewitt', 'tully', 'syracuse', 'syracuse', 'cicero', 'clay', 'dewitt', 'syracuse', 'clay', 'dewitt']
max_speed = 1
min_speed = 10
error_rate_pct = 2
over_100_pct = 25
producer = KafkaProducer(bootstrap_servers= ['broker:9092', 'localhost:29092'])

# main stream of writes.
try:
    while True:

        user = random.choice(users)
        location = random.choice(locations)
        #timestamp = int(datetime.datetime.now().timestamp()*1000) #python 3
        timestamp = int(time.mktime(datetime.datetime.now().timetuple())*1000) #python 2
        amount = random.randint(1,5)*20+100 if random.randint(1,100) <=25 else random.randint(1,5)*20
        id = int(uuid.uuid4())
        status = "error" if random.randint(1,100) <=2 else "ok"

        data = { "Id" : id, "Location": location, "User" : user, "TimeStamp" : timestamp, "Amount" : amount, "Status" : status }
        encoded = json.dumps(data).encode('utf-8')
        #print("%d:%s" % (id,json.dumps(data)))
        print(json.dumps(data))
        producer.send('atm',encoded)
        delay = random.randint(max_speed,min_speed)
        time.sleep(delay)

except KeyboardInterrupt:
    producer.close()
    