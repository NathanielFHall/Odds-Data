#takes dataframe of each event and puts them into a textfile/multiple textfiles?
#takes dataframe of general info and adds it to a csv textfile
#uploads these file to github?
from datetime import datetime
current_time = datetime.now()

MONTH = {'Jan': 1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
ABC = {'|':'27','_':'00','a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07', 'h': '08', 'i': '09', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
abc = ['_','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','|']
sports = {"soccer":0, "basketball":1,"baseball":2, "football":3,"hockey":4,"golf":5,"other":6}
sportslist = ["soccer", "basketball","baseball", "football","hockey","golf","other"]

#function to attatch an ID to any data point
#input [teamA-at-teamB,date,sport,league]
#needs work
def getID(info,coversID):
    while len(coversID)<6:
        coversID+="0"
    ID = str(coversID)+"-"
    if info[2] in sports.keys():
        ID+=str(sports[info[2]])
    else:
        ID+="6"
    TeamA = ""
    TeamB = ""
    teamString = info[0]
    for k in range(len(teamString)):
        n = 0
        if teamString[k] == "-":
            n+=1
            TeamA = teamString[:k-3]
        if teamString[k] == "-" and n==1:
             TeamB = teamString[k+1:]
    while len(TeamA)<3:
        TeamA+="_"
    while len(TeamB)<3:
        TeamB+="_"
    
    for i in TeamA[:3]+"|"+TeamB[:3]:
        ID+=ABC[i];
        
    monthNum = str(MONTH[info[1][:3]])
    ID+=monthNum
    if len(info[1][4:])<2:
        ID+="0"+info[1][4:]
    else:
        ID+= info[1][4:]
    return ID

#needs work
def getInfoFromID(ID):
    for a in range(len(ID)):
        if ID[a] == "-":
            k = a
    
    sport = sportslist[int(ID[k+1])]
    gameID = ID[:k]
    date = ID[k+16]+"-"+ID[k+16:]
    teams = ""
    for i in range(7):
        j = 2*i
        
        teams+=abc[int(ID[j+8]+ID[j+9])]
    return [gameID,sport,teams,date]


#print(getID(['sea-at-ny', 'Sep 5', 'basketball', 'wnba'],302895))
#print(getInfoFromID("302895-219050127142500905"))

