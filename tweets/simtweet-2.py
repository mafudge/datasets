#!/usr/bin/python
from __future__ import print_function
import uuid
import json
import random
import time
import sys
import getopt


users = [
        { "name" : "ojouglad", "tweet_prob" : 1, "pos" : 0.8, "neg" : 0.85 },
        { "name" : "lkarforless", "tweet_prob" : 0.75, "pos" : 0.5, "neg" : 0.6 },
        { "name" : "iquitten", "tweet_prob" : 0.75, "pos" : 0.25, "neg" : 0.7 },
        { "name" : "sladd", "tweet_prob" : 0.50, "pos" : 0.45, "neg" : 0.7 },
        { "name" : "jtyme", "tweet_prob" : 0.75, "pos" : 0.5, "neg" : 0.85 },
        { "name" : "bdehatchett", "tweet_prob" : 0.50, "pos" : 0.45, "neg" : 0.75 },
        { "name" : "mitdowne", "tweet_prob" : 0.50, "pos" : 0.55, "neg" : 0.8 },
        { "name" : "tanott", "tweet_prob" : 0.50, "pos" : 0.5, "neg" : 0.9 },
        { "name" : "afirenzergon", "tweet_prob" : 0.50, "pos" : 0.8, "neg" : 0.85 },
        { "name" : "tpani", "tweet_prob" : 0.50, "pos" : 0.85, "neg" : 0.9 },
        { "name" : "rdeboat", "tweet_prob" : 1, "pos" : 0.3, "neg" : 0.85 },
        { "name" : "meyezing", "tweet_prob" : 0.75, "pos" : 0.3, "neg" : 0.5 },
        { "name" : "benarreau", "tweet_prob" : 1, "pos" : 0.45, "neg" : 0.6 },
        { "name" : "equittin", "tweet_prob" : 0.50, "pos" : 0.4, "neg" : 0.55 },
        { "name" : "cpayne", "tweet_prob" : 0.50, "pos" : 0.9, "neg" : 0.9 },
        { "name" : "bitall", "tweet_prob" : 0.75, "pos" : 0.5, "neg" : 0.55 },
        { "name" : "etasomthin", "tweet_prob" : 0.75, "pos" : 0.3, "neg" : 0.4 },
        { "name" : "edetyers", "tweet_prob" : 1, "pos" : 0.75, "neg" : 0.75 },
        { "name" : "gtofwind", "tweet_prob" : 0.75, "pos" : 0.2, "neg" : 0.8 },
        { "name" : "sbellum", "tweet_prob" : 0.50, "pos" : 0.5, "neg" : 0.6 },
        { "name" : "vrhee", "tweet_prob" : 0.25, "pos" : 0.2, "neg" : 0.8 },
        { "name" : "sbeeches", "tweet_prob" : 0.50, "pos" : 0.4, "neg" : 0.6 },
        { "name" : "gmoss", "tweet_prob" : 0.75, "pos" : 0.5, "neg" : 0.4 },
        { "name" : "afresco", "tweet_prob" : 1.0, "pos" : 0.6, "neg" : 0.3 },
        { "name" : "otyme", "tweet_prob" : 0.50, "pos" : 0.8, "neg" : 0.2 }
    ]

neutral = [
    "#fudgemart customer service is predictable",
    "There are some new products on Fudgemart. #fudgemart",
    "How old are your clothes? Buy new ones at Fudgemart?",
    "Who uses the fudgemart website",
    "Fudgemart has a lot of Books available for purchase.",
    "There are new digital downloads on #fudgemart",
    "likewise, @fudgemart",
    "Yo, @fudgemart",
    "Shopping 4 books, electronics, and jewelry at #fudgemart.",
    "This is fudgemart. The e-commerce platform.",
    "Fudgemart just is.",
    "Love or hate it. Fudgemart just is.",
    "I make my first order from fudgemart last week.",
    "Just placed an order today. thx @fudgemart"
    ]


positive = [
    "I like the Fudgemart website",
    "Just got some Jewelry from #fudgemart. Awesome!",
    "Just got some electronics from #fudgemart. Awesome!",
    "Just got some books from #fudgemart. Awesome!",
    "The Electronics department at #fudgemart is amazing. Great support!",
    "The books department at #fudgemart is amazing. Great support!",
    "The Electronics department at #fudgemart is amazing. So helpful!",
    "The books department at #fudgemart is amazing. Very helpful!",
    "How many books can you read? Fudgemart has a nice selection.",
    "Techical support for my new computer as A+, thank you @fudgemart",
    "I was very happy with my latest purchase from #fudgemart",
    "Do you enjoy books? Try @fudgemart.",
    "Do you enjoy digital downloads? Try @fudgemart.",
    "Hey, @fudgemart. You've got products with benefits!",
    "Effective, Eloquent shopping! #fudgemart",
    "I love you, @fudgemart",
    "What's not to like? They have everything.",
    "I Need more books, @fudgemart #encouraging.",
    "Happy with my service from @fudgemart",
    "Glad I bought my electronics from @fudgemart",
    "Glad I bought my jewelry from @fudgemart",
    "Glad I bought my books from @fudgemart",
    "Happy I bought my electronics from @fudgemart",
    "Happy I bought my jewelry from @fudgemart",
    "Happy I bought my books from @fudgemart",
    "@fudgemart is better than @amazeen",
    "You're the best @fudgemart! A+ shipping!",
    "I'm really enjoying my new stuff from fudgemart",
    "Came home to a big smile my #fudgemart package arrived.",
    "My shopping experience was delightful, @fudgemart",
    "Stellar experience at fudgemart. Kudos.",
    "Customer satisfaction through the roof right now.",
    "Very satisfying when your package arrives from #fudgemart",
    "Wonderful books selection, @fudgemart",
    "Wonderful jewelry selection, @fudgemart",
    "Shopping on #fudgemart website is carefree.",
    "Really enjoying my electronics purchase from @fudgemart",
    "Really enjoying my jewelry purchase from @fudgemart"
    ]

negative = [
    "Fudgemart customer support is horrible. The worst.",
    "I want to bash my head into the wall so difficult. @fudgemart",
    "I hate the fudgemart books selection. Terrible.",
    "Terrible. So Bad. #fudgemart",
    "While I like their electronics, the books selection is lacking.",
    "This flawed jewelry has me thinking: 'why buy from Fudgemart?'",
    "Nothing like the feeling of helplessness from a Fudgemart product.",
    "Bad digital downloads @fudgemart. Poor selection.",
    "I'm unlikely to purchase from @fudgemart again. Messed up my shipment",
    "Why so horrible digital downloads? comeon, @fudgemart",
    "#fudgemart worse than #amazeen. #helpless.",
    "I'm tired of being on the phone with electroincs support at @fudgemart",
    "The digital downloads section of #fudgemart looks abandoned.",
    "Digital downloads selection on fudgemart is freakishly small. #bad",
    "Why is customer support so bad at @fudgemart? #frustrated.",
    "Shipping takes forever. so slow.",
    "Fudgemart's digital downloads: paltry!",
    "Fudgemart's digital downloads is lacking titles!",
    "Fudgemart's digital downloads selection is uneventful!",
    "Hey fudgemart, why is your support so bad? #frustrated",
    "Hey fudgemart, why is your support so bad? #angry",
    "Hey fudgemart, why is your support so bad? #upset",
    "Worst purchase ever: digital downloads at @fudgemart.",
    "Worst purchase ever:jewelry at @fudgemart.",
    "The shipping process is flawed. Two weeks? Really? #fudgemart"
    ]


def printUsage():    
    print('python simtweet.py -c <count> -s <start-date> -e <end-date> -f <format>')
    print('python simtweet.py --count=<count> --startdate=<start-date> --enddate=<end-date> --format=<format>')
    print('')
    print('<count> is the number of tweets to generate')
    print('<start-date> is the date and time of the earliest tweet')
    print('<end-date> is the date and time of the latest tweet.')
    print('<format> is either json or psv (pipe-separated values)')
    print('')
    print('This prints 10 random tweets in the year 2015 output as json.')
    print('python simtweet.py -c 10 -s "1/1/2015 12:00 AM" -e "12/31/2015 11:59 PM" -f json')

def getCommandArgs(argv):
    try:
        count = 0
        startDate = ""
        endDate = ""
        outFormat = ""
        opts, args = getopt.getopt(argv,"c:s:e:f:",["count=","startdate=","enddate=","format="])

    except getopt.GetoptError as err:
        print(err)
        printUsage()
        sys.exit(2)

    for opt,arg in opts:
        if opt in ("-c", "--count"):
            count = arg
        elif opt in ("-s", "--startdate"):
            startDate = arg
        elif opt in ("-e", "--enddate"):
            endDate = arg
        elif opt in ("-f","--format"):
            outFormat = arg
    # check args
    if count == 0 or startDate== "" or endDate == "" or outFormat not in ('json','psv'):
        printUsage()
        sys.exit(2)
    return count, startDate, endDate, outFormat

def generateTweets(users, count, start, end, fmt):
    tweets = []
    for i in range(1, int(count)+1):
        r = random.random()
        while True:
            user = random.choice(users)
            if r <= user['tweet_prob']: # this user can tweet
                p = random.random()
                if p <= user['pos']:
                    text = positiveTweet(positive)
                elif p <= user['neg']:
                    text = negativeTweet(negative)
                else:
                    text = neutralTweet(neutral)
                s = randomUnixTimestamp(start, end)
                t = tweet(s,user['name'], text)
                tweets.append(t)
                break;
    return tweets;

def toJson(tweets):
    return json.dumps(tweets)

def toPsv(tweets):
    psv = ""
    for t in tweets:
        psv += str(t['id']) + "|" + str(t['created_at_unixtime']) + "|" + t['created_at'] + "|" + t['user'] + "|" + t['text'] + "\n"
    return psv

# generate a pisitive tweet with optional hashtag and product category
def positiveTweet(positive):
    return random.choice(positive)

def negativeTweet(negative):
    return random.choice(negative)

def neutralTweet(neutral):
    return random.choice(neutral)

def tweet(timeStamp,user,text):
    id = int(uuid.uuid4()) & (1<<62)-1
    unixtime = timeStamp
    timestamp= toTimeString(timeStamp)
    tweet = { "id" : id,
              "created_at_unixtime" : unixtime,
              "created_at" : timestamp,
              "user" : user,
              "text" : text }
    return tweet

def toTimeString(timeStamp):
    return time.strftime('%a %b %d %H:%M:%S +0000 %Y', time.localtime(timeStamp))

def randomUnixTimestamp(startTimeString, endTimeString, format_string = '%m/%d/%Y %I:%M %p'):
    stime = time.mktime(time.strptime(startTimeString, format_string))
    etime = time.mktime(time.strptime(endTimeString, format_string))
    randomTime = stime + random.random() * (etime - stime)
    return randomTime


# main
count, startDate, endDate, outFormat = getCommandArgs(sys.argv[1:])
tweets = generateTweets(users, count, startDate, endDate, outFormat)
if outFormat =='json':
    print(toJson(tweets),end='')
else:
    print(toPsv(tweets),end='')
