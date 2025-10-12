import pandas as pd

from utils.Extract_Data_Script import basicGameInfo, separateTeamsData, shotAtGoalInfo, \
    penaltyInfo, topPlayersInfo, topAssistsInfo, \
    topPlayerAssist, goalsChukka, shotAtGoalChukka, \
    penaltyChukka, foulChukka, topPlayersChukka, \
    topAssistsChukka, topPlayerAssistsChukka

def single_file(finalLst, path):
    dataframe_columns = ["stage", "year", "tournament", "club", "date", "total_chukkas",
                         "team1", "team2", "goals1", "goals2", "goal_diff", "fouls1", "fouls2",
                         "shotAtGoal1", "shotAtGoal2", "shotAtGoal_diff",
                         "shotAtGoalOutcomeGoal1", "shotAtGoalOutcomeGoal2",
                         "shotAtGoalOutcomeGoal_diff", "shotAtGoalOutcomeGoalPercent1",
                         "shotAtGoalOutcomeGoalPercent2",
                         "shotAtGoalOutcomeGoalPercent_diff",
                         "penaltyShots1", "penaltyShots2", "penaltyShotsGoal1",
                         "penaltyShotsGoal2", "penaltyShotsGoalPercent1",
                         "penaltyShotsGoalPercent2", "topPlayerGoals1",
                         "topPlayerGoals2", "topPlayers1", "topPlayers2",
                         "totalTopPlayers1", "totalTopPlayers2",
                         "topAssistGoals1", "topAssistGoals2",
                         "topAssists1", "topAssists2",
                         "totalTopAssists1", "totalTopAssists2",
                         "bothTopPlayerAssist1", "bothTopPlayerAssist2",
                         "goals1Chukka1", "goals1Chukka2", "goals1Chukka3",
                         "goals1Chukka4", "goals1Chukka5", "goals1Chukka6",
                         "goals2Chukka1", "goals2Chukka2", "goals2Chukka3",
                         "goals2Chukka4", "goals2Chukka5", "goals2Chukka6",
                         "goalsChukka1_diff", "goalsChukka2_diff",
                         "goalsChukka3_diff", "goalsChukka4_diff",
                         "goalsChukka5_diff", "goalsChukka6_diff",
                         "shotAtGoal1Chukka1", "shotAtGoal1Chukka2", "shotAtGoal1Chukka3",
                         "shotAtGoal1Chukka4", "shotAtGoal1Chukka5", "shotAtGoal1Chukka6",
                         "shotAtGoal2Chukka1", "shotAtGoal2Chukka2", "shotAtGoal2Chukka3",
                         "shotAtGoal2Chukka4", "shotAtGoal2Chukka5", "shotAtGoal2Chukka6",
                         "shotAtGoalChukka1_diff", "shotAtGoalChukka2_diff",
                         "shotAtGoalChukka3_diff", "shotAtGoalChukka4_diff",
                         "shotAtGoalChukka5_diff", "shotAtGoalChukka6_diff",
                         "shotAtGoalOutGoal1Chukka1", "shotAtGoalOutGoal1Chukka2",
                         "shotAtGoalOutGoal1Chukka3", "shotAtGoalOutGoal1Chukka4",
                         "shotAtGoalOutGoal1Chukka5", "shotAtGoalOutGoal1Chukka6",
                         "shotAtGoalOutGoal2Chukka1", "shotAtGoalOutGoal2Chukka2",
                         "shotAtGoalOutGoal2Chukka3", "shotAtGoalOutGoal2Chukka4",
                         "shotAtGoalOutGoal2Chukka5", "shotAtGoalOutGoal2Chukka6",
                         "shotAtGoalOutGoalChukka1_diff", "shotAtGoalOutGoalChukka2_diff",
                         "shotAtGoalOutGoalChukka3_diff", "shotAtGoalOutGoalChukka4_diff",
                         "shotAtGoalOutGoalChukka5_diff", "shotAtGoalOutGoalChukka6_diff",
                         "shotAtGoalOutGoalPer1Chukka1", "shotAtGoalOutGoalPer1Chukka2",
                         "shotAtGoalOutGoalPer1Chukka3", "shotAtGoalOutGoalPer1Chukka4",
                         "shotAtGoalOutGoalPer1Chukka5", "shotAtGoalOutGoalPer1Chukka6",
                         "shotAtGoalOutGoalPer2Chukka1", "shotAtGoalOutGoalPer2Chukka2",
                         "shotAtGoalOutGoalPer2Chukka3", "shotAtGoalOutGoalPer2Chukka4",
                         "shotAtGoalOutGoalPer2Chukka5", "shotAtGoalOutGoalPer2Chukka6",
                         "shotAtGoalsFirstHalf1", "shotAtGoalsFirstHalf2",
                         "shotAtGoalsSecondHalf1", "shotAtGoalsSecondHalf2",
                         "shotAtGoalsFirstHalf_diff", "shotAtGoalsSecondHalf_diff",
                         "shotAtGoalsOutGoalsFirstHalf1", "shotAtGoalsOutGoalsFirstHalf2",
                         "shotAtGoalsOutGoalsSecondHalf1", "shotAtGoalsOutGoalsSecondHalf2",
                         "shotAtGoalsOutGoalsFirstHalf_diff", "shotAtGoalsOutGoalsSecondHalf_diff",
                         "shotAtGoalOutGoalPer1FHalf", "shotAtGoalOutGoalPer2FHalf",
                         "shotAtGoalOutGoalPer1SHalf", "shotAtGoalOutGoalPer2SHalf",
                         "penalty1Chukka1", "penalty1Chukka2", "penalty1Chukka3",
                         "penalty1Chukka4", "penalty1Chukka5", "penalty1Chukka6",
                         "penalty2Chukka1", "penalty2Chukka2", "penalty2Chukka3",
                         "penalty2Chukka4", "penalty2Chukka5", "penalty2Chukka6",
                         "penaltyOutGoal1Chukka1", "penaltyOutGoal1Chukka2",
                         "penaltyOutGoal1Chukka3", "penaltyOutGoal1Chukka4",
                         "penaltyOutGoal1Chukka5", "penaltyOutGoal1Chukka6",
                         "penaltyOutGoal2Chukka1", "penaltyOutGoal2Chukka2",
                         "penaltyOutGoal2Chukka3", "penaltyOutGoal2Chukka4",
                         "penaltyOutGoal2Chukka5", "penaltyOutGoal2Chukka6",
                         "penaltyOutGoalPer1Chukka1", "penaltyOutGoalPer1Chukka2",
                         "penaltyOutGoalPer1Chukka3", "penaltyOutGoalPer1Chukka4",
                         "penaltyOutGoalPer1Chukka5", "penaltyOutGoalPer1Chukka6",
                         "penaltyOutGoalPer2Chukka1", "penaltyOutGoalPer2Chukka2",
                         "penaltyOutGoalPer2Chukka3", "penaltyOutGoalPer2Chukka4",
                         "penaltyOutGoalPer2Chukka5", "penaltyOutGoalPer2Chukka6",
                         "foul1Chukka1", "foul1Chukka2", "foul1Chukka3",
                         "foul1Chukka4", "foul1Chukka5", "foul1Chukka6",
                         "foul2Chukka1", "foul2Chukka2", "foul2Chukka3",
                         "foul2Chukka4", "foul2Chukka5", "foul2Chukka6",
                         "topPlayerGoals1Chukka1", "topPlayerGoals1Chukka2",
                         "topPlayerGoals1Chukka3", "topPlayerGoals1Chukka4",
                         "topPlayerGoals1Chukka5", "topPlayerGoals1Chukka6",
                         "topPlayerGoals2Chukka1", "topPlayerGoals2Chukka2",
                         "topPlayerGoals2Chukka3", "topPlayerGoals2Chukka4",
                         "topPlayerGoals2Chukka5", "topPlayerGoals2Chukka6",
                         "topPlayers1Chukka1", "topPlayers1Chukka2", "topPlayers1Chukka3",
                         "topPlayers1Chukka4", "topPlayers1Chukka5", "topPlayers1Chukka6",
                         "topPlayers2Chukka1", "topPlayers2Chukka2", "topPlayers2Chukka3",
                         "topPlayers2Chukka4", "topPlayers2Chukka5", "topPlayers2Chukka6",
                         "totalTopPlayers1Chukka1", "totalTopPlayers1Chukka2",
                         "totalTopPlayers1Chukka3", "totalTopPlayers1Chukka4",
                         "totalTopPlayers1Chukka5", "totalTopPlayers1Chukka6",
                         "totalTopPlayers2Chukka1", "totalTopPlayers2Chukka2",
                         "totalTopPlayers2Chukka3", "totalTopPlayers2Chukka4",
                         "totalTopPlayers2Chukka5", "totalTopPlayers2Chukka6",
                         "topAssistGoals1Chukka1", "topAssistGoals1Chukka2",
                         "topAssistGoals1Chukka3", "topAssistGoals1Chukka4",
                         "topAssistGoals1Chukka5", "topAssistGoals1Chukka6",
                         "topAssistGoals2Chukka1", "topAssistGoals2Chukka2",
                         "topAssistGoals2Chukka3", "topAssistGoals2Chukka4",
                         "topAssistGoals2Chukka5", "topAssistGoals2Chukka6",
                         "topAssists1Chukka1", "topAssists1Chukka2",
                         "topAssists1Chukka3", "topAssists1Chukka4",
                         "topAssists1Chukka5", "topAssists1Chukka6",
                         "topAssists2Chukka1", "topAssists2Chukka2",
                         "topAssists2Chukka3", "topAssists2Chukka4",
                         "topAssists2Chukka5", "topAssists2Chukka6",
                         "totalTopAssists1Chukka1", "totalTopAssists1Chukka2",
                         "totalTopAssists1Chukka3", "totalTopAssists1Chukka4",
                         "totalTopAssists1Chukka5", "totalTopAssists1Chukka6",
                         "totalTopAssists2Chukka1", "totalTopAssists2Chukka2",
                         "totalTopAssists2Chukka3", "totalTopAssists2Chukka4",
                         "totalTopAssists2Chukka5", "totalTopAssists2Chukka6",
                         "bothTopPlayerAssist1_1", "bothTopPlayerAssist1_2",
                         "bothTopPlayerAssist1_3", "bothTopPlayerAssist1_4",
                         "bothTopPlayerAssist1_5", "bothTopPlayerAssist1_6",
                         "bothTopPlayerAssist2_1", "bothTopPlayerAssist2_2",
                         "bothTopPlayerAssist2_3", "bothTopPlayerAssist2_4",
                         "bothTopPlayerAssist2_5", "bothTopPlayerAssist2_6"]

    df = pd.DataFrame([finalLst], columns=dataframe_columns)
    lst = path.split('/')
    filename = lst[-1]
    df["filename"] = filename
    return df, filename

def data_Extract(data):
    #   Remove Unimportant Info
    data = data[data["Team"] != "Team"]

    ###################
    stage, year, tournament, club, date, total_chukkas = basicGameInfo(data)

    lst_basicInfo = [stage, year, tournament, club, date, total_chukkas]

    ###################
    team1, team2, data1, data2, \
    goals1, goals2, goal_diff, fouls1, fouls2 = separateTeamsData(data)

    lst_separateTeamsData = [team1, team2, goals1, goals2, goal_diff, fouls1, fouls2]

    ##################
    shotAtGoal1, shotAtGoal2, shotAtGoal_diff, \
    shotAtGoalOutcomeGoal1, shotAtGoalOutcomeGoal2, \
    shotAtGoalOutcomeGoal_diff, shotAtGoalOutcomeGoalPercent1, \
    shotAtGoalOutcomeGoalPercent2, shotAtGoalOutcomeGoalPercent_diff = shotAtGoalInfo(data1, data2)

    lst_shotAtGoalInfo = [shotAtGoal1, shotAtGoal2, shotAtGoal_diff,
                          shotAtGoalOutcomeGoal1, shotAtGoalOutcomeGoal2,
                          shotAtGoalOutcomeGoal_diff,
                          shotAtGoalOutcomeGoalPercent1,
                          shotAtGoalOutcomeGoalPercent2,
                          shotAtGoalOutcomeGoalPercent_diff]

    ##################
    penaltyShots1, penaltyShots2, penaltyShotsGoal1, penaltyShotsGoal2, \
    penaltyShotsGoalPercent1, penaltyShotsGoalPercent2 = penaltyInfo(data1, data2)

    lst_penaltyInfo = [penaltyShots1, penaltyShots2, penaltyShotsGoal1,
                       penaltyShotsGoal2, penaltyShotsGoalPercent1,
                       penaltyShotsGoalPercent2]

    ###################
    topPlayerGoals1, topPlayerGoals2, \
    topPlayers1, topPlayers2, \
    totalTopPlayers1, totalTopPlayers2 = topPlayersInfo(data1, data2)

    lst_topPlayersInfo = [topPlayerGoals1, topPlayerGoals2,
                          topPlayers1, topPlayers2, totalTopPlayers1,
                          totalTopPlayers2]

    ###################
    topAssistGoals1, topAssistGoals2, \
    topAssists1, topAssists2, \
    totalTopAssists1, totalTopAssists2 = topAssistsInfo(data1, data2)

    lst_topAssistsInfo = [topAssistGoals1, topAssistGoals2,
                          topAssists1, topAssists2,
                          totalTopAssists1, totalTopAssists2]

    ###################

    bothTopPlayerAssist1, bothTopPlayerAssist2 = topPlayerAssist(topPlayers1, topPlayers2,
                                                                 topAssists1, topAssists2)

    lst_topPlayerAssist = [bothTopPlayerAssist1, bothTopPlayerAssist2]

    ##################

    goals1Chukka1, goals1Chukka2, goals1Chukka3, \
    goals1Chukka4, goals1Chukka5, goals1Chukka6, \
    goals2Chukka1, goals2Chukka2, goals2Chukka3, \
    goals2Chukka4, goals2Chukka5, goals2Chukka6, \
    goalsChukka1_diff, goalsChukka2_diff, \
    goalsChukka3_diff, goalsChukka4_diff, \
    goalsChukka5_diff, goalsChukka6_diff = goalsChukka(data1, data2)

    lst_goalsChukka = [goals1Chukka1, goals1Chukka2, goals1Chukka3,
                       goals1Chukka4, goals1Chukka5, goals1Chukka6,
                       goals2Chukka1, goals2Chukka2, goals2Chukka3,
                       goals2Chukka4, goals2Chukka5, goals2Chukka6,
                       goalsChukka1_diff, goalsChukka2_diff,
                       goalsChukka3_diff, goalsChukka4_diff,
                       goalsChukka5_diff, goalsChukka6_diff]

    ###################

    shotAtGoal1Chukka1, shotAtGoal1Chukka2, shotAtGoal1Chukka3, \
    shotAtGoal1Chukka4, shotAtGoal1Chukka5, shotAtGoal1Chukka6, \
    shotAtGoal2Chukka1, shotAtGoal2Chukka2, shotAtGoal2Chukka3, \
    shotAtGoal2Chukka4, shotAtGoal2Chukka5, shotAtGoal2Chukka6, \
    shotAtGoalChukka1_diff, shotAtGoalChukka2_diff, \
    shotAtGoalChukka3_diff, shotAtGoalChukka4_diff, \
    shotAtGoalChukka5_diff, shotAtGoalChukka6_diff, \
    shotAtGoalOutGoal1Chukka1, shotAtGoalOutGoal1Chukka2, \
    shotAtGoalOutGoal1Chukka3, shotAtGoalOutGoal1Chukka4, \
    shotAtGoalOutGoal1Chukka5, shotAtGoalOutGoal1Chukka6, \
    shotAtGoalOutGoal2Chukka1, shotAtGoalOutGoal2Chukka2, \
    shotAtGoalOutGoal2Chukka3, shotAtGoalOutGoal2Chukka4, \
    shotAtGoalOutGoal2Chukka5, shotAtGoalOutGoal2Chukka6, \
    shotAtGoalOutGoalChukka1_diff, shotAtGoalOutGoalChukka2_diff, \
    shotAtGoalOutGoalChukka3_diff, shotAtGoalOutGoalChukka4_diff, \
    shotAtGoalOutGoalChukka5_diff, shotAtGoalOutGoalChukka6_diff, \
    shotAtGoalOutGoalPer1Chukka1, shotAtGoalOutGoalPer1Chukka2, \
    shotAtGoalOutGoalPer1Chukka3, shotAtGoalOutGoalPer1Chukka4, \
    shotAtGoalOutGoalPer1Chukka5, shotAtGoalOutGoalPer1Chukka6, \
    shotAtGoalOutGoalPer2Chukka1, shotAtGoalOutGoalPer2Chukka2, \
    shotAtGoalOutGoalPer2Chukka3, shotAtGoalOutGoalPer2Chukka4, \
    shotAtGoalOutGoalPer2Chukka5, shotAtGoalOutGoalPer2Chukka6, \
    shotAtGoalsFirstHalf1, shotAtGoalsFirstHalf2, \
    shotAtGoalsSecondHalf1, shotAtGoalsSecondHalf2, \
    shotAtGoalsFirstHalf_diff, shotAtGoalsSecondHalf_diff, \
    shotAtGoalsOutGoalsFirstHalf1, shotAtGoalsOutGoalsFirstHalf2, \
    shotAtGoalsOutGoalsSecondHalf1, shotAtGoalsOutGoalsSecondHalf2, \
    shotAtGoalsOutGoalsFirstHalf_diff, shotAtGoalsOutGoalsSecondHalf_diff, \
    shotAtGoalOutGoalPer1FHalf, shotAtGoalOutGoalPer2FHalf, \
    shotAtGoalOutGoalPer1SHalf, shotAtGoalOutGoalPer2SHalf = shotAtGoalChukka(data1, data2)

    lst_shotAtGoalChukka = [shotAtGoal1Chukka1, shotAtGoal1Chukka2, shotAtGoal1Chukka3,
                            shotAtGoal1Chukka4, shotAtGoal1Chukka5, shotAtGoal1Chukka6,
                            shotAtGoal2Chukka1, shotAtGoal2Chukka2, shotAtGoal2Chukka3,
                            shotAtGoal2Chukka4, shotAtGoal2Chukka5, shotAtGoal2Chukka6,
                            shotAtGoalChukka1_diff, shotAtGoalChukka2_diff,
                            shotAtGoalChukka3_diff, shotAtGoalChukka4_diff,
                            shotAtGoalChukka5_diff, shotAtGoalChukka6_diff,
                            shotAtGoalOutGoal1Chukka1, shotAtGoalOutGoal1Chukka2,
                            shotAtGoalOutGoal1Chukka3, shotAtGoalOutGoal1Chukka4,
                            shotAtGoalOutGoal1Chukka5, shotAtGoalOutGoal1Chukka6,
                            shotAtGoalOutGoal2Chukka1, shotAtGoalOutGoal2Chukka2,
                            shotAtGoalOutGoal2Chukka3, shotAtGoalOutGoal2Chukka4,
                            shotAtGoalOutGoal2Chukka5, shotAtGoalOutGoal2Chukka6,
                            shotAtGoalOutGoalChukka1_diff, shotAtGoalOutGoalChukka2_diff,
                            shotAtGoalOutGoalChukka3_diff, shotAtGoalOutGoalChukka4_diff,
                            shotAtGoalOutGoalChukka5_diff, shotAtGoalOutGoalChukka6_diff,
                            shotAtGoalOutGoalPer1Chukka1, shotAtGoalOutGoalPer1Chukka2,
                            shotAtGoalOutGoalPer1Chukka3, shotAtGoalOutGoalPer1Chukka4,
                            shotAtGoalOutGoalPer1Chukka5, shotAtGoalOutGoalPer1Chukka6,
                            shotAtGoalOutGoalPer2Chukka1, shotAtGoalOutGoalPer2Chukka2,
                            shotAtGoalOutGoalPer2Chukka3, shotAtGoalOutGoalPer2Chukka4,
                            shotAtGoalOutGoalPer2Chukka5, shotAtGoalOutGoalPer2Chukka6,
                            shotAtGoalsFirstHalf1, shotAtGoalsFirstHalf2,
                            shotAtGoalsSecondHalf1, shotAtGoalsSecondHalf2,
                            shotAtGoalsFirstHalf_diff, shotAtGoalsSecondHalf_diff,
                            shotAtGoalsOutGoalsFirstHalf1, shotAtGoalsOutGoalsFirstHalf2,
                            shotAtGoalsOutGoalsSecondHalf1, shotAtGoalsOutGoalsSecondHalf2,
                            shotAtGoalsOutGoalsFirstHalf_diff, shotAtGoalsOutGoalsSecondHalf_diff,
                            shotAtGoalOutGoalPer1FHalf, shotAtGoalOutGoalPer2FHalf,
                            shotAtGoalOutGoalPer1SHalf, shotAtGoalOutGoalPer2SHalf]

    ###################

    penalty1Chukka1, penalty1Chukka2, penalty1Chukka3, \
    penalty1Chukka4, penalty1Chukka5, penalty1Chukka6, \
    penalty2Chukka1, penalty2Chukka2, penalty2Chukka3, \
    penalty2Chukka4, penalty2Chukka5, penalty2Chukka6, \
    penaltyOutGoal1Chukka1, penaltyOutGoal1Chukka2, \
    penaltyOutGoal1Chukka3, penaltyOutGoal1Chukka4, \
    penaltyOutGoal1Chukka5, penaltyOutGoal1Chukka6, \
    penaltyOutGoal2Chukka1, penaltyOutGoal2Chukka2, \
    penaltyOutGoal2Chukka3, penaltyOutGoal2Chukka4, \
    penaltyOutGoal2Chukka5, penaltyOutGoal2Chukka6, \
    penaltyOutGoalPer1Chukka1, penaltyOutGoalPer1Chukka2, \
    penaltyOutGoalPer1Chukka3, penaltyOutGoalPer1Chukka4, \
    penaltyOutGoalPer1Chukka5, penaltyOutGoalPer1Chukka6, \
    penaltyOutGoalPer2Chukka1, penaltyOutGoalPer2Chukka2, \
    penaltyOutGoalPer2Chukka3, penaltyOutGoalPer2Chukka4, \
    penaltyOutGoalPer2Chukka5, penaltyOutGoalPer2Chukka6 = penaltyChukka(data1, data2)

    lst_penaltyChukka = [penalty1Chukka1, penalty1Chukka2, penalty1Chukka3,
                         penalty1Chukka4, penalty1Chukka5, penalty1Chukka6,
                         penalty2Chukka1, penalty2Chukka2, penalty2Chukka3,
                         penalty2Chukka4, penalty2Chukka5, penalty2Chukka6,
                         penaltyOutGoal1Chukka1, penaltyOutGoal1Chukka2,
                         penaltyOutGoal1Chukka3, penaltyOutGoal1Chukka4,
                         penaltyOutGoal1Chukka5, penaltyOutGoal1Chukka6,
                         penaltyOutGoal2Chukka1, penaltyOutGoal2Chukka2,
                         penaltyOutGoal2Chukka3, penaltyOutGoal2Chukka4,
                         penaltyOutGoal2Chukka5, penaltyOutGoal2Chukka6,
                         penaltyOutGoalPer1Chukka1, penaltyOutGoalPer1Chukka2,
                         penaltyOutGoalPer1Chukka3, penaltyOutGoalPer1Chukka4,
                         penaltyOutGoalPer1Chukka5, penaltyOutGoalPer1Chukka6,
                         penaltyOutGoalPer2Chukka1, penaltyOutGoalPer2Chukka2,
                         penaltyOutGoalPer2Chukka3, penaltyOutGoalPer2Chukka4,
                         penaltyOutGoalPer2Chukka5, penaltyOutGoalPer2Chukka6]

    ###################
    foul1Chukka1, foul1Chukka2, foul1Chukka3, \
    foul1Chukka4, foul1Chukka5, foul1Chukka6, \
    foul2Chukka1, foul2Chukka2, foul2Chukka3, \
    foul2Chukka4, foul2Chukka5, foul2Chukka6 = foulChukka(data1, data2)

    lst_foulChukka = [foul1Chukka1, foul1Chukka2, foul1Chukka3,
                      foul1Chukka4, foul1Chukka5, foul1Chukka6,
                      foul2Chukka1, foul2Chukka2, foul2Chukka3,
                      foul2Chukka4, foul2Chukka5, foul2Chukka6]

    ###################

    topPlayerGoals1Chukka1, topPlayerGoals1Chukka2, \
    topPlayerGoals1Chukka3, topPlayerGoals1Chukka4, \
    topPlayerGoals1Chukka5, topPlayerGoals1Chukka6, \
    topPlayerGoals2Chukka1, topPlayerGoals2Chukka2, \
    topPlayerGoals2Chukka3, topPlayerGoals2Chukka4, \
    topPlayerGoals2Chukka5, topPlayerGoals2Chukka6, \
    topPlayers1Chukka1, topPlayers1Chukka2, topPlayers1Chukka3, \
    topPlayers1Chukka4, topPlayers1Chukka5, topPlayers1Chukka6, \
    topPlayers2Chukka1, topPlayers2Chukka2, topPlayers2Chukka3, \
    topPlayers2Chukka4, topPlayers2Chukka5, topPlayers2Chukka6, \
    totalTopPlayers1Chukka1, totalTopPlayers1Chukka2, \
    totalTopPlayers1Chukka3, totalTopPlayers1Chukka4, \
    totalTopPlayers1Chukka5, totalTopPlayers1Chukka6, \
    totalTopPlayers2Chukka1, totalTopPlayers2Chukka2, \
    totalTopPlayers2Chukka3, totalTopPlayers2Chukka4, \
    totalTopPlayers2Chukka5, totalTopPlayers2Chukka6 = topPlayersChukka(data1, data2)

    lst_topPlayersChukka = [topPlayerGoals1Chukka1, topPlayerGoals1Chukka2,
                            topPlayerGoals1Chukka3, topPlayerGoals1Chukka4,
                            topPlayerGoals1Chukka5, topPlayerGoals1Chukka6,
                            topPlayerGoals2Chukka1, topPlayerGoals2Chukka2,
                            topPlayerGoals2Chukka3, topPlayerGoals2Chukka4,
                            topPlayerGoals2Chukka5, topPlayerGoals2Chukka6,
                            topPlayers1Chukka1, topPlayers1Chukka2, topPlayers1Chukka3,
                            topPlayers1Chukka4, topPlayers1Chukka5, topPlayers1Chukka6,
                            topPlayers2Chukka1, topPlayers2Chukka2, topPlayers2Chukka3,
                            topPlayers2Chukka4, topPlayers2Chukka5, topPlayers2Chukka6,
                            totalTopPlayers1Chukka1, totalTopPlayers1Chukka2,
                            totalTopPlayers1Chukka3, totalTopPlayers1Chukka4,
                            totalTopPlayers1Chukka5, totalTopPlayers1Chukka6,
                            totalTopPlayers2Chukka1, totalTopPlayers2Chukka2,
                            totalTopPlayers2Chukka3, totalTopPlayers2Chukka4,
                            totalTopPlayers2Chukka5, totalTopPlayers2Chukka6]

    ###################

    topAssistGoals1Chukka1, topAssistGoals1Chukka2, \
    topAssistGoals1Chukka3, topAssistGoals1Chukka4, \
    topAssistGoals1Chukka5, topAssistGoals1Chukka6, \
    topAssistGoals2Chukka1, topAssistGoals2Chukka2, \
    topAssistGoals2Chukka3, topAssistGoals2Chukka4, \
    topAssistGoals2Chukka5, topAssistGoals2Chukka6, \
    topAssists1Chukka1, topAssists1Chukka2, \
    topAssists1Chukka3, topAssists1Chukka4, \
    topAssists1Chukka5, topAssists1Chukka6, \
    topAssists2Chukka1, topAssists2Chukka2, \
    topAssists2Chukka3, topAssists2Chukka4, \
    topAssists2Chukka5, topAssists2Chukka6, \
    totalTopAssists1Chukka1, totalTopAssists1Chukka2, \
    totalTopAssists1Chukka3, totalTopAssists1Chukka4, \
    totalTopAssists1Chukka5, totalTopAssists1Chukka6, \
    totalTopAssists2Chukka1, totalTopAssists2Chukka2, \
    totalTopAssists2Chukka3, totalTopAssists2Chukka4, \
    totalTopAssists2Chukka5, totalTopAssists2Chukka6 = topAssistsChukka(data1, data2)

    lst_topAssistsChukka = [topAssistGoals1Chukka1, topAssistGoals1Chukka2,
                            topAssistGoals1Chukka3, topAssistGoals1Chukka4,
                            topAssistGoals1Chukka5, topAssistGoals1Chukka6,
                            topAssistGoals2Chukka1, topAssistGoals2Chukka2,
                            topAssistGoals2Chukka3, topAssistGoals2Chukka4,
                            topAssistGoals2Chukka5, topAssistGoals2Chukka6,
                            topAssists1Chukka1, topAssists1Chukka2,
                            topAssists1Chukka3, topAssists1Chukka4,
                            topAssists1Chukka5, topAssists1Chukka6,
                            topAssists2Chukka1, topAssists2Chukka2,
                            topAssists2Chukka3, topAssists2Chukka4,
                            topAssists2Chukka5, topAssists2Chukka6,
                            totalTopAssists1Chukka1, totalTopAssists1Chukka2,
                            totalTopAssists1Chukka3, totalTopAssists1Chukka4,
                            totalTopAssists1Chukka5, totalTopAssists1Chukka6,
                            totalTopAssists2Chukka1, totalTopAssists2Chukka2,
                            totalTopAssists2Chukka3, totalTopAssists2Chukka4,
                            totalTopAssists2Chukka5, totalTopAssists2Chukka6]

    ###################

    bothTopPlayerAssist1_1, bothTopPlayerAssist1_2, \
    bothTopPlayerAssist1_3, bothTopPlayerAssist1_4, \
    bothTopPlayerAssist1_5, bothTopPlayerAssist1_6, \
    bothTopPlayerAssist2_1, bothTopPlayerAssist2_2, \
    bothTopPlayerAssist2_3, bothTopPlayerAssist2_4, \
    bothTopPlayerAssist2_5, bothTopPlayerAssist2_6 = topPlayerAssistsChukka(topPlayers1Chukka1, topAssists1Chukka1,
                                                                            topPlayers1Chukka2, topAssists1Chukka2,
                                                                            topPlayers1Chukka3, topAssists1Chukka3,
                                                                            topPlayers1Chukka4, topAssists1Chukka4,
                                                                            topPlayers1Chukka5, topAssists1Chukka5,
                                                                            topPlayers1Chukka6, topAssists1Chukka6,
                                                                            topPlayers2Chukka1, topAssists2Chukka1,
                                                                            topPlayers2Chukka2, topAssists2Chukka2,
                                                                            topPlayers2Chukka3, topAssists2Chukka3,
                                                                            topPlayers2Chukka4, topAssists2Chukka4,
                                                                            topPlayers2Chukka5, topAssists2Chukka5,
                                                                            topPlayers2Chukka6, topAssists2Chukka6)

    lst_topPlayerAssistsChukka = [bothTopPlayerAssist1_1, bothTopPlayerAssist1_2,
                                  bothTopPlayerAssist1_3, bothTopPlayerAssist1_4,
                                  bothTopPlayerAssist1_5, bothTopPlayerAssist1_6,
                                  bothTopPlayerAssist2_1, bothTopPlayerAssist2_2,
                                  bothTopPlayerAssist2_3, bothTopPlayerAssist2_4,
                                  bothTopPlayerAssist2_5, bothTopPlayerAssist2_6]

    ###################
    finalLst = lst_basicInfo + lst_separateTeamsData + lst_shotAtGoalInfo + lst_penaltyInfo + \
               lst_topPlayersInfo + lst_topAssistsInfo + \
               lst_topPlayerAssist + lst_goalsChukka + lst_shotAtGoalChukka + \
               lst_penaltyChukka + lst_foulChukka + lst_topPlayersChukka + \
               lst_topAssistsChukka + lst_topPlayerAssistsChukka

    return finalLst

