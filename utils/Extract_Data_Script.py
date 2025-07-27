from collections import OrderedDict

def basicGameInfo(data):
        
    #   Game Stage Info
    stages = data["Stage"].unique()
    stage = stages[0]
    
    #   Game Year Info    
    years = data["Year"].unique()
    year = years[0]
        
    #   Game Tournament Info
    tournaments = data["Tournament"].unique()
    tournament = tournaments[0]
        
    #   Game Club Info
    clubs = data["Club"].unique()
    club = clubs[0]

    #   Game Date Info
    dates = data["Match Date"].unique()
    date = dates[0]

    #   Chukka Info
    Chukkas = data["Chukka"].unique()
    total_chukkas = len(Chukkas)

    return (stage, year, tournament, club, date, total_chukkas)

def separateTeamsData(data):

    #   Team Names
    teams = data["Team"].unique()
    team1 = teams[0]
    team2 = teams[1]

    #   Storing Separate Teams Data
    data1 = data[data["Team"]==team1]
    data2 = data[data["Team"]==team2]

    #   Goals by Each Team
    goals1 = len(data1["Goal"].dropna())
    goals2 = len(data2["Goal"].dropna())
    goal_diff = goals1-goals2
    
    #   Fouls by Each Team    
    fouls1 = len(data1[data1["Foul"]=="Foul"])
    fouls2 = len(data2[data2["Foul"]=="Foul"])
        
    return (team1, team2, data1, data2, goals1, goals2, goal_diff, fouls1, fouls2)
    
def shotAtGoalInfo(data1, data2):

    #   Shot At Goal by Each team
    shotAtGoal1 = len(data1["Shot At Goal"].dropna())
    shotAtGoal2 = len(data2["Shot At Goal"].dropna())
    
    shotAtGoal_diff = shotAtGoal1-shotAtGoal2
    
    #   Shot At Goal Outcome Goal by Each team
    shotAtGoalOutcomeGoal1 = len(data1[data1["Shot At Goal Outcome"]=="Goal"])
    shotAtGoalOutcomeGoal2 = len(data2[data2["Shot At Goal Outcome"]=="Goal"])
    
    shotAtGoalOutcomeGoal_diff = shotAtGoalOutcomeGoal1-shotAtGoalOutcomeGoal2
    
    #   Shot At Goal Percent by Each Team
    if shotAtGoal1==0:
        shotAtGoalOutcomeGoalPercent1 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutcomeGoalPercent1 = int(round((shotAtGoalOutcomeGoal1/shotAtGoal1)*100))
    
    if shotAtGoal2==0:
        shotAtGoalOutcomeGoalPercent2 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutcomeGoalPercent2 = int(round((shotAtGoalOutcomeGoal2/shotAtGoal2)*100))

    if (shotAtGoal1 != 0) & (shotAtGoal2 != 0):
        shotAtGoalOutcomeGoalPercent_diff = shotAtGoalOutcomeGoalPercent1-shotAtGoalOutcomeGoalPercent2
    else:
        shotAtGoalOutcomeGoalPercent_diff = "Not_Valid_(Zero_Division)"
    
    return (shotAtGoal1, shotAtGoal2,
            shotAtGoal_diff,
            shotAtGoalOutcomeGoal1, shotAtGoalOutcomeGoal2,
            shotAtGoalOutcomeGoal_diff,
            shotAtGoalOutcomeGoalPercent1, shotAtGoalOutcomeGoalPercent2,
            shotAtGoalOutcomeGoalPercent_diff)
    
    
def penaltyInfo(data1, data2):
    penaltyShots1 = len(data1["Penalty Outcome"].dropna())
    penaltyShots2 = len(data2["Penalty Outcome"].dropna())
    
    penaltyShotsGoal1 = len(data1[data1["Penalty Outcome"]=="Goal"])
    penaltyShotsGoal2 = len(data2[data2["Penalty Outcome"]=="Goal"])

    if penaltyShots1==0:
        penaltyShotsGoalPercent1 = "Not_Valid_(Zero_Division)"
    else:
        penaltyShotsGoalPercent1 = int(round((penaltyShotsGoal1/penaltyShots1)*100))
    
    if penaltyShots2==0:
        penaltyShotsGoalPercent2 = "Not_Valid_(Zero_Division)"
    else:
        penaltyShotsGoalPercent2 = int(round((penaltyShotsGoal2/penaltyShots2)*100))

    return (penaltyShots1, penaltyShots2,
            penaltyShotsGoal1, penaltyShotsGoal2,
            penaltyShotsGoalPercent1, penaltyShotsGoalPercent2)

def topPlayersInfo(data1, data2):
    data1_a = data1.loc[data1["Goal"].dropna().index]
    data2_a = data2.loc[data2["Goal"].dropna().index]
    
    dictionary1 = OrderedDict(data1_a.groupby(["Player"]).count()["Name"])
    dictionary2 = OrderedDict(data2_a.groupby(["Player"]).count()["Name"])
    
    if len(dictionary1)>0:
        topPlayerGoals1 = next(iter(dictionary1.values()))
    else:
        topPlayerGoals1 = None

    if len(dictionary2)>0:
        topPlayerGoals2 = next(iter(dictionary2.values()))
    else:
        topPlayerGoals2 = None
    
    topPlayers1 = [ key for key, value in dictionary1.items() if value == topPlayerGoals1 ]
    topPlayers2 = [ key for key, value in dictionary2.items() if value == topPlayerGoals2 ]
    
    totalTopPlayers1 = len(topPlayers1)
    totalTopPlayers2 = len(topPlayers2)

    return (topPlayerGoals1, topPlayerGoals2,
            topPlayers1, topPlayers2,
            totalTopPlayers1, totalTopPlayers2)

def topAssistsInfo(data1, data2):
    data1_a = data1[data1["Assist Outcome"]=="Successful"]
    data2_a = data2[data2["Assist Outcome"]=="Successful"]
    
    dictionary1 = OrderedDict(data1_a["Assist"].value_counts())
    dictionary2 = OrderedDict(data2_a["Assist"].value_counts())

    if len(dictionary1)>0:
        topAssistGoals1 = next(iter(dictionary1.values()))
    else:
        topAssistGoals1 = None

    if len(dictionary2)>0:
        topAssistGoals2 = next(iter(dictionary2.values()))
    else:
        topAssistGoals2 = None
    
    topAssists1 = [ key for key, value in dictionary1.items() if value == topAssistGoals1 ]
    topAssists2 = [ key for key, value in dictionary2.items() if value == topAssistGoals2 ]
    
    totalTopAssists1 = len(topAssists1)
    totalTopAssists2 = len(topAssists2)

    return (topAssistGoals1, topAssistGoals2,
            topAssists1, topAssists2,
            totalTopAssists1, totalTopAssists2)

def topPlayerAssist(topPlayers1, topPlayers2,
                    topAssists1, topAssists2):
    bothTopPlayerAssist1 = list(set(topPlayers1).intersection(topAssists1))
    bothTopPlayerAssist2 = list(set(topPlayers2).intersection(topAssists2))

    return (bothTopPlayerAssist1,
            bothTopPlayerAssist2)

############################ Using Chukka ############################

def goalsChukka(data1, data2):
    data1_goal = data1.loc[data1["Goal"].dropna().index]
    goals1Chukka1 = len(data1_goal[data1_goal["Chukka"]=="Chukka 1"])
    goals1Chukka2 = len(data1_goal[data1_goal["Chukka"]=="Chukka 2"])
    goals1Chukka3 = len(data1_goal[data1_goal["Chukka"]=="Chukka 3"])
    goals1Chukka4 = len(data1_goal[data1_goal["Chukka"]=="Chukka 4"])
    goals1Chukka5 = len(data1_goal[data1_goal["Chukka"]=="Chukka 5"])
    goals1Chukka6 = len(data1_goal[data1_goal["Chukka"]=="Chukka 6"])
    
    data2_goal = data2.loc[data2["Goal"].dropna().index]
    goals2Chukka1 = len(data2_goal[data2_goal["Chukka"]=="Chukka 1"])
    goals2Chukka2 = len(data2_goal[data2_goal["Chukka"]=="Chukka 2"])
    goals2Chukka3 = len(data2_goal[data2_goal["Chukka"]=="Chukka 3"])
    goals2Chukka4 = len(data2_goal[data2_goal["Chukka"]=="Chukka 4"])
    goals2Chukka5 = len(data2_goal[data2_goal["Chukka"]=="Chukka 5"])
    goals2Chukka6 = len(data2_goal[data2_goal["Chukka"]=="Chukka 6"])
    
    goalsChukka1_diff = goals1Chukka1 - goals2Chukka1
    goalsChukka2_diff = goals1Chukka2 - goals2Chukka2
    goalsChukka3_diff = goals1Chukka3 - goals2Chukka3
    goalsChukka4_diff = goals1Chukka4 - goals2Chukka4
    goalsChukka5_diff = goals1Chukka5 - goals2Chukka5
    goalsChukka6_diff = goals1Chukka6 - goals2Chukka6 

    return (goals1Chukka1,goals1Chukka2,goals1Chukka3,
            goals1Chukka4,goals1Chukka5,goals1Chukka6,
            goals2Chukka1,goals2Chukka2,goals2Chukka3,
            goals2Chukka4,goals2Chukka5,goals2Chukka6,
            goalsChukka1_diff,goalsChukka2_diff,
            goalsChukka3_diff,goalsChukka4_diff,
            goalsChukka5_diff,goalsChukka6_diff
            )

def shotAtGoalChukka(data1, data2):
    data1_shotAtGoal = data1.loc[data1["Shot At Goal"].dropna().index]
    shotAtGoal1Chukka1 = len(data1_shotAtGoal[data1_shotAtGoal["Chukka"]=="Chukka 1"])
    shotAtGoal1Chukka2 = len(data1_shotAtGoal[data1_shotAtGoal["Chukka"]=="Chukka 2"])
    shotAtGoal1Chukka3 = len(data1_shotAtGoal[data1_shotAtGoal["Chukka"]=="Chukka 3"])
    shotAtGoal1Chukka4 = len(data1_shotAtGoal[data1_shotAtGoal["Chukka"]=="Chukka 4"])
    shotAtGoal1Chukka5 = len(data1_shotAtGoal[data1_shotAtGoal["Chukka"]=="Chukka 5"])
    shotAtGoal1Chukka6 = len(data1_shotAtGoal[data1_shotAtGoal["Chukka"]=="Chukka 6"])
    
    data2_shotAtGoal = data2.loc[data2["Shot At Goal"].dropna().index]
    shotAtGoal2Chukka1 = len(data2_shotAtGoal[data2_shotAtGoal["Chukka"]=="Chukka 1"])
    shotAtGoal2Chukka2 = len(data2_shotAtGoal[data2_shotAtGoal["Chukka"]=="Chukka 2"])
    shotAtGoal2Chukka3 = len(data2_shotAtGoal[data2_shotAtGoal["Chukka"]=="Chukka 3"])
    shotAtGoal2Chukka4 = len(data2_shotAtGoal[data2_shotAtGoal["Chukka"]=="Chukka 4"])
    shotAtGoal2Chukka5 = len(data2_shotAtGoal[data2_shotAtGoal["Chukka"]=="Chukka 5"])
    shotAtGoal2Chukka6 = len(data2_shotAtGoal[data2_shotAtGoal["Chukka"]=="Chukka 6"])    

    shotAtGoalChukka1_diff = shotAtGoal1Chukka1-shotAtGoal2Chukka1
    shotAtGoalChukka2_diff = shotAtGoal1Chukka2-shotAtGoal2Chukka2
    shotAtGoalChukka3_diff = shotAtGoal1Chukka3-shotAtGoal2Chukka3
    shotAtGoalChukka4_diff = shotAtGoal1Chukka4-shotAtGoal2Chukka4
    shotAtGoalChukka5_diff = shotAtGoal1Chukka5-shotAtGoal2Chukka5
    shotAtGoalChukka6_diff = shotAtGoal1Chukka6-shotAtGoal2Chukka6

    data1_shotAtGoalOutGoal = data1[data1["Shot At Goal Outcome"]=="Goal"]
    shotAtGoalOutGoal1Chukka1 = len(data1_shotAtGoalOutGoal[data1_shotAtGoalOutGoal["Chukka"]=="Chukka 1"])
    shotAtGoalOutGoal1Chukka2 = len(data1_shotAtGoalOutGoal[data1_shotAtGoalOutGoal["Chukka"]=="Chukka 2"])
    shotAtGoalOutGoal1Chukka3 = len(data1_shotAtGoalOutGoal[data1_shotAtGoalOutGoal["Chukka"]=="Chukka 3"])
    shotAtGoalOutGoal1Chukka4 = len(data1_shotAtGoalOutGoal[data1_shotAtGoalOutGoal["Chukka"]=="Chukka 4"])
    shotAtGoalOutGoal1Chukka5 = len(data1_shotAtGoalOutGoal[data1_shotAtGoalOutGoal["Chukka"]=="Chukka 5"])
    shotAtGoalOutGoal1Chukka6 = len(data1_shotAtGoalOutGoal[data1_shotAtGoalOutGoal["Chukka"]=="Chukka 6"])
    
    data2_shotAtGoalOutGoal = data2[data2["Shot At Goal Outcome"]=="Goal"]
    shotAtGoalOutGoal2Chukka1 = len(data2_shotAtGoalOutGoal[data2_shotAtGoalOutGoal["Chukka"]=="Chukka 1"])
    shotAtGoalOutGoal2Chukka2 = len(data2_shotAtGoalOutGoal[data2_shotAtGoalOutGoal["Chukka"]=="Chukka 2"])
    shotAtGoalOutGoal2Chukka3 = len(data2_shotAtGoalOutGoal[data2_shotAtGoalOutGoal["Chukka"]=="Chukka 3"])
    shotAtGoalOutGoal2Chukka4 = len(data2_shotAtGoalOutGoal[data2_shotAtGoalOutGoal["Chukka"]=="Chukka 4"])
    shotAtGoalOutGoal2Chukka5 = len(data2_shotAtGoalOutGoal[data2_shotAtGoalOutGoal["Chukka"]=="Chukka 5"])
    shotAtGoalOutGoal2Chukka6 = len(data2_shotAtGoalOutGoal[data2_shotAtGoalOutGoal["Chukka"]=="Chukka 6"])

    shotAtGoalOutGoalChukka1_diff = shotAtGoalOutGoal1Chukka1-shotAtGoalOutGoal2Chukka1
    shotAtGoalOutGoalChukka2_diff = shotAtGoalOutGoal1Chukka2-shotAtGoalOutGoal2Chukka2
    shotAtGoalOutGoalChukka3_diff = shotAtGoalOutGoal1Chukka3-shotAtGoalOutGoal2Chukka3
    shotAtGoalOutGoalChukka4_diff = shotAtGoalOutGoal1Chukka4-shotAtGoalOutGoal2Chukka4
    shotAtGoalOutGoalChukka5_diff = shotAtGoalOutGoal1Chukka5-shotAtGoalOutGoal2Chukka5
    shotAtGoalOutGoalChukka6_diff = shotAtGoalOutGoal1Chukka6-shotAtGoalOutGoal2Chukka6

    if shotAtGoal1Chukka1==0:
        shotAtGoalOutGoalPer1Chukka1 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer1Chukka1 = int(round((shotAtGoalOutGoal1Chukka1/shotAtGoal1Chukka1)*100))
    
    if shotAtGoal1Chukka2==0:
        shotAtGoalOutGoalPer1Chukka2 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer1Chukka2 = int(round((shotAtGoalOutGoal1Chukka2/shotAtGoal1Chukka2)*100))
    
    if shotAtGoal1Chukka3==0:
        shotAtGoalOutGoalPer1Chukka3 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer1Chukka3 = int(round((shotAtGoalOutGoal1Chukka3/shotAtGoal1Chukka3)*100))
    
    if shotAtGoal1Chukka4==0:
        shotAtGoalOutGoalPer1Chukka4 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer1Chukka4 = int(round((shotAtGoalOutGoal1Chukka4/shotAtGoal1Chukka4)*100))
    
    if shotAtGoal1Chukka5==0:
        shotAtGoalOutGoalPer1Chukka5 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer1Chukka5 = int(round((shotAtGoalOutGoal1Chukka5/shotAtGoal1Chukka5)*100))
        
    if shotAtGoal1Chukka6==0:
        shotAtGoalOutGoalPer1Chukka6 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer1Chukka6 = int(round((shotAtGoalOutGoal1Chukka6/shotAtGoal1Chukka6)*100))    
        
    #########################    
        
    if shotAtGoal2Chukka1==0:
        shotAtGoalOutGoalPer2Chukka1 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer2Chukka1 = int(round((shotAtGoalOutGoal2Chukka1/shotAtGoal2Chukka1)*100))
    
    if shotAtGoal2Chukka2==0:
        shotAtGoalOutGoalPer2Chukka2 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer2Chukka2 = int(round((shotAtGoalOutGoal2Chukka2/shotAtGoal2Chukka2)*100))
    
    if shotAtGoal2Chukka3==0:
        shotAtGoalOutGoalPer2Chukka3 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer2Chukka3 = int(round((shotAtGoalOutGoal2Chukka3/shotAtGoal2Chukka3)*100))
    
    if shotAtGoal2Chukka4==0:
        shotAtGoalOutGoalPer2Chukka4 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer2Chukka4 = int(round((shotAtGoalOutGoal2Chukka4/shotAtGoal2Chukka4)*100))
    
    if shotAtGoal2Chukka5==0:
        shotAtGoalOutGoalPer2Chukka5 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer2Chukka5 = int(round((shotAtGoalOutGoal2Chukka5/shotAtGoal2Chukka5)*100))
        
    if shotAtGoal2Chukka6==0:
        shotAtGoalOutGoalPer2Chukka6 = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer2Chukka6 = int(round((shotAtGoalOutGoal2Chukka6/shotAtGoal2Chukka6)*100))        

    ###############################################

    shotAtGoalsFirstHalf1 = shotAtGoal1Chukka1+shotAtGoal1Chukka2+shotAtGoal1Chukka3
    shotAtGoalsFirstHalf2 = shotAtGoal2Chukka1+shotAtGoal2Chukka2+shotAtGoal2Chukka3
    shotAtGoalsSecondHalf1 = shotAtGoal1Chukka4+shotAtGoal1Chukka5+shotAtGoal1Chukka6
    shotAtGoalsSecondHalf2 = shotAtGoal2Chukka4+shotAtGoal2Chukka5+shotAtGoal2Chukka6
    shotAtGoalsFirstHalf_diff = shotAtGoalsFirstHalf1 - shotAtGoalsFirstHalf2
    shotAtGoalsSecondHalf_diff = shotAtGoalsSecondHalf1 - shotAtGoalsSecondHalf2
    shotAtGoalsOutGoalsFirstHalf1 = shotAtGoalOutGoal1Chukka1+shotAtGoalOutGoal1Chukka2+shotAtGoalOutGoal1Chukka3
    shotAtGoalsOutGoalsFirstHalf2 = shotAtGoalOutGoal2Chukka1+shotAtGoalOutGoal2Chukka2+shotAtGoalOutGoal2Chukka3
    shotAtGoalsOutGoalsSecondHalf1 = shotAtGoalOutGoal1Chukka4+shotAtGoalOutGoal1Chukka5+shotAtGoalOutGoal1Chukka6
    shotAtGoalsOutGoalsSecondHalf2 = shotAtGoalOutGoal2Chukka4+shotAtGoalOutGoal2Chukka5+shotAtGoalOutGoal2Chukka6
    shotAtGoalsOutGoalsFirstHalf_diff = shotAtGoalsOutGoalsFirstHalf1 - shotAtGoalsOutGoalsFirstHalf2
    shotAtGoalsOutGoalsSecondHalf_diff = shotAtGoalsOutGoalsSecondHalf1 - shotAtGoalsOutGoalsSecondHalf2

    if shotAtGoalsFirstHalf1==0:
        shotAtGoalOutGoalPer1FHalf = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer1FHalf = int(round((shotAtGoalsOutGoalsFirstHalf1/shotAtGoalsFirstHalf1)*100))

    if shotAtGoalsSecondHalf1==0:
        shotAtGoalOutGoalPer1SHalf = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer1SHalf = int(round((shotAtGoalsOutGoalsSecondHalf1/shotAtGoalsSecondHalf1)*100))

    if shotAtGoalsFirstHalf2==0:
        shotAtGoalOutGoalPer2FHalf = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer2FHalf = int(round((shotAtGoalsOutGoalsFirstHalf2/shotAtGoalsFirstHalf2)*100))

    if shotAtGoalsSecondHalf2==0:
        shotAtGoalOutGoalPer2SHalf = "Not_Valid_(Zero_Division)"
    else:
        shotAtGoalOutGoalPer2SHalf = int(round((shotAtGoalsOutGoalsSecondHalf2/shotAtGoalsSecondHalf2)*100))


    return (shotAtGoal1Chukka1,shotAtGoal1Chukka2,shotAtGoal1Chukka3,
            shotAtGoal1Chukka4,shotAtGoal1Chukka5,shotAtGoal1Chukka6,
            shotAtGoal2Chukka1,shotAtGoal2Chukka2,shotAtGoal2Chukka3,
            shotAtGoal2Chukka4,shotAtGoal2Chukka5,shotAtGoal2Chukka6,
            shotAtGoalChukka1_diff,shotAtGoalChukka2_diff,
            shotAtGoalChukka3_diff,shotAtGoalChukka4_diff,
            shotAtGoalChukka5_diff,shotAtGoalChukka6_diff,
            shotAtGoalOutGoal1Chukka1,shotAtGoalOutGoal1Chukka2,
            shotAtGoalOutGoal1Chukka3,shotAtGoalOutGoal1Chukka4,
            shotAtGoalOutGoal1Chukka5,shotAtGoalOutGoal1Chukka6,
            shotAtGoalOutGoal2Chukka1,shotAtGoalOutGoal2Chukka2,
            shotAtGoalOutGoal2Chukka3,shotAtGoalOutGoal2Chukka4,
            shotAtGoalOutGoal2Chukka5,shotAtGoalOutGoal2Chukka6,
            shotAtGoalOutGoalChukka1_diff,shotAtGoalOutGoalChukka2_diff,
            shotAtGoalOutGoalChukka3_diff,shotAtGoalOutGoalChukka4_diff,
            shotAtGoalOutGoalChukka5_diff,shotAtGoalOutGoalChukka6_diff,
            shotAtGoalOutGoalPer1Chukka1,shotAtGoalOutGoalPer1Chukka2,
            shotAtGoalOutGoalPer1Chukka3,shotAtGoalOutGoalPer1Chukka4,
            shotAtGoalOutGoalPer1Chukka5,shotAtGoalOutGoalPer1Chukka6,
            shotAtGoalOutGoalPer2Chukka1,shotAtGoalOutGoalPer2Chukka2,
            shotAtGoalOutGoalPer2Chukka3,shotAtGoalOutGoalPer2Chukka4,
            shotAtGoalOutGoalPer2Chukka5,shotAtGoalOutGoalPer2Chukka6,
            shotAtGoalsFirstHalf1,shotAtGoalsFirstHalf2,
            shotAtGoalsSecondHalf1,shotAtGoalsSecondHalf2,
            shotAtGoalsFirstHalf_diff,shotAtGoalsSecondHalf_diff,
            shotAtGoalsOutGoalsFirstHalf1,shotAtGoalsOutGoalsFirstHalf2,
            shotAtGoalsOutGoalsSecondHalf1,shotAtGoalsOutGoalsSecondHalf2,
            shotAtGoalsOutGoalsFirstHalf_diff,shotAtGoalsOutGoalsSecondHalf_diff,
            shotAtGoalOutGoalPer1FHalf,shotAtGoalOutGoalPer2FHalf,
            shotAtGoalOutGoalPer1SHalf,shotAtGoalOutGoalPer2SHalf)


def penaltyChukka(data1, data2):
    data1_penalty = data1.loc[data1["Penalty Outcome"].dropna().index]
    penalty1Chukka1 = len(data1_penalty[data1_penalty["Chukka"]=="Chukka 1"])
    penalty1Chukka2 = len(data1_penalty[data1_penalty["Chukka"]=="Chukka 2"])
    penalty1Chukka3 = len(data1_penalty[data1_penalty["Chukka"]=="Chukka 3"])
    penalty1Chukka4 = len(data1_penalty[data1_penalty["Chukka"]=="Chukka 4"])
    penalty1Chukka5 = len(data1_penalty[data1_penalty["Chukka"]=="Chukka 5"])
    penalty1Chukka6 = len(data1_penalty[data1_penalty["Chukka"]=="Chukka 6"])
    
    data2_penalty = data2.loc[data2["Penalty Outcome"].dropna().index]
    penalty2Chukka1 = len(data2_penalty[data2_penalty["Chukka"]=="Chukka 1"])
    penalty2Chukka2 = len(data2_penalty[data2_penalty["Chukka"]=="Chukka 2"])
    penalty2Chukka3 = len(data2_penalty[data2_penalty["Chukka"]=="Chukka 3"])
    penalty2Chukka4 = len(data2_penalty[data2_penalty["Chukka"]=="Chukka 4"])
    penalty2Chukka5 = len(data2_penalty[data2_penalty["Chukka"]=="Chukka 5"])
    penalty2Chukka6 = len(data2_penalty[data2_penalty["Chukka"]=="Chukka 6"])
    
    data1_penaltyOutGoal = data1[data1["Penalty Outcome"]=="Goal"]
    penaltyOutGoal1Chukka1 = len(data1_penaltyOutGoal[data1_penaltyOutGoal["Chukka"]=="Chukka 1"])
    penaltyOutGoal1Chukka2 = len(data1_penaltyOutGoal[data1_penaltyOutGoal["Chukka"]=="Chukka 2"])
    penaltyOutGoal1Chukka3 = len(data1_penaltyOutGoal[data1_penaltyOutGoal["Chukka"]=="Chukka 3"])
    penaltyOutGoal1Chukka4 = len(data1_penaltyOutGoal[data1_penaltyOutGoal["Chukka"]=="Chukka 4"])
    penaltyOutGoal1Chukka5 = len(data1_penaltyOutGoal[data1_penaltyOutGoal["Chukka"]=="Chukka 5"])
    penaltyOutGoal1Chukka6 = len(data1_penaltyOutGoal[data1_penaltyOutGoal["Chukka"]=="Chukka 6"])
    
    data2_penaltyOutGoal = data2[data2["Penalty Outcome"]=="Goal"]
    penaltyOutGoal2Chukka1 = len(data2_penaltyOutGoal[data2_penaltyOutGoal["Chukka"]=="Chukka 1"])
    penaltyOutGoal2Chukka2 = len(data2_penaltyOutGoal[data2_penaltyOutGoal["Chukka"]=="Chukka 2"])
    penaltyOutGoal2Chukka3 = len(data2_penaltyOutGoal[data2_penaltyOutGoal["Chukka"]=="Chukka 3"])
    penaltyOutGoal2Chukka4 = len(data2_penaltyOutGoal[data2_penaltyOutGoal["Chukka"]=="Chukka 4"])
    penaltyOutGoal2Chukka5 = len(data2_penaltyOutGoal[data2_penaltyOutGoal["Chukka"]=="Chukka 5"])
    penaltyOutGoal2Chukka6 = len(data2_penaltyOutGoal[data2_penaltyOutGoal["Chukka"]=="Chukka 6"])
    
    if penalty1Chukka1==0:
        penaltyOutGoalPer1Chukka1 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer1Chukka1 = int(round((penaltyOutGoal1Chukka1/penalty1Chukka1)*100))
        
    if penalty1Chukka2==0:
        penaltyOutGoalPer1Chukka2 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer1Chukka2 = int(round((penaltyOutGoal1Chukka2/penalty1Chukka2)*100))
    
    if penalty1Chukka3==0:
        penaltyOutGoalPer1Chukka3 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer1Chukka3 = int(round((penaltyOutGoal1Chukka3/penalty1Chukka3)*100))
    
    if penalty1Chukka4==0:
        penaltyOutGoalPer1Chukka4 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer1Chukka4 = int(round((penaltyOutGoal1Chukka4/penalty1Chukka4)*100))
    
    if penalty1Chukka5==0:
        penaltyOutGoalPer1Chukka5 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer1Chukka5 = int(round((penaltyOutGoal1Chukka5/penalty1Chukka5)*100))
    
    if penalty1Chukka6==0:
        penaltyOutGoalPer1Chukka6 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer1Chukka6 = int(round((penaltyOutGoal1Chukka6/penalty1Chukka6)*100))
    
    ##############
    
    if penalty2Chukka1==0:
        penaltyOutGoalPer2Chukka1 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer2Chukka1 = int(round((penaltyOutGoal2Chukka1/penalty2Chukka1)*100))
        
    if penalty2Chukka2==0:
        penaltyOutGoalPer2Chukka2 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer2Chukka2 = int(round((penaltyOutGoal2Chukka2/penalty2Chukka2)*100))
    
    if penalty2Chukka3==0:
        penaltyOutGoalPer2Chukka3 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer2Chukka3 = int(round((penaltyOutGoal2Chukka3/penalty2Chukka3)*100))
    
    if penalty2Chukka4==0:
        penaltyOutGoalPer2Chukka4 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer2Chukka4 = int(round((penaltyOutGoal2Chukka4/penalty2Chukka4)*100))
    
    if penalty2Chukka5==0:
        penaltyOutGoalPer2Chukka5 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer2Chukka5 = int(round((penaltyOutGoal2Chukka5/penalty2Chukka5)*100))
    
    if penalty2Chukka6==0:
        penaltyOutGoalPer2Chukka6 = "Not_Valid_(Zero_Division)"
    else:
        penaltyOutGoalPer2Chukka6 = int(round((penaltyOutGoal2Chukka6/penalty2Chukka6)*100))

    return (penalty1Chukka1,penalty1Chukka2,penalty1Chukka3,
            penalty1Chukka4,penalty1Chukka5,penalty1Chukka6,
            penalty2Chukka1,penalty2Chukka2,penalty2Chukka3,
            penalty2Chukka4,penalty2Chukka5,penalty2Chukka6,
            penaltyOutGoal1Chukka1,penaltyOutGoal1Chukka2,
            penaltyOutGoal1Chukka3,penaltyOutGoal1Chukka4,
            penaltyOutGoal1Chukka5,penaltyOutGoal1Chukka6,
            penaltyOutGoal2Chukka1,penaltyOutGoal2Chukka2,
            penaltyOutGoal2Chukka3,penaltyOutGoal2Chukka4,
            penaltyOutGoal2Chukka5,penaltyOutGoal2Chukka6,
            penaltyOutGoalPer1Chukka1,penaltyOutGoalPer1Chukka2,
            penaltyOutGoalPer1Chukka3,penaltyOutGoalPer1Chukka4,
            penaltyOutGoalPer1Chukka5,penaltyOutGoalPer1Chukka6,
            penaltyOutGoalPer2Chukka1,penaltyOutGoalPer2Chukka2,
            penaltyOutGoalPer2Chukka3,penaltyOutGoalPer2Chukka4,
            penaltyOutGoalPer2Chukka5,penaltyOutGoalPer2Chukka6,
            )

def foulChukka(data1, data2):
    data1_foul = data1[data1["Foul"]=="Foul"]
    foul1Chukka1 = len(data1_foul[data1_foul["Chukka"]=="Chukka 1"])
    foul1Chukka2 = len(data1_foul[data1_foul["Chukka"]=="Chukka 2"])
    foul1Chukka3 = len(data1_foul[data1_foul["Chukka"]=="Chukka 3"])
    foul1Chukka4 = len(data1_foul[data1_foul["Chukka"]=="Chukka 4"])
    foul1Chukka5 = len(data1_foul[data1_foul["Chukka"]=="Chukka 5"])
    foul1Chukka6 = len(data1_foul[data1_foul["Chukka"]=="Chukka 6"])
    
    data2_foul = data2[data2["Foul"]=="Foul"]
    foul2Chukka1 = len(data2_foul[data2_foul["Chukka"]=="Chukka 1"])
    foul2Chukka2 = len(data2_foul[data2_foul["Chukka"]=="Chukka 2"])
    foul2Chukka3 = len(data2_foul[data2_foul["Chukka"]=="Chukka 3"])
    foul2Chukka4 = len(data2_foul[data2_foul["Chukka"]=="Chukka 4"])
    foul2Chukka5 = len(data2_foul[data2_foul["Chukka"]=="Chukka 5"])
    foul2Chukka6 = len(data2_foul[data2_foul["Chukka"]=="Chukka 6"])

    return (foul1Chukka1,foul1Chukka2,foul1Chukka3,
            foul1Chukka4,foul1Chukka5,foul1Chukka6,
            foul2Chukka1,foul2Chukka2,foul2Chukka3,
            foul2Chukka4,foul2Chukka5,foul2Chukka6,
            )

def topPlayersChukka(data1, data2):
    chukka1_1 = data1[data1["Chukka"]=="Chukka 1"]
    chukka2_1 = data1[data1["Chukka"]=="Chukka 2"]
    chukka3_1 = data1[data1["Chukka"]=="Chukka 3"]
    chukka4_1 = data1[data1["Chukka"]=="Chukka 4"]
    chukka5_1 = data1[data1["Chukka"]=="Chukka 5"]
    chukka6_1 = data1[data1["Chukka"]=="Chukka 6"]
    
    chukka1_2 = data2[data2["Chukka"]=="Chukka 1"]
    chukka2_2 = data2[data2["Chukka"]=="Chukka 2"]
    chukka3_2 = data2[data2["Chukka"]=="Chukka 3"]
    chukka4_2 = data2[data2["Chukka"]=="Chukka 4"]
    chukka5_2 = data2[data2["Chukka"]=="Chukka 5"]
    chukka6_2 = data2[data2["Chukka"]=="Chukka 6"]
    
    chukka1_1_a = chukka1_1.loc[chukka1_1["Goal"].dropna().index]
    chukka2_1_a = chukka2_1.loc[chukka2_1["Goal"].dropna().index]
    chukka3_1_a = chukka3_1.loc[chukka3_1["Goal"].dropna().index]
    chukka4_1_a = chukka4_1.loc[chukka4_1["Goal"].dropna().index]
    chukka5_1_a = chukka5_1.loc[chukka5_1["Goal"].dropna().index]
    chukka6_1_a = chukka6_1.loc[chukka6_1["Goal"].dropna().index]
    
    chukka1_2_a = chukka1_2.loc[chukka1_2["Goal"].dropna().index]
    chukka2_2_a = chukka2_2.loc[chukka2_2["Goal"].dropna().index]
    chukka3_2_a = chukka3_2.loc[chukka3_2["Goal"].dropna().index]
    chukka4_2_a = chukka4_2.loc[chukka4_2["Goal"].dropna().index]
    chukka5_2_a = chukka5_2.loc[chukka5_2["Goal"].dropna().index]
    chukka6_2_a = chukka6_2.loc[chukka6_2["Goal"].dropna().index]
    
    dictionary1_1 = OrderedDict(chukka1_1_a.groupby(["Player"]).count()["Name"])
    dictionary2_1 = OrderedDict(chukka2_1_a.groupby(["Player"]).count()["Name"])
    dictionary3_1 = OrderedDict(chukka3_1_a.groupby(["Player"]).count()["Name"])
    dictionary4_1 = OrderedDict(chukka4_1_a.groupby(["Player"]).count()["Name"])
    dictionary5_1 = OrderedDict(chukka5_1_a.groupby(["Player"]).count()["Name"])
    dictionary6_1 = OrderedDict(chukka6_1_a.groupby(["Player"]).count()["Name"])
    
    dictionary1_2 = OrderedDict(chukka1_2_a.groupby(["Player"]).count()["Name"])
    dictionary2_2 = OrderedDict(chukka2_2_a.groupby(["Player"]).count()["Name"])
    dictionary3_2 = OrderedDict(chukka3_2_a.groupby(["Player"]).count()["Name"])
    dictionary4_2 = OrderedDict(chukka4_2_a.groupby(["Player"]).count()["Name"])
    dictionary5_2 = OrderedDict(chukka5_2_a.groupby(["Player"]).count()["Name"])
    dictionary6_2 = OrderedDict(chukka6_2_a.groupby(["Player"]).count()["Name"])
    
    if len(dictionary1_1)>0:
        topPlayerGoals1Chukka1 = next(iter(dictionary1_1.values()))
    else:
        topPlayerGoals1Chukka1 = None
    
    if len(dictionary2_1)>0:
        topPlayerGoals1Chukka2 = next(iter(dictionary2_1.values()))
    else:
        topPlayerGoals1Chukka2 = None
    
    if len(dictionary3_1)>0:
        topPlayerGoals1Chukka3 = next(iter(dictionary3_1.values()))
    else:
        topPlayerGoals1Chukka3 = None
    
    if len(dictionary4_1)>0:
        topPlayerGoals1Chukka4 = next(iter(dictionary4_1.values()))
    else:
        topPlayerGoals1Chukka4 = None
    
    if len(dictionary5_1)>0:
        topPlayerGoals1Chukka5 = next(iter(dictionary5_1.values()))
    else:
        topPlayerGoals1Chukka5 = None
    
    if len(dictionary6_1)>0:
        topPlayerGoals1Chukka6 = next(iter(dictionary6_1.values()))
    else:
        topPlayerGoals1Chukka6 = None
        
    #######################
    
    if len(dictionary1_2)>0:
        topPlayerGoals2Chukka1 = next(iter(dictionary1_2.values()))
    else:
        topPlayerGoals2Chukka1 = None
    
    if len(dictionary2_2)>0:
        topPlayerGoals2Chukka2 = next(iter(dictionary2_2.values()))
    else:
        topPlayerGoals2Chukka2 = None
    
    if len(dictionary3_2)>0:
        topPlayerGoals2Chukka3 = next(iter(dictionary3_2.values()))
    else:
        topPlayerGoals2Chukka3 = None
    
    if len(dictionary4_2)>0:
        topPlayerGoals2Chukka4 = next(iter(dictionary4_2.values()))
    else:
        topPlayerGoals2Chukka4 = None
    
    if len(dictionary5_2)>0:
        topPlayerGoals2Chukka5 = next(iter(dictionary5_2.values()))
    else:
        topPlayerGoals2Chukka5 = None
    
    if len(dictionary6_2)>0:
        topPlayerGoals2Chukka6 = next(iter(dictionary6_2.values()))
    else:
        topPlayerGoals2Chukka6 = None
    
    topPlayers1Chukka1 = [ key for key, value in dictionary1_1.items() if value == topPlayerGoals1Chukka1 ]
    topPlayers1Chukka2 = [ key for key, value in dictionary2_1.items() if value == topPlayerGoals1Chukka2 ]
    topPlayers1Chukka3 = [ key for key, value in dictionary3_1.items() if value == topPlayerGoals1Chukka3 ]
    topPlayers1Chukka4 = [ key for key, value in dictionary4_1.items() if value == topPlayerGoals1Chukka4 ]
    topPlayers1Chukka5 = [ key for key, value in dictionary5_1.items() if value == topPlayerGoals1Chukka5 ]
    topPlayers1Chukka6 = [ key for key, value in dictionary6_1.items() if value == topPlayerGoals1Chukka6 ]
    
    topPlayers2Chukka1 = [ key for key, value in dictionary1_2.items() if value == topPlayerGoals2Chukka1 ]
    topPlayers2Chukka2 = [ key for key, value in dictionary2_2.items() if value == topPlayerGoals2Chukka2 ]
    topPlayers2Chukka3 = [ key for key, value in dictionary3_2.items() if value == topPlayerGoals2Chukka3 ]
    topPlayers2Chukka4 = [ key for key, value in dictionary4_2.items() if value == topPlayerGoals2Chukka4 ]
    topPlayers2Chukka5 = [ key for key, value in dictionary5_2.items() if value == topPlayerGoals2Chukka5 ]
    topPlayers2Chukka6 = [ key for key, value in dictionary6_2.items() if value == topPlayerGoals2Chukka6 ]
    
    totalTopPlayers1Chukka1 = len(topPlayers1Chukka1)
    totalTopPlayers1Chukka2 = len(topPlayers1Chukka2)
    totalTopPlayers1Chukka3 = len(topPlayers1Chukka3)
    totalTopPlayers1Chukka4 = len(topPlayers1Chukka4)
    totalTopPlayers1Chukka5 = len(topPlayers1Chukka5)
    totalTopPlayers1Chukka6 = len(topPlayers1Chukka6)
    
    totalTopPlayers2Chukka1 = len(topPlayers2Chukka1)
    totalTopPlayers2Chukka2 = len(topPlayers2Chukka2)
    totalTopPlayers2Chukka3 = len(topPlayers2Chukka3)
    totalTopPlayers2Chukka4 = len(topPlayers2Chukka4)
    totalTopPlayers2Chukka5 = len(topPlayers2Chukka5)
    totalTopPlayers2Chukka6 = len(topPlayers2Chukka6)
    
    return (topPlayerGoals1Chukka1,topPlayerGoals1Chukka2,
            topPlayerGoals1Chukka3,topPlayerGoals1Chukka4,
            topPlayerGoals1Chukka5,topPlayerGoals1Chukka6,
            topPlayerGoals2Chukka1,topPlayerGoals2Chukka2,
            topPlayerGoals2Chukka3,topPlayerGoals2Chukka4,
            topPlayerGoals2Chukka5,topPlayerGoals2Chukka6,
            topPlayers1Chukka1,topPlayers1Chukka2,topPlayers1Chukka3,
            topPlayers1Chukka4,topPlayers1Chukka5,topPlayers1Chukka6,
            topPlayers2Chukka1,topPlayers2Chukka2,topPlayers2Chukka3,
            topPlayers2Chukka4,topPlayers2Chukka5,topPlayers2Chukka6,
            totalTopPlayers1Chukka1,totalTopPlayers1Chukka2,
            totalTopPlayers1Chukka3,totalTopPlayers1Chukka4,
            totalTopPlayers1Chukka5,totalTopPlayers1Chukka6,
            totalTopPlayers2Chukka1,totalTopPlayers2Chukka2,
            totalTopPlayers2Chukka3,totalTopPlayers2Chukka4,
            totalTopPlayers2Chukka5,totalTopPlayers2Chukka6
            )

def topAssistsChukka(data1, data2):
    chukka1_1 = data1[data1["Chukka"]=="Chukka 1"]
    chukka2_1 = data1[data1["Chukka"]=="Chukka 2"]
    chukka3_1 = data1[data1["Chukka"]=="Chukka 3"]
    chukka4_1 = data1[data1["Chukka"]=="Chukka 4"]
    chukka5_1 = data1[data1["Chukka"]=="Chukka 5"]
    chukka6_1 = data1[data1["Chukka"]=="Chukka 6"]
    
    chukka1_2 = data2[data2["Chukka"]=="Chukka 1"]
    chukka2_2 = data2[data2["Chukka"]=="Chukka 2"]
    chukka3_2 = data2[data2["Chukka"]=="Chukka 3"]
    chukka4_2 = data2[data2["Chukka"]=="Chukka 4"]
    chukka5_2 = data2[data2["Chukka"]=="Chukka 5"]
    chukka6_2 = data2[data2["Chukka"]=="Chukka 6"]
    
    chukka1_1_a = chukka1_1[chukka1_1["Assist Outcome"]=="Successful"]
    chukka2_1_a = chukka2_1[chukka2_1["Assist Outcome"]=="Successful"]
    chukka3_1_a = chukka3_1[chukka3_1["Assist Outcome"]=="Successful"]
    chukka4_1_a = chukka4_1[chukka4_1["Assist Outcome"]=="Successful"]
    chukka5_1_a = chukka5_1[chukka5_1["Assist Outcome"]=="Successful"]
    chukka6_1_a = chukka6_1[chukka6_1["Assist Outcome"]=="Successful"]
    
    chukka1_2_a = chukka1_2[chukka1_2["Assist Outcome"]=="Successful"]
    chukka2_2_a = chukka2_2[chukka2_2["Assist Outcome"]=="Successful"]
    chukka3_2_a = chukka3_2[chukka3_2["Assist Outcome"]=="Successful"]
    chukka4_2_a = chukka4_2[chukka4_2["Assist Outcome"]=="Successful"]
    chukka5_2_a = chukka5_2[chukka5_2["Assist Outcome"]=="Successful"]
    chukka6_2_a = chukka6_2[chukka6_2["Assist Outcome"]=="Successful"]
    
    dictionary1_1 = OrderedDict(chukka1_1_a["Assist"].value_counts())
    dictionary2_1 = OrderedDict(chukka2_1_a["Assist"].value_counts())
    dictionary3_1 = OrderedDict(chukka3_1_a["Assist"].value_counts())
    dictionary4_1 = OrderedDict(chukka4_1_a["Assist"].value_counts())
    dictionary5_1 = OrderedDict(chukka5_1_a["Assist"].value_counts())
    dictionary6_1 = OrderedDict(chukka6_1_a["Assist"].value_counts())
    
    dictionary1_2 = OrderedDict(chukka1_2_a["Assist"].value_counts())
    dictionary2_2 = OrderedDict(chukka2_2_a["Assist"].value_counts())
    dictionary3_2 = OrderedDict(chukka3_2_a["Assist"].value_counts())
    dictionary4_2 = OrderedDict(chukka4_2_a["Assist"].value_counts())
    dictionary5_2 = OrderedDict(chukka5_2_a["Assist"].value_counts())
    dictionary6_2 = OrderedDict(chukka6_2_a["Assist"].value_counts())
    
    if len(dictionary1_1)>0:
        topAssistGoals1Chukka1 = next(iter(dictionary1_1.values()))
    else:
        topAssistGoals1Chukka1 = None
    
    if len(dictionary2_1)>0:
        topAssistGoals1Chukka2 = next(iter(dictionary2_1.values()))
    else:
        topAssistGoals1Chukka2 = None
    
    if len(dictionary3_1)>0:
        topAssistGoals1Chukka3 = next(iter(dictionary3_1.values()))
    else:
        topAssistGoals1Chukka3 = None
    
    if len(dictionary4_1)>0:
        topAssistGoals1Chukka4 = next(iter(dictionary4_1.values()))
    else:
        topAssistGoals1Chukka4 = None
    
    if len(dictionary5_1)>0:
        topAssistGoals1Chukka5 = next(iter(dictionary5_1.values()))
    else:
        topAssistGoals1Chukka5 = None
    
    if len(dictionary6_1)>0:
        topAssistGoals1Chukka6 = next(iter(dictionary6_1.values()))
    else:
        topAssistGoals1Chukka6 = None
        
    #############
    
    if len(dictionary1_2)>0:
        topAssistGoals2Chukka1 = next(iter(dictionary1_2.values()))
    else:
        topAssistGoals2Chukka1 = None
    
    if len(dictionary2_2)>0:
        topAssistGoals2Chukka2 = next(iter(dictionary2_2.values()))
    else:
        topAssistGoals2Chukka2 = None
    
    if len(dictionary3_2)>0:
        topAssistGoals2Chukka3 = next(iter(dictionary3_2.values()))
    else:
        topAssistGoals2Chukka3 = None
    
    if len(dictionary4_2)>0:
        topAssistGoals2Chukka4 = next(iter(dictionary4_2.values()))
    else:
        topAssistGoals2Chukka4 = None
    
    if len(dictionary5_2)>0:
        topAssistGoals2Chukka5 = next(iter(dictionary5_2.values()))
    else:
        topAssistGoals2Chukka5 = None
    
    if len(dictionary6_2)>0:
        topAssistGoals2Chukka6 = next(iter(dictionary6_2.values()))
    else:
        topAssistGoals2Chukka6 = None
        
    topAssists1Chukka1 = [ key for key, value in dictionary1_1.items() if value == topAssistGoals1Chukka1 ]
    topAssists1Chukka2 = [ key for key, value in dictionary2_1.items() if value == topAssistGoals1Chukka2 ]
    topAssists1Chukka3 = [ key for key, value in dictionary3_1.items() if value == topAssistGoals1Chukka3 ]
    topAssists1Chukka4 = [ key for key, value in dictionary4_1.items() if value == topAssistGoals1Chukka4 ]
    topAssists1Chukka5 = [ key for key, value in dictionary5_1.items() if value == topAssistGoals1Chukka5 ]
    topAssists1Chukka6 = [ key for key, value in dictionary6_1.items() if value == topAssistGoals1Chukka6 ]
    
    topAssists2Chukka1 = [ key for key, value in dictionary1_2.items() if value == topAssistGoals2Chukka1 ]
    topAssists2Chukka2 = [ key for key, value in dictionary2_2.items() if value == topAssistGoals2Chukka2 ]
    topAssists2Chukka3 = [ key for key, value in dictionary3_2.items() if value == topAssistGoals2Chukka3 ]
    topAssists2Chukka4 = [ key for key, value in dictionary4_2.items() if value == topAssistGoals2Chukka4 ]
    topAssists2Chukka5 = [ key for key, value in dictionary5_2.items() if value == topAssistGoals2Chukka5 ]
    topAssists2Chukka6 = [ key for key, value in dictionary6_2.items() if value == topAssistGoals2Chukka6 ]
    
    totalTopAssists1Chukka1 = len(topAssists1Chukka1)
    totalTopAssists1Chukka2 = len(topAssists1Chukka2)
    totalTopAssists1Chukka3 = len(topAssists1Chukka3)
    totalTopAssists1Chukka4 = len(topAssists1Chukka4)
    totalTopAssists1Chukka5 = len(topAssists1Chukka5)
    totalTopAssists1Chukka6 = len(topAssists1Chukka6)
    
    totalTopAssists2Chukka1 = len(topAssists2Chukka1)
    totalTopAssists2Chukka2 = len(topAssists2Chukka2)
    totalTopAssists2Chukka3 = len(topAssists2Chukka3)
    totalTopAssists2Chukka4 = len(topAssists2Chukka4)
    totalTopAssists2Chukka5 = len(topAssists2Chukka5)
    totalTopAssists2Chukka6 = len(topAssists2Chukka6)
    
    return (topAssistGoals1Chukka1,topAssistGoals1Chukka2,
            topAssistGoals1Chukka3,topAssistGoals1Chukka4,
            topAssistGoals1Chukka5,topAssistGoals1Chukka6,
            topAssistGoals2Chukka1,topAssistGoals2Chukka2,
            topAssistGoals2Chukka3,topAssistGoals2Chukka4,
            topAssistGoals2Chukka5,topAssistGoals2Chukka6,
            topAssists1Chukka1,topAssists1Chukka2,
            topAssists1Chukka3,topAssists1Chukka4,
            topAssists1Chukka5,topAssists1Chukka6,
            topAssists2Chukka1,topAssists2Chukka2,
            topAssists2Chukka3,topAssists2Chukka4,
            topAssists2Chukka5,topAssists2Chukka6,
            totalTopAssists1Chukka1,totalTopAssists1Chukka2,
            totalTopAssists1Chukka3,totalTopAssists1Chukka4,
            totalTopAssists1Chukka5,totalTopAssists1Chukka6,
            totalTopAssists2Chukka1,totalTopAssists2Chukka2,
            totalTopAssists2Chukka3,totalTopAssists2Chukka4,
            totalTopAssists2Chukka5,totalTopAssists2Chukka6,
            )

def topPlayerAssistsChukka(topPlayers1Chukka1,topAssists1Chukka1,
                           topPlayers1Chukka2,topAssists1Chukka2,
                           topPlayers1Chukka3,topAssists1Chukka3,
                           topPlayers1Chukka4,topAssists1Chukka4,
                           topPlayers1Chukka5,topAssists1Chukka5,
                           topPlayers1Chukka6,topAssists1Chukka6,
                           topPlayers2Chukka1,topAssists2Chukka1,
                           topPlayers2Chukka2,topAssists2Chukka2,
                           topPlayers2Chukka3,topAssists2Chukka3,
                           topPlayers2Chukka4,topAssists2Chukka4,
                           topPlayers2Chukka5,topAssists2Chukka5,
                           topPlayers2Chukka6,topAssists2Chukka6,
                           ):
    
    bothTopPlayerAssist1_1 = list(set(topPlayers1Chukka1).intersection(topAssists1Chukka1))
    bothTopPlayerAssist1_2 = list(set(topPlayers1Chukka2).intersection(topAssists1Chukka2))
    bothTopPlayerAssist1_3 = list(set(topPlayers1Chukka3).intersection(topAssists1Chukka3))
    bothTopPlayerAssist1_4 = list(set(topPlayers1Chukka4).intersection(topAssists1Chukka4))
    bothTopPlayerAssist1_5 = list(set(topPlayers1Chukka5).intersection(topAssists1Chukka5))
    bothTopPlayerAssist1_6 = list(set(topPlayers1Chukka6).intersection(topAssists1Chukka6))
    
    bothTopPlayerAssist2_1 = list(set(topPlayers2Chukka1).intersection(topAssists2Chukka1))
    bothTopPlayerAssist2_2 = list(set(topPlayers2Chukka2).intersection(topAssists2Chukka2))
    bothTopPlayerAssist2_3 = list(set(topPlayers2Chukka3).intersection(topAssists2Chukka3))
    bothTopPlayerAssist2_4 = list(set(topPlayers2Chukka4).intersection(topAssists2Chukka4))
    bothTopPlayerAssist2_5 = list(set(topPlayers2Chukka5).intersection(topAssists2Chukka5))
    bothTopPlayerAssist2_6 = list(set(topPlayers2Chukka6).intersection(topAssists2Chukka6))
    
    return (bothTopPlayerAssist1_1,bothTopPlayerAssist1_2,
            bothTopPlayerAssist1_3,bothTopPlayerAssist1_4,
            bothTopPlayerAssist1_5,bothTopPlayerAssist1_6,
            bothTopPlayerAssist2_1,bothTopPlayerAssist2_2,
            bothTopPlayerAssist2_3,bothTopPlayerAssist2_4,
            bothTopPlayerAssist2_5,bothTopPlayerAssist2_6,
            )

