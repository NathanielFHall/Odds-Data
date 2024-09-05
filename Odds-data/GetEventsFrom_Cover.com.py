import requests
from bs4 import BeautifulSoup
from datetime import datetime
import lineMovementHistory

MONTH = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
current_time = datetime.now()

games = {}

#These are the games that have the most line movement history i.e. games that are happening today
full_data_games = []
IDs = []

full_line_history_link = {}

#parse the sections of the matchup link by / seperated values into a list
def parse_link(string):
    parts = []
    j = 0;
    for i in range(len(string)):
        if string[i] =="/":
            parts.append(string[j+1:i])
            j = i;
    parts.append(string[j+1:])
    return parts


#parse the date of string including taking any string that says Today in it and putting the actual date in.
def parse_date(string):
     for i in range(len(string)):
        if "Today" in string:
            return MONTH[current_time.month-1]+" "+str(current_time.day)
        if string[i] ==",":
            return string[:i]





 
def getEvents_Covers():
    webpage = "https://www.covers.com/sport/odds"
    page = requests.get(webpage)
    soup = BeautifulSoup(page.content, "html.parser")


    # finds all the different tables on the webpage for each event
    oddsGameRow = soup.find_all(class_="oddsGameRow")


    for i in oddsGameRow:
        #find out the date of the game
        game_time = i.find(class_="td-cell game-time")
        
        if game_time != None:
            game_date = game_time.find_all("span")[0].text
        
        #find the teams playing
        teams  = i.find_all("strong")

        #find the game id
        lineHistoryBrick  = i.find(class_="lineHistoryBrick" )
        if lineHistoryBrick != None:
            gameID = lineHistoryBrick["data-game"]


        #add all of this information to a dictionary that stores the teams playing and when they are playing and the sport they are in   
        if len(teams)>0:
          #adds the games happening today to a specific dictionary full_data_games
          if "Today" in game_date:
              full_data_games.append(gameID)
          games[gameID] = [teams[0].text.lower()+"-at-"+teams[1].text.lower(),parse_date(game_date)]
          
 
   
    links = soup.find_all("a")
    for i in links:
        if "Matchup" in i.contents:
            sport = parse_link(i["href"])[2]
            league = parse_link(i["href"])[3]
            id = parse_link(i["href"])[5]

            #this is needed so that the program doesn't add the same info twice to the same game id
            if id in IDs:
                pass
            
            
            else:
                IDs.append(id)
                games[id].append(sport)
                games[id].append(league)
    

getEvents_Covers()


#create the links for full line history

#EXAMPLE LINK: https://www.covers.com/sport/basketball/nba/linemovement/ind-at-det/315483
for i in IDs:
    full_line_history_link[i] = "https://www.covers.com/sport/"+games[i][2]+"/"+games[i][3]+"/linemovement/"+games[i][0]+"/"+i

for i in full_line_history_link:
    try:
        lineMovementHistory.scrape(full_line_history_link[i])
        print("================================="+"\n")
    except:
        print("SCRAPING ERROR")
        print(full_line_history_link[i])
        print("================================="+"\n")