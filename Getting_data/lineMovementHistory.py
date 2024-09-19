import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import DateToTime
from IPython.display import display

link = "https://www.covers.com/sport/baseball/mlb/linemovement/min-at-tb/301204"





#return team abreviations from link in the form [teamA,teamB]
def teams(string):
    j = 0;
    TeamA = ""
    TeamB = ""
    teamString = ""
    for i in string:
        if i == "/":
            j+=1
        if j == 7:
                teamString +=i
    for k in range(len(teamString)):
        n = 0
        if teamString[k] == "-":
            n+=1
            TeamA = teamString[1:k-3]
        if teamString[k] == "-" and n==1:
             TeamB = teamString[k+1:]
    return [TeamA,TeamB]


#check if date is in sportsbook dict if not put "N/A" for now

def checkDate(Sportsbook,df_dates):
    for i in Sportsbook:
        if i in df_dates:
            pass
        else:
            df_dates.append(i)




#This is going to return a time series dataframe of the change in odds
def scrape(link):
    FD = {};
    C = {};
    B3 = {};
    DK = {};
    MGM = {};

    ROWS = []

    df_dates = []
    TeamA = teams(link)[0]
    TeamB = teams(link)[1]

    page = requests.get(link)
    
    
    soup = BeautifulSoup(page.content, "html.parser")

    moneyline = soup.find(id="tab-moneyline")
    Tables = moneyline.find_all(class_="row covers-CoversMatchups-matchupDetailsBlock")
    for i in range(len(Tables)):
         rows = Tables[i].find_all("tr")
         
         
         for j in range(len(rows)):
                try:
                    date = rows[j].find("td").text
                    decimals = rows[j].find_all(class_="Decimal")
                    if i == 0:
                        FD[DateToTime.parseDate(date)]=[decimals[0].text,decimals[1].text]
                    if i == 1:
                        C[DateToTime.parseDate(date)]=[decimals[0].text,decimals[1].text]
                    if i == 2:
                        B3[DateToTime.parseDate(date)]=[decimals[0].text,decimals[1].text]
                    if i == 3:
                        DK[DateToTime.parseDate(date)]=[decimals[0].text,decimals[1].text]
                    if i == 4:
                        MGM[DateToTime.parseDate(date)]=[decimals[0].text,decimals[1].text]
                except:
                    pass
    checkDate(FD,df_dates)
    checkDate(C,df_dates)
    checkDate(B3,df_dates)
    checkDate(DK,df_dates)
    checkDate(MGM,df_dates)
   
    for i in range(len(df_dates)):
        date = df_dates[i];
        if date in FD:
            pass
        else:
            FD[date] = ["N/A","N/A"]
        if date in B3:
            pass
        else:
            B3[date] =["N/A","N/A"]
        if date in C:
            pass
        else:
            C[date] = ["N/A","N/A"]
        if date in DK:
            pass
        else:
            DK[date] = ["N/A","N/A"]
        if date in MGM:
            pass
        else:
            MGM[date] = ["N/A","N/A"]
        
        row = [date,FD[date],C[date],B3[date],DK[date],MGM[date]]
        ROWS.append(row)
        

    #sort rows list
    def e(x):
        return int(x[0].replace(":",""))
    ROWS.sort(key=e)    

    
    #get starting odds
    def startingOdds(index):
        for k in range(len(ROWS)):
            if ROWS[k][index] == ["N/A","N/A"]:
                pass
            else:
                return [k,ROWS[k][index]]
            
 

    #fill in missing dates
    for x in range(5):
        y = x+1
        odds = startingOdds(y)[1]
        for i in range(len(ROWS)):
            
            if i > startingOdds(y)[0]:
                if ROWS[i][y] == ["N/A","N/A"]:
                    ROWS[i][y] = odds
                else:
                    odds = ROWS[i][y]; 
                

    df_ROW = [];
    df_ROWS = []
    #converting it into a list that can be added to the dataframe
    for i in ROWS:

        df_ROW = [i[0],i[1][0],i[1][1],i[2][0],i[2][1],i[3][0],i[3][1],i[4][0],i[4][1],i[5][0],i[5][1]]
        df_ROWS.append(df_ROW)
   
    df = pd.DataFrame(df_ROWS,columns=["Date","Fanduel Odds["+TeamA+"]","Fanduel Odds["+TeamB+"]","Cesears Odds["+TeamA+"]","Cesears Odds["+TeamB+"]","Bet365 Odds["+TeamA+"]","Bet365 Odds["+TeamB+"]","DraftKings Odds["+TeamA+"]","DraftKings Odds["+TeamB+"]","BetMGM Odds["+TeamA+"]","BetMGM Odds["+TeamB+"]"])
    display(df)
    return df




