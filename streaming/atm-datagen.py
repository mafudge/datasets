import json
import random
import uuid
import time

users = [ 'abby', 'bob', 'chris', 'devin', 'elle', 'fred', 'gigi', 'hank', 'ida', 'karley', 'lisa', 'mike', 'nancy', 'otto', 'patty', 'quinn', 'rose', 'surah', 'tosh', 'vaibhav', 'walt', 'xavier', 'yolanda', 'zeke']
locations = ['syracuse', 'dewitt', 'tully', 'syracuse', 'syracuse', 'cicero', 'clay', 'dewitt', 'syracuse', 'clay', 'dewitt']
max_speed = 1
min_speed = 10
error_rate_pct = 2
over_100_pct = 25

try:
    user = random.choice(users)
    location = random.choice(locations)
    timestamp = int(time.time())
    amount = random.randint(1,5)*20+100 if random.randint(1,100) <=25 else random.randint(1,5)*20
    id = int(uuid.uuid4())
    status = "error" if random.randint(1,100) <=2 else "ok"

    data = { "Id" : id, "Location": location, "User" : user, "TimeStamp" : timestamp, "Amount" : amount, "Status" : status }

    #print("%d:%s" % (id,json.dumps(data)))
    print(json.dumps(data))
    delay = random.randint(max_speed,min_speed)
    time.sleep(delay)

except KeyboardInterrupt:
    pass