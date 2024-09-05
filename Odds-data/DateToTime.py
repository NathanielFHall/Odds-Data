#basic script to parse dates from covers.com

from datetime import datetime
MONTH = {'Jan': 1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
current_time = datetime.now()

YEAR = str(current_time.year)[2:]
#example input'Sep|2|15:34|ET'
#example output 24:9:2:15:34

#year:month:day:hour:minute
#transform covers dates into timestamps
def DatetoTime(string):
    j = 0
    for i in range(len(string)):
        if string[i] =="|":
            j+=1
        if j == 1 and string[i] == "|":
            m = i
            try:
                month = str(MONTH[string[:m]])
            except:
                print("ERROR: DatetoTime script probably a key error with MONTH dict")

        if j == 2 and string[i]=="|":
            d = i
            day = string[m+1:d]
            hour_min = string[d+1:len(string)-3]

    return YEAR+":"+month+":"+day+":"+hour_min



#Parse Example: '\n\n                            \r\n\r\nMon, Sep 2\n                            \r\n\r\n17:59 ET (ET)\n                        \n'
#output example: 24:9:2:15:34 
def parseDate(string):
    date = ""
    j = 0;
    newstr = string.replace(" ","|")
    for i in range(len(newstr)):
        
        if newstr[i].isalnum() or newstr[i]=="|" or  newstr[i]==":" :
            date+=newstr[i]
    return DatetoTime(date.replace("|||","").replace("ET|ET","ET")[5:])  