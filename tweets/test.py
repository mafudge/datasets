import sys
import getopt

def printUsage():    
    print('python test.py -c <count> -s <start-date> -e <end-date> -f <format>')
    print('python test.py --count=<count> --startdate=<start-date> --enddate=<end-date> --format=<format>')
    print('')
    print('<count> is the number of tweets to generate')
    print('<start-date> is the date and time of the earliest tweet')
    print('<end-date> is the date and time of the latest tweet.')
    print('<format> is either json or psv (pipe-separated values)')
    print('')
    print('This prints 10 random tweets in the year 2015 output as json.')
    print('python test.py -c 10 -s "1/1/2015 12:00 AM" -e "12/31/2015 11:59 PM" -f json')

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
        


count, startDate, endDate, outFormat = getCommandArgs(sys.argv[1:])
print(count,startDate, endDate, outFormat)



