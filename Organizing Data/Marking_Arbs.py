import pandas as pd
from IPython.display import display

# want to go through collected data and record where an arb occurs as well as some basic info about this recording.

# Basic: added implied probabilities , between which bookmakers, what game it occured at, what sport, 
# Other info: how many days before the game, what were the preceding odds, how long did arb last,  
# Less Basic: timeline of major headlines or events preceding arb. How to define a major headline produced, where to get these headlines CBS?.

TeamA = "sea" #this should be the first team in the title of the game for example TeamA_at_TeamB
TeamB = "lv"

def List_implied_prob(values):
    new_list = []
    for i in values:
        new_list.append(1/i)
    return new_list



def Find_Arbs(filename):
    try:
        df = pd.read_csv(filename)
    except:
        print("error opening csv file")
    
    headers = list(df.columns.values)
    
    #Fandual odds
    TeamA_FD = df[headers[2]].to_list()
    TeamB_FD =  df[headers[3]].to_list()
    
    #Cesears odds
    TeamA_C = df[headers[4]].to_list()
    TeamB_C = df[headers[5]].to_list()

    #Bet365 odds
    TeamA_BT = df[headers[6]].to_list()
    TeamB_BT = df[headers[7]].to_list()

    #Draft Kings odds
    TeamA_DK = df[headers[8]].to_list()
    TeamB_DK = df[headers[9]].to_list()

    #BetMGM odds
    TeamA_BM = df[headers[10]].to_list()
    TeamB_BM = df[headers[11]].to_list()

    print(TeamA_FD)
    print("=========================================")
    print(List_implied_prob(TeamA_FD))

    
Find_Arbs("Getting_data/Games Data/sea-at-hou 301482")