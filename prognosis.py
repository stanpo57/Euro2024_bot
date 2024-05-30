from random import random, randint

from euro2024 import (
    rating_fifa, teams, matches, matches_final, tables_formation, matches_to_bot, separator,
    tables_sort, tables_to_bot, matches_group_to_bot, table_group_to_bot, finalists_from_group, final_8_formation,
    finalists_from_finals, final_4_formation, final_2_formation, final_1_formation, itog_formation,
    matches_final_to_bot, itog_table_to_bot, msg_to_file,
)


def matches_predict_random(matches):    # рандомное формирование результатов матчей в группах
    for i in range(len(matches)):
        if not matches[i]["played"]:
            matches[i]["goals_hosts"] = randint(0, 3)
            matches[i]["goals_guests"] = randint(0, 3)
            matches[i]["played"] = 1

    return matches


def match_predict(team1, team2):    # формирование прогноза результата матча с учетом рейтинга
    goals_per_match = random() * 5
    random_ratio = 0.2
    # result = [0, 0]
    ratings = [rating_fifa[team1], rating_fifa[team2]]
    result = [ratings[0]/(ratings[0] + ratings[1]),
              ratings[1]/(ratings[0] + ratings[1])]
    randoms = [random() * random_ratio, random() * random_ratio]
    l1 = f"t1 - {team1}, t2 - {team2}; ratings - {ratings}, g_p_m - {goals_per_match}, result - {result}"
    result = [result[0]*randoms[0]/(result[0]*randoms[0]+result[1]*randoms[1]),
            result[1] * randoms[1]/(result[0]*randoms[0]+result[1]*randoms[1])]
    result = [round(result[0] * goals_per_match),
              round(result[1] * goals_per_match)]
    l2 = f"randoms - {randoms}, result - {result}"

    with open("predict_matches_result.txt", "w") as file:
        file.write(l1 + '\n' + l2 + '\n\n')

    return result


def matches_formation_predict(matches):     # формирование прогноза результатов матчей в группах
    for i in range(len(matches)):
        if not matches[i]["played"]:
            result = match_predict(matches[i]["hosts"], matches[i]["guests"])
            matches[i]["goals_hosts"] = result[0]
            matches[i]["goals_guests"] = result[1]
            matches[i]["played"] = 1

    return matches


def penalty_predict():  # прогноз пробития пенальти
    goals = [0, 0]
    goals[0] = randint(0, 3)
    goals[1] = randint(0, 3)
    if abs(goals[1] - goals[0]) == 3:
        return goals
    else:
        goals[0] += randint(0, 1)
        goals[1] += randint(0, 1)

    if abs(goals[1] - goals[0]) >= 2:
        return goals
    else:
        goals[0] += randint(0, 1)
        goals[1] += randint(0, 1)

    if abs(goals[1] - goals[0]) >= 1:
        return goals
    else:
        goals[0] += randint(0, 1)
        goals[1] += randint(0, 1)

    if goals[1] != goals[0]:
        return goals

    while goals[0] == goals[1]:
        goals[0] += randint(0, 1)
        goals[1] += randint(0, 1)
    return goals


def final_formation_predict(matches_final, final):  # прогноз результата матча финального турнира
    for l in matches_final:
        if l["final"] == final and not l["played"]:
            result = match_predict(l["hosts"], l["guests"])
            l["goals_hosts"] = result[0]
            l["goals_guests"] = result[1]
            g_h = l["goals_hosts"]
            g_g = l["goals_guests"]

            if result[0] == result[1]:
                l["goals_hosts_extratime"] = randint(0, 2)
                l["goals_guests_extratime"] = randint(0, 2)
                g_h += l["goals_hosts_extratime"]
                g_g += l["goals_guests_extratime"]

            if g_h == g_g:
                result_penalty = penalty_predict()
                l["goals_hosts_penalty"] = result_penalty[0]
                l["goals_guests_penalty"] = result_penalty[1]

            l["played"] = 1

    return matches_final


def predict(n):     # прогноз
    teams_predict = teams.copy()
    matches_predict = matches.copy()
    matches_final_predict = matches_final.copy()
    matches_formation_predict(matches_predict)
    tables_formation(teams_predict, matches_predict)
    msg_matches_predict = matches_to_bot(matches_predict) + separator(n)
    group_itog_predict = tables_sort(teams_predict)
    msg_tables_predict = tables_to_bot(group_itog_predict) + separator(n)
    msg_group1_predict = matches_group_to_bot(matches_predict, 1) + table_group_to_bot(group_itog_predict, 1) + separator(n)
    msg_group2_predict = matches_group_to_bot(matches_predict, 2) + table_group_to_bot(group_itog_predict, 2) + separator(n)
    msg_group3_predict = matches_group_to_bot(matches_predict, 3) + table_group_to_bot(group_itog_predict, 3) + separator(n)
    msg_group4_predict = matches_group_to_bot(matches_predict, 4) + table_group_to_bot(group_itog_predict, 4) + separator(n)
    msg_group5_predict = matches_group_to_bot(matches_predict, 5) + table_group_to_bot(group_itog_predict, 5) + separator(n)
    msg_group6_predict = matches_group_to_bot(matches_predict, 5) + table_group_to_bot(group_itog_predict, 6) + separator(n)
    finalists_predict = finalists_from_group(group_itog_predict)
    # 1/8 финала
    matches_final_predict = final_8_formation(finalists_predict, matches_final_predict)
    matches_final_predict = final_formation_predict(matches_final_predict, '1/8')
    finalists_8_predict = finalists_from_finals(matches_final_predict, '1/8')
    # 1/4 финала
    matches_final_predict = final_4_formation(finalists_8_predict, matches_final_predict)
    matches_final_predict = final_formation_predict(matches_final_predict, '1/4')
    finalists_4_predict = finalists_from_finals(matches_final_predict, '1/4')
    # 1/2 финала
    matches_final_predict = final_2_formation(finalists_4_predict, matches_final_predict)
    matches_final_predict = final_formation_predict(matches_final_predict, '1/2')
    finalists_2_predict = finalists_from_finals(matches_final_predict, '1/2')
    # финал
    matches_final_predict = final_1_formation(finalists_2_predict, matches_final_predict)
    matches_final_predict = final_formation_predict(matches_final_predict, '1/1')
    # итоговая таблица
    itog_table_predict = itog_formation(matches_final_predict)
    msg_final_predict = matches_final_to_bot(matches_final_predict)
    msg_itog_table_predict = itog_table_to_bot(itog_table_predict)

    return [
        msg_matches_predict,
        msg_tables_predict,
        msg_group1_predict,
        msg_group2_predict,
        msg_group3_predict,
        msg_group4_predict,
        msg_group5_predict,
        msg_group6_predict,
        msg_final_predict,
        msg_itog_table_predict
    ]


new_predict = predict(5)
print(new_predict[0])
print(new_predict[1])
print(new_predict[8])
print(new_predict[9])
