import re

# from predicts import predict


# from pprint import pprint


def teams_load(file):   # загрузка списка команд и списка групп из файла
    teams_list = []
    teams_list1= []
    teams_dict = {}
    group_dict = {}

    with open(file, 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            teams_list.append([line.strip()] + [i // 4 + 1] + [0] * 9)
            teams_list1.append(line.strip())
            i += 1

    for i in teams_list:
        teams_dict[i[0]] = i[1:]

    for i in range(0, len(teams_list1), 4):
        group_num = i // 4 + 1
        group_list = teams_list1[i:i+4]
        group_dict[group_num] = group_list

    return [teams_dict, group_dict]


def matches_load(file):     # загрузка расписания матчей в группах из файла и результатов
    matches_list = []
    with open(file, 'r', encoding='utf-8') as f:
        i = 0
        for l in f:
            match_dict = {}
            match_dict['id'] = i + 1
            match_dict['datetime'] = re.search(r'\((.+?)\)', l)[1].split(',')[1].strip()
            match_dict['played'] = 0
            match_dict['hosts'] = l.split()[1]
            match_dict['goals_hosts'] = 0
            match_dict['guests'] = l.split()[3]
            match_dict['goals_guests'] = 0
            match_dict['info'] = re.search(r'\((.+?)\)', l)[1].strip()

            if l.find('>') - l.find('<') > 2:   # если матч сыгран
                h = l[l.find('<')+1:l.find('>'):].split(':')[0].strip()
                g = l[l.find('<')+1:l.find('>'):].split(':')[1].strip()
                match_dict['played'] = 1
                match_dict['goals_hosts'] = int(h)
                match_dict['goals_guests'] = int(g)
                match_dict['info'] += '; ' + l[l.find('[')+1:l.find(']'):]

            matches_list.append(match_dict)
            i += 1

    return matches_list


def matches_final_load(file):   # загрузка расписания финальных матчей из файла
    matches_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for l in f:
            match_dict = {}
            match_dict['id'] = int(l.split()[0])
            match_dict['datetime'] = re.search(r'\((.+?)\)', l)[1].split(',')[1].strip()
            match_dict['played'] = 0
            match_dict['final'] = l[l.find('1/'):l.find('1/')+3]
            match_dict['hosts'] = l.split()[1]
            match_dict['goals_hosts'] = 0
            match_dict['guests'] = l.split()[3]
            match_dict['goals_guests'] = 0
            match_dict['goals_hosts_extratime'] = 0
            match_dict['goals_guests_extratime'] = 0
            match_dict['goals_hosts_penalty'] = 0
            match_dict['goals_guests_penalty'] = 0
            match_dict['info'] = re.search(r'\((.+?)\)', l)[1].strip()
            matches_list.append(match_dict)

    return matches_list


def rating_fifa_load(file):     # загрузка рейтинга фифа из файла
    rating_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for l in f:
            rating_dict[l.split()[2]] = float(l.split()[3])

    return rating_dict


def msg_to_file(msg_in, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(msg_in)
    except Exception as e:
        print(f"Произошла ошибка при сохранении строки в файл: {e}")

    return


def ratings_to_bot(ratings, n:int, l:int):     # формирование списка рейтингов для вывода в бот
    if n < 51:
        msg = "\n"
    else:
        msg = ""
    ratings_sorted = sorted(ratings.items(), key=lambda item: item[1], reverse=True)

    for i in range(n-50, min(len(ratings_sorted), n)):
        id = str(i+1).rjust(3)
        t = str(ratings_sorted[i][0]).ljust(l)
        r = ratings_sorted[i][1]
        msg += f"\n{id} {t} - {r}"

    return msg


def rating_euro(file):  # формирование рейтингов команд участников че2024
    teams_list = []
    teams_dict = {}

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            teams_list.append(line.strip())

    rating_fifa = rating_fifa_load("input_rating_fifa.txt")
    for team in teams_list:
        teams_dict[team] = rating_fifa[team]

    return teams_dict


def rating_team(team):  # выборка рейтинга команды из списка рейтингов
    if team in rating_fifa:
        return rating_fifa[team]
    else:
         return 0


def rating_teams(teams):    # занесение рейтингов в список команд
    for s in teams:
        teams[s][8] = rating_team(s)


def test_team(team):    # проверка наличия команды в списке
    if team in teams:
        return f'{team} - OK'
    else:
         return f'{team} - not presented'


def test_matches(matches):  # сверка команд из списка команд с расписанием матчей
    for s in matches:
        print(test_team(s["hosts"]))
        print(test_team(s["guests"]))


def tables_formation(teams, matches):   # формирование таблиц по группам в соответствии с результатами матчей
    for key in teams:
        teams[key][1:8] = [0] * 7

    for i in range(len(matches)):
        if matches[i]["played"]:
            teams[matches[i]["hosts"]][1] += 1
            teams[matches[i]["hosts"]][5] += matches[i]["goals_hosts"]
            teams[matches[i]["hosts"]][6] += matches[i]["goals_guests"]

            teams[matches[i]["guests"]][1] += 1
            teams[matches[i]["guests"]][5] += matches[i]["goals_guests"]
            teams[matches[i]["guests"]][6] += matches[i]["goals_hosts"]

            if matches[i]["goals_hosts"] > matches[i]["goals_guests"]:
                teams[matches[i]["hosts"]][2] += 1
                teams[matches[i]["hosts"]][7] += 3
                teams[matches[i]["guests"]][4] += 1

            elif matches[i]["goals_hosts"] < matches[i]["goals_guests"]:
                teams[matches[i]["guests"]][2] += 1
                teams[matches[i]["guests"]][7] += 3
                teams[matches[i]["hosts"]][4] += 1

            else:
                teams[matches[i]["hosts"]][3] += 1
                teams[matches[i]["hosts"]][7] += 1
                teams[matches[i]["guests"]][3] += 1
                teams[matches[i]["guests"]][7] += 1

    return teams


def tables_sort(teams):     # сортировка таблиц по группам
    for k, v in teams.items():
        v[9] = (9-v[0])*10000000 + v[7]*1000000 + (v[5]-v[6]+20)*10000 + v[5]*100
    teams_sorted = sorted(teams.items(), key=lambda item: item[1][9], reverse=True)

    for i in range(len(teams_sorted)):
        if (i+1) % 4 == 0:
            teams_sorted[i][1][9] = 4
        else:
            teams_sorted[i][1][9] = (i+1) % 4

    return teams_sorted


def tables_print(teams): # печать групповых результатов
    i = 0
    for s in teams:
        if i % 4 == 0:
            print(' ')
            print(f'  Группа {chr(int(i / 4) + 65)}')
            print('  команды        и  в  н  п  мз мп о')
        print(
            f'{s[1][9]} {s[0].ljust(12)}   {s[1][1]}  {s[1][2]}  {s[1][3]}  {s[1][4]}  {s[1][5]}  {s[1][6]}  {s[1][7]}   {s[1][8]}')
        i += 1


def matches_to_bot(matches):    # формирование групповых результатов для вывода в бот
    msg = "\n"
    for l in matches:
        id =str(l['id']).rjust(2)
        d = l['datetime'].rjust(13)
        h = l['hosts'].ljust(10)
        g = l['guests'].ljust(10)
        inf = l['info']
        if l['played']:
            h_g = str(l['goals_hosts']).rjust(2)
            g_g = str(l['goals_guests']).rjust(2)
        else:
            h_g = ' -'
            g_g = ' -'
        msg += f"\n{id} {d} {h} - {g} {h_g} : {g_g}" # {inf}

    msg_to_file(msg, "txt_matches.txt")
    return msg


def matches_group_to_bot(matches, group):   # формирование результатов матчей для группы для вывода в бот
    msg = ""
    for l in matches:

        if l['hosts'] in groups[group]:
            id =str(l['id']).rjust(2)
            d = l['datetime'].rjust(13)
            h = l['hosts'].rjust(10)
            g = l['guests'].ljust(10)
            inf = l['info']
            if l['played']:
                h_g = str(l['goals_hosts']).rjust(2)
                g_g = str(l['goals_guests']).rjust(2)
            else:
                h_g = ' -'
                g_g = ' -'
            # msg += f"\n{id} {d} {h} - {g} {h_g} : {g_g}  {inf}"
            msg += f"\n {d} {h} {h_g} : {g_g} {g}"

    msg_to_file(msg, f"txt_matches_gr{str(group)}.txt")

    return msg


def tables_to_bot(teams):   # формирование таблиц групповых результатов для вывода в бот
    msg = ""
    i = 0

    for s in teams:
        if i % 4 == 0:
            msg += f'\n\n  Группа {chr(int(i / 4) + 65)}'
            msg += f'\n  команды    и  в  н  п  мз  мп  о'
        pl = s[1][9]
        te = s[0].ljust(10)
        gm = s[1][1]
        wi = s[1][2]
        no = s[1][3]
        lo = s[1][4]
        g_wi = str(s[1][5]).ljust(2)
        g_lo = str(s[1][6]).ljust(2)
        sc = s[1][7]
        msg += f'\n{pl} {te} {gm}  {wi}  {no}  {lo}  {g_wi}  {g_lo}  {sc}'
        i += 1

    msg_to_file(msg, "txt_tables.txt")

    return msg


def table_group_to_bot(teams, group):   # формирование таблиц по группам для вывода в бот
    msg = ""
    msg += f'\n\n  Группа {chr(group + 64)}'
    msg += f'\n  команды    и  в  н  п  мз  мп  о'

    for s in teams:
        # print(s)
        if s[1][0] == group:
            pl = s[1][9]
            te = s[0].ljust(10)
            gm = s[1][1]
            wi = s[1][2]
            no = s[1][3]
            lo = s[1][4]
            g_wi = str(s[1][5]).ljust(2)
            g_lo = str(s[1][6]).ljust(2)
            sc = s[1][7]
            msg += f'\n{pl} {te} {gm}  {wi}  {no}  {lo}  {g_wi}  {g_lo}  {sc}'

    msg_to_file(msg, f"txt_table_group{str(group)}.txt")

    return msg


def separator(n):   # разделитель
    msg = f"\n{'-' * n}"

    return msg


def finalists_from_group(group_itog):   # выбока участников финального турнира из групп
    finalists = {}
    finalists_3 = {}
    for s in group_itog:
        if s[1][9] < 3:
            key = str(s[1][9]) + chr(s[1][0]+64)
            finalists[key] = s[0]
        elif s[1][9] == 3:
            key = s[0]
            finalists_3[key] = s[1]

    for k, v in finalists_3.items():
        v[9] = v[7]*1000000 + (v[5]-v[6]+20)*10000 + v[5]*100
    finalists_3_sorted = sorted(finalists_3.items(), key=lambda item: item[1][9], reverse=True)
    finalists['3D/E/F'] = finalists_3_sorted[0][0]
    finalists['3A/D/E/F'] = finalists_3_sorted[1][0]
    finalists['3A/B/C'] = finalists_3_sorted[2][0]
    finalists['3A/B/C/D'] = finalists_3_sorted[3][0]

    return finalists


def final_8_formation(finalists, matches_final):    # формирование пар участников 1/8 финала
    for l in matches_final:
        if l['final'] == '1/8':
            try:
                l.update({'hosts': finalists[l['hosts']], "guests": finalists[l['guests']]})
            except KeyError:
                pass

    return matches_final


def matches_final_to_bot(matches):  # формирование результатов финального турнира для вывода в бот
    f = matches_final[0]['final']
    msg = f"\n {f} финала"
    for l in matches:
        if f != l['final']:
            f = l['final']
            msg += f"\n\n {f} финала"

        id =str(l['id']).rjust(2)
        d = l['datetime'].rjust(13)
        h = l['hosts'].ljust(10)
        g = l['guests'].ljust(10)
        inf = l['info']
        if l['played']:
            h_g = str(l['goals_hosts']).rjust(2)
            g_g = str(l['goals_guests']).rjust(2)
            h_g_p, g_g_p = "", ""
            if l['goals_hosts'] == l['goals_guests']:
                h_g = str(l['goals_hosts'] + l['goals_hosts_extratime']).rjust(2)
                g_g = str(l['goals_guests'] + l['goals_guests_extratime']).rjust(2)
                if l['goals_hosts'] + l['goals_hosts_extratime'] == l['goals_guests'] + l['goals_guests_extratime']:
                    h_g_p = str(l['goals_hosts_penalty']).rjust(2)
                    g_g_p = str(l['goals_guests_penalty']).rjust(2)
        else:
            h_g = ' -'
            g_g = ' -'
            h_g_p = ''
            g_g_p = ''

        if h_g_p != "":
            msg += f"\n{id} {d} {h} - {g} {h_g} : {g_g} ({h_g_p} : {g_g_p})" # {inf}
        else:
            msg += f"\n{id} {d} {h} - {g} {h_g} : {g_g}"  # {inf}

    msg_to_file(msg, "txt_matches_final.txt")

    return msg


def finalists_from_finals(matches_final, final):    # выборка списка победителей матчей финального турнира
    finalists = {}

    for l in matches_final:
        if l['final'] == final:

            if not l['played']:
                finalists[l['id']] = '-'
            else:
                g_h = l['goals_hosts'] + l['goals_hosts_extratime'] + l['goals_hosts_penalty']
                g_g = l['goals_guests'] + l['goals_guests_extratime'] + l['goals_guests_penalty']
                winner = l['hosts'] if g_h > g_g else l['guests']
                finalists[l['id']] = winner

    return finalists


def final_4_formation(finalists, matches_final):    # формирование пар участников 1/4 финала
    for l in matches_final:
        if l['final'] == '1/4':
            try:
                l.update({'hosts': finalists[int(l['hosts'])], "guests": finalists[int(l['guests'])]})
            except ValueError:
                pass

    return matches_final


def final_2_formation(finalists, matches_final):    # формирование пар участников 1/2 финала
    for l in matches_final:
        if l['final'] == '1/2':
            try:
                l.update({'hosts': finalists[int(l['hosts'])], "guests": finalists[int(l['guests'])]})
            except ValueError:
                pass

    return matches_final


def final_1_formation(finalists, matches_final):    # формирование пары участников финала
    for l in matches_final:
        if l['final'] == '1/1':
            try:
                l.update({'hosts': finalists[int(l['hosts'])], "guests": finalists[int(l['guests'])]})
            except ValueError:
                pass

    return matches_final


def itog_formation(matches_final):  # формирование итоговой таблицы
    teams = []
    for l in matches_final:
        if l['final'] == "1/1":
            g_h = l['goals_hosts'] + l['goals_hosts_extratime'] + l['goals_hosts_penalty']
            g_g = l['goals_guests'] + l['goals_guests_extratime'] + l['goals_guests_penalty']
            if g_h > g_g:
                teams.append(l['hosts'])
                teams.append(l['guests'])
            else:
                teams.append(l['guests'])
                teams.append(l['hosts'])

    for l in matches_final:
        if l['final'] == "1/2":
            g_h = l['goals_hosts'] + l['goals_hosts_extratime'] + l['goals_hosts_penalty']
            g_g = l['goals_guests'] + l['goals_guests_extratime'] + l['goals_guests_penalty']
            if g_h > g_g:
                teams.append(l['guests'])
            else:
                teams.append(l['hosts'])
    return teams


def itog_table_to_bot(teams):   # формирование итоговой таблицы для вывода в бот
    msg = f"\n ИТОГОВАЯ ТАБЛИЦА \n\n"
    i = 1

    for l in teams:
        if i < 3:
            place = f'  {i}'
        else:
            place = '3/4'
        msg += f"{place}. {l}\n"
        i += 1

    msg_to_file(msg, "txt_itog.txt")

    return msg


teams = teams_load("input_teams.txt")[0]
groups = teams_load("input_teams.txt")[1]
matches = matches_load("input_matches.txt")
matches_final = matches_final_load("input matches_final.txt")
rating_fifa = rating_fifa_load("input_rating_fifa.txt")
msg1_ratings = ratings_to_bot(rating_fifa, 50, 33)
msg2_ratings = ratings_to_bot(rating_fifa, 100, 33)
msg3_ratings = ratings_to_bot(rating_fifa, 150, 33)
msg4_ratings = ratings_to_bot(rating_fifa, 200, 33)
msg5_ratings = ratings_to_bot(rating_fifa, 250, 33)
ratings_euro = rating_euro("input_teams.txt")
msg_ratings_euro = ratings_to_bot(ratings_euro, 50, 14)
tables_formation(teams, matches)
msg_matches = matches_to_bot(matches) + separator(48)
group_itog = tables_sort(teams)
msg_tables = tables_to_bot(group_itog) + separator(48)
msg_group1 = table_group_to_bot(group_itog, 1) + '\n' + matches_group_to_bot(matches, 1) + separator(36)
msg_group2 = table_group_to_bot(group_itog, 2) + '\n' + matches_group_to_bot(matches, 2) + separator(36)
msg_group3 = table_group_to_bot(group_itog, 3) + '\n' + matches_group_to_bot(matches, 3) + separator(36)
msg_group4 = table_group_to_bot(group_itog, 4) + '\n' + matches_group_to_bot(matches, 4) + separator(36)
msg_group5 = table_group_to_bot(group_itog, 5) + '\n' + matches_group_to_bot(matches, 5) + separator(36)
msg_group6 = table_group_to_bot(group_itog, 6) + '\n' + matches_group_to_bot(matches, 6) + separator(36)
msg_matches_final = matches_final_to_bot(matches_final)

print(msg_matches)
print(msg_tables)
print(msg_group1)
print(msg_group2)
print(msg_group3)
print(msg_group4)
print(msg_group5)
print(msg_group6)
print(msg1_ratings)
print(msg2_ratings)
print(msg3_ratings)
print(msg4_ratings)
print(msg5_ratings)
print(msg_ratings_euro)

# i = 0
# n = 3
# while i < n:
#     print(f'\n Прогноз \n=========')
#     msg_predict = predict(i + 2)
#     print(msg_predict[0])
#     print(msg_predict[1])
#     print(msg_predict[2])
#     print(msg_predict[3])
#     print(msg_predict[4])
#     print(msg_predict[5])
#     print(msg_predict[6])
#     print(msg_predict[7])
#     print(msg_predict[8])
#     print(msg_predict[9])
#     i += 1

# pprint(rating_fifa)
# pprint(ratings_euro)
# print(msg_ratings_euro)

