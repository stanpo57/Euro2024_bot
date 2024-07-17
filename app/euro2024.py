import re
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
        for s in f:
            match_dict = {'id': i + 1,
                          'datetime': re.search(r'\((.+?)\)', s)[1].split(',')[1].strip(),
                          'played': 0,
                          'hosts': s.split()[1],
                          'goals_hosts': 0,
                          'guests': s.split()[3],
                          'goals_guests': 0,
                          'info': re.search(r'\((.+?)\)', s)[1].strip()}

            if s.find('>') - s.find('<') > 2:   # если матч сыгран
                h = s[s.find('<')+1:s.find('>'):].split(':')[0].strip()
                g = s[s.find('<')+1:s.find('>'):].split(':')[1].strip()
                match_dict['played'] = 1
                match_dict['goals_hosts'] = int(h)
                match_dict['goals_guests'] = int(g)
                match_dict['info'] += '; ' + s[s.find('[')+1:s.find(']'):]

            matches_list.append(match_dict)
            i += 1

    return matches_list


def matches_final_load(file):   # загрузка расписания финальных матчей из файла
    matches_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for s in f:
            match_dict = {'id': int(s.split()[0]),
                          'datetime': re.search(r'\((.+?)\)', s)[1].split(',')[1].strip(),
                          'played': 0,
                          'final': s[s.find('1/'):s.find('1/') + 3],
                          'hosts': s.split()[1],
                          'goals_hosts': 0,
                          'guests': s.split()[3],
                          'goals_guests': 0,
                          'goals_hosts_extratime': 0,
                          'goals_guests_extratime': 0,
                          'goals_hosts_penalty': 0,
                          'goals_guests_penalty': 0,
                          'info': re.search(r'\((.+?)\)', s)[1].strip()}
            matches_list.append(match_dict)

            if s.find('>') - s.find('<') > 2:  # если матч сыгран
                results = s[s.find('<') + 1:s.find('>'):].split(':')

                if len(results) == 2:
                    h = results[0].strip()
                    g = results[1].strip()
                    match_dict['goals_hosts'] = int(h)
                    match_dict['goals_guests'] = int(g)

                elif len(results) == 3:
                    h = results[0].strip()
                    g = results[1].split()[0].strip()
                    h_ext = results[1].split()[1].strip()
                    g_ext = results[2].strip()
                    match_dict['goals_hosts'] = int(h)
                    match_dict['goals_guests'] = int(g)
                    match_dict['goals_hosts_extratime'] = int(h_ext)
                    match_dict['goals_guests_extratime'] = int(g_ext)

                elif len(results) == 4:
                    h = results[0].strip()
                    g = results[1].split()[0].strip()
                    h_ext = results[1].split()[1].strip()
                    g_ext = results[2].split()[0].strip()
                    h_pen = results[2].split()[1].strip()
                    g_pen = results[3].strip()
                    match_dict['goals_hosts'] = int(h)
                    match_dict['goals_guests'] = int(g)
                    match_dict['goals_hosts_extratime'] = int(h_ext)
                    match_dict['goals_guests_extratime'] = int(g_ext)
                    match_dict['goals_hosts_penalty'] = int(h_pen)
                    match_dict['goals_guests_penalty'] = int(g_pen)

                match_dict['played'] = 1
                match_dict['goals_hosts'] = int(h)
                match_dict['goals_guests'] = int(g)
                match_dict['info'] += '; ' + s[s.find('[') + 1:s.find(']'):]

    return matches_list


def rating_fifa_load(file):     # загрузка рейтинга фифа из файла
    rating_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for l in f:
            rating_dict[l.split()[2]] = float(l.split()[3])

    return rating_dict


def rating_uefa(file):     # загрузка рейтинга уефа из файла с рейтингом фифа
    rating_dict = {}
    with open(file, 'r', encoding='utf-8') as f:
        for l in f:
            if l.split()[5] == "УЕФА":
                rating_dict[l.split()[2]] = float(l.split()[3])

    return rating_dict


def msg_to_file(msg_in, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(msg_in)
    except Exception as e:
        print(f"Произошла ошибка при сохранении строки в файл: {e}")

    return


def ratings_to_bot(ratings, n:int, width:int):     # формирование списка рейтингов для вывода в бот
    msg = ""
    ratings_sorted = sorted(ratings.items(), key=lambda item: item[1], reverse=True)

    for i in range(n-50, min(len(ratings_sorted), n)):
        id_team = str(i + 1).rjust(3)
        t = str(ratings_sorted[i][0]).ljust(width)
        r = round(ratings_sorted[i][1])
        msg += f"\n{id_team} {t}-{r}"

    return msg


def rating_euro(file):  # формирование рейтингов команд участников че2024
    teams_list = []
    teams_dict = {}

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            teams_list.append(line.strip())

    rating_of_team = rating_fifa_load("input/input_rating_fifa.txt")
    for team in teams_list:
        teams_dict[team] = rating_of_team[team]

    return teams_dict


def rating_team(team):  # выборка рейтинга команды из списка рейтингов
    if team in rating_fifa:
        return rating_fifa[team]
    else:
         return 0


def rating_teams(teams_in):    # занесение рейтингов в список команд
    for s in teams_in:
        teams_in[s][8] = rating_team(s)


def test_team(team):    # проверка наличия команды в списке
    if team in teams:
        return f'{team} - OK'
    else:
         return f'{team} - not presented'


def test_matches(matches_in):  # сверка команд из списка команд с расписанием матчей
    for s in matches_in:
        print(test_team(s["hosts"]))
        print(test_team(s["guests"]))


def tables_formation(teams_in, matches_in):   # формирование таблиц по группам в соответствии с результатами матчей
    for key in teams_in:
        teams_in[key][1:8] = [0] * 7

    for i in range(len(matches_in)):
        if matches_in[i]["played"]:
            teams_in[matches_in[i]["hosts"]][1] += 1
            teams_in[matches_in[i]["hosts"]][5] += matches_in[i]["goals_hosts"]
            teams_in[matches_in[i]["hosts"]][6] += matches_in[i]["goals_guests"]

            teams_in[matches_in[i]["guests"]][1] += 1
            teams_in[matches_in[i]["guests"]][5] += matches_in[i]["goals_guests"]
            teams_in[matches_in[i]["guests"]][6] += matches_in[i]["goals_hosts"]

            if matches_in[i]["goals_hosts"] > matches_in[i]["goals_guests"]:
                teams_in[matches_in[i]["hosts"]][2] += 1
                teams_in[matches_in[i]["hosts"]][7] += 3
                teams_in[matches_in[i]["guests"]][4] += 1

            elif matches_in[i]["goals_hosts"] < matches_in[i]["goals_guests"]:
                teams_in[matches_in[i]["guests"]][2] += 1
                teams_in[matches_in[i]["guests"]][7] += 3
                teams_in[matches_in[i]["hosts"]][4] += 1

            else:
                teams_in[matches_in[i]["hosts"]][3] += 1
                teams_in[matches_in[i]["hosts"]][7] += 1
                teams_in[matches_in[i]["guests"]][3] += 1
                teams_in[matches_in[i]["guests"]][7] += 1

    return teams_in


def tables_sort(teams_in):     # сортировка таблиц по группам
    for k, v in teams_in.items():
        v[9] = (9-v[0])*10000000 + v[7]*1000000 + (v[5]-v[6]+20)*10000 + v[5]*100
    teams_sorted = sorted(teams_in.items(), key=lambda item: item[1][9], reverse=True)

    for i in range(len(teams_sorted)):
        if (i+1) % 4 == 0:
            teams_sorted[i][1][9] = 4
        else:
            teams_sorted[i][1][9] = (i+1) % 4

    return teams_sorted


def tables_print(teams_in): # печать групповых результатов
    i = 0
    for s in teams_in:
        if i % 4 == 0:
            print(' ')
            print(f'  Группа {chr(int(i / 4) + 65)}')
            print('  команды        и  в  н  п  мз мп о')
        print(
            f'{s[1][9]} {s[0].ljust(12)}   {s[1][1]}  {s[1][2]}  {s[1][3]}  {s[1][4]}  {s[1][5]}  {s[1][6]}  {s[1][7]}   {s[1][8]}')
        i += 1


def matches_to_bot(matches_in, real):    # формирование групповых результатов для вывода в бот
    msg = "\n"
    for s in matches_in:
        match_num = f"<{str(s['id'])}>".rjust(4)
        d = s['datetime'].rjust(13)
        h = s['hosts'].rjust(10)
        g = s['guests'].ljust(10)

        if s['played']:
            h_g = str(s['goals_hosts']).rjust(2)
            g_g = str(s['goals_guests']).ljust(2)
        else:
            h_g = ' -'
            g_g = '-'
        msg += f"\n{match_num}  {d} \n{h} -{g} {h_g}:{g_g}"

    if real:
        msg_to_file(msg, "txt/txt_matches.txt")

    return msg


def matches_group_to_bot(matches_in, group, real):   # формирование результатов матчей для группы для вывода в бот
    msg = ""
    for s in matches_in:

        if s['hosts'] in groups[group]:
            match_num = f"<{str(s['id'])}>".rjust(2)
            d = s['datetime'].rjust(13)
            h = s['hosts'].rjust(10)
            g = s['guests'].ljust(10)

            if s['played']:
                h_g = str(s['goals_hosts']).rjust(2)
                g_g = str(s['goals_guests']).ljust(2)
            else:
                h_g = ' -'
                g_g = '-'
            msg += f"\n{match_num}  {d} \n{h} -{g} {h_g}:{g_g}"

    if real:
        msg_to_file(msg, f"txt/txt_matches_gr{str(group)}.txt")

    return msg


def tables_to_bot(teams_in, real):   # формирование таблиц групповых результатов для вывода в бот
    msg = ""
    i = 0

    for s in teams_in:
        if i % 4 == 0:
            msg += f'\n\n  Группа {chr(int(i / 4) + 65)}'
            msg += f'\n  команды    и в н п мз мп о'
        pl = s[1][9]
        te = s[0].ljust(10)
        gm = s[1][1]
        wi = s[1][2]
        no = s[1][3]
        lo = s[1][4]
        g_wi = str(s[1][5]).ljust(2)
        g_lo = str(s[1][6]).ljust(2)
        sc = s[1][7]
        msg += f'\n{pl} {te} {gm} {wi} {no} {lo} {g_wi} {g_lo} {sc}'
        i += 1

    if real:
        msg_to_file(msg, "txt/txt_tables.txt")

    return msg


def table_group_to_bot(teams_in, group, real):   # формирование таблиц по группам для вывода в бот
    msg = ""
    msg += f'\n\n  Группа {chr(group + 64)}'
    msg += f'\n  команды    и в н п мз мп о'

    for s in teams_in:
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
            msg += f'\n{pl} {te} {gm} {wi} {no} {lo} {g_wi} {g_lo} {sc}'

    if real:
        msg_to_file(msg, f"txt/txt_table_group{str(group)}.txt")

    return msg


def matches_num_dict(matches_groups, matches_finals):
    num_dict = {}
    for i in range(len(matches_groups)):
        num_dict[matches_groups[i]["id"]] = [1,i]

    for i in range(len(matches_finals)):
        num_dict[matches_finals[i]["id"]] = [2,i]

    return num_dict


def match_info_to_bot(matches_groups, matches_finals, match_num: int):  # формирование детальной информации матча для вывода в бот
    match_inds = matches_num_dict(matches, matches_final)

    if match_num in match_inds:
        match_ind = match_inds[match_num][1]

        if match_inds[match_num][0] == 1:
            match_num = str(matches_groups[match_ind]['id']).rjust(2)
            d = matches_groups[match_ind]['datetime'].rjust(13)
            h = matches_groups[match_ind]['hosts']
            g = matches_groups[match_ind]['guests']
            inf = matches_groups[match_ind]['info']

            if matches_groups[match_ind]['played'] == 1:
                h_g = str(matches_groups[match_ind]['goals_hosts']).rjust(2)
                g_g = str(matches_groups[match_ind]['goals_guests']).ljust(2)
            else:
                h_g = '- '
                g_g = ' -'

            result = f"{h} - {g}  {h_g}:{g_g}".ljust(35)
            msg = f"\n<{match_num}>  {d} \n{result} \n\n{inf}"

            return msg

        else:
            match_num = str(matches_finals[match_ind]['id']).rjust(2)
            d = matches_finals[match_ind]['datetime'].rjust(13)
            h = matches_finals[match_ind]['hosts']
            g = matches_finals[match_ind]['guests']
            inf = matches_finals[match_ind]['info']

            if matches_finals[match_ind]['played'] == 1:
                h_g = str(matches_finals[match_ind]['goals_hosts']).rjust(2)
                g_g = str(matches_finals[match_ind]['goals_guests']).ljust(2)
                h_g_p = "    "
                g_g_p = "   "

                if int(h_g) == int(g_g):
                    h_g = str(int(h_g) + matches_finals[match_ind]['goals_hosts_extratime'])
                    g_g = str(int(g_g) + matches_finals[match_ind]['goals_guests_extratime'])
                    if int(h_g) == int(g_g):
                        h_g_p = "(" + str(matches_finals[match_ind]['goals_hosts_penalty']) + ":"
                        g_g_p = str(matches_finals[match_ind]['goals_guests_penalty']) + ")"

            else:
                h_g = '- '
                g_g = ' -'
                h_g_p = '    '
                g_g_p = '   '

            result = f"{h} - {g}  {h_g}:{g_g} {h_g_p}{g_g_p}".ljust(35)
            msg = f"\n<{match_num}>  {d} \n{result} \n\n{inf}"

            return msg

    else:

        return False


def separator(n):   # разделитель
    msg = f"\n{'-' * n}"

    return msg


def finalists_from_group(groups_itog):   # выбока участников финального турнира из групп
    finalists_gr = {}
    finalists_3 = {}

    for i in range(0, len(groups_itog) - 1, 4):
        if groups_itog[i][1][1]+groups_itog[i + 1][1][1]+groups_itog[i + 2][1][1]+groups_itog[i + 3][1][1]==12:
            key1 = f"1{chr(groups_itog[i][1][0] + 64)}"
            key2 = f"2{chr(groups_itog[i][1][0] + 64)}"
            key3 = groups_itog[i + 2][0]
            finalists_gr[key1] = groups_itog[i][0]
            finalists_gr[key2] = groups_itog[i + 1][0]
            finalists_3[key3] = groups_itog[i + 2][1]

        if len(finalists_3) == 6:
            for k, v in finalists_3.items():
                v[9] = v[7]*1000000 + (v[5]-v[6]+20)*10000 + v[5]*100
                finalists_3_sorted = sorted(finalists_3.items(), key=lambda item: item[1][9], reverse=True)
                finalists_gr['3A/B/C/D'] = finalists_3_sorted[0][0]
                finalists_gr['3A/D/E/F'] = finalists_3_sorted[1][0]
                finalists_gr['3D/E/F'] = finalists_3_sorted[2][0]
                finalists_gr['3A/B/C'] = finalists_3_sorted[3][0]

    return finalists_gr


def final_8_formation(finalists_fin, matches_final_in):    # формирование пар участников 1/8 финала
    for s in matches_final_in:
        if s['final'] == '1/8':
            if finalists_fin.get(s['hosts']) is not None:
                s['hosts'] = finalists_fin[s['hosts']]

            if finalists_fin.get(s['guests']) is not None:
                s['guests'] = finalists_fin[s['guests']]

    return matches_final_in


def matches_final_to_bot(matches_in, real):  # формирование результатов финального турнира для вывода в бот
    f = matches_final[0]['final']
    msg = f"\n {f} финала"
    for s in matches_in:
        if f != s['final']:
            f = s['final']
            msg += f"\n\n {f} финала"

        match_num =str(s['id']).rjust(2)
        d = s['datetime'].rjust(13)
        h = s['hosts'].rjust(10)
        g = s['guests'].ljust(10)

        if s['played']:
            h_g = str(s['goals_hosts']).rjust(2)
            g_g = str(s['goals_guests']).ljust(2)
            h_g_p, g_g_p = "", ""

            if s['goals_hosts'] == s['goals_guests']:
                h_g = str(s['goals_hosts'] + s['goals_hosts_extratime']).rjust(2)
                g_g = str(s['goals_guests'] + s['goals_guests_extratime']).ljust(2)

                if s['goals_hosts'] + s['goals_hosts_extratime'] == s['goals_guests'] + s['goals_guests_extratime']:
                    h_g_p = str(s['goals_hosts_penalty'])
                    g_g_p = str(s['goals_guests_penalty'])
        else:
            h_g = ' -'
            g_g = '-'
            h_g_p = ''
            g_g_p = ''

        if h_g_p != "":
            msg += f"\n<{match_num}> {d} \n{h}-{g} {h_g}:{g_g}({h_g_p}:{g_g_p})"
        else:
            msg += f"\n<{match_num}> {d} \n{h}-{g} {h_g}:{g_g}"

    if real:
        msg_to_file(msg, "txt/txt_matches_final.txt")

    return msg


def finalists_from_finals(matches_final_in, final):    # выборка списка победителей матчей финального турнира
    finalists_fin = {}

    for s in matches_final_in:
        if s['final'] == final:

            if not s['played']:
                finalists_fin[s['id']] = str(s['id'])
            else:
                g_h = s['goals_hosts'] + s['goals_hosts_extratime'] + s['goals_hosts_penalty']
                g_g = s['goals_guests'] + s['goals_guests_extratime'] + s['goals_guests_penalty']
                winner = s['hosts'] if g_h > g_g else s['guests']
                finalists_fin[s['id']] = winner

    return finalists_fin


def final_4_formation(finalists_in, matches_final_in):    # формирование пар участников 1/4 финала
    for s in matches_final_in:

        if s['final'] == '1/4':
            try:
                s.update({'hosts': finalists_in[int(s['hosts'])], "guests": finalists_in[int(s['guests'])]})
            except ValueError:
                pass

    return matches_final_in


def final_2_formation(finalists_fin, matches_final_in):    # формирование пар участников 1/2 финала
    for s in matches_final_in:

        if s['final'] == '1/2':
            try:
                s.update({'hosts': finalists_fin[int(s['hosts'])], "guests": finalists_fin[int(s['guests'])]})
            except ValueError:
                pass

    return matches_final_in


def final_1_formation(finalists_in, matches_final_in):    # формирование пары участников финала
    for s in matches_final_in:

        if s['final'] == '1/1':
            try:
                s.update({'hosts': finalists_in[int(s['hosts'])], "guests": finalists_in[int(s['guests'])]})
            except ValueError:
                pass

    return matches_final_in


def itog_formation(matches_final_in):  # формирование итоговой таблицы
    teams_winners = []
    for s in matches_final_in:

        if s['final'] == "1/1":
            if s['played']:
                g_h = s['goals_hosts'] + s['goals_hosts_extratime'] + s['goals_hosts_penalty']
                g_g = s['goals_guests'] + s['goals_guests_extratime'] + s['goals_guests_penalty']
                if g_h > g_g:
                    teams_winners.append(s['hosts'])
                    teams_winners.append(s['guests'])
                else:
                    teams_winners.append(s['guests'])
                    teams_winners.append(s['hosts'])

            else:
                teams_winners.append('     -     ')
                teams_winners.append('     -     ')

    for s in matches_final_in:

        if s['final'] == "1/2":
            if s['played']:
                g_h = s['goals_hosts'] + s['goals_hosts_extratime'] + s['goals_hosts_penalty']
                g_g = s['goals_guests'] + s['goals_guests_extratime'] + s['goals_guests_penalty']
                if g_h > g_g:
                    teams_winners.append(s['guests'])
                else:
                    teams_winners.append(s['hosts'])

            else:
                teams_winners.append('     -     ')

    return teams_winners


def itog_table_to_bot(teams_win, real):   # формирование итоговой таблицы для вывода в бот
    if real:
        msg = ""
    else:
        msg = f"\n Итог \n"

    i = 1

    for s in teams_win:
        if i < 3:
            place = f'  {i}'
        else:
            place = '3/4'
        msg += f"{place}. {s}\n"
        i += 1

    if real:
        msg_to_file(msg, "txt/txt_itog.txt")

    return msg


teams = teams_load("input/input_teams.txt")[0]
groups = teams_load("input/input_teams.txt")[1]
matches = matches_load("input/input_matches.txt")
matches_final = matches_final_load("input/input_matches_final.txt")
rating_fifa = rating_fifa_load("input/input_rating_fifa.txt")
ratings_uefa = rating_uefa("input/input_rating_fifa.txt")
msg1_ratings = ratings_to_bot(rating_fifa, 50, 20)
msg2_ratings = ratings_to_bot(rating_fifa, 100, 20)
msg3_ratings = ratings_to_bot(rating_fifa, 150, 20)
msg4_ratings = ratings_to_bot(rating_fifa, 200, 20)
msg5_ratings = ratings_to_bot(rating_fifa, 250, 20)
ratings_euro = rating_euro("input/input_teams.txt")
msg_ratings_euro = ratings_to_bot(ratings_euro, 50, 14)
msg1_ratings_uefa = ratings_to_bot(ratings_uefa, 50, 20)
msg2_ratings_uefa = ratings_to_bot(ratings_uefa, 100, 20)
tables_formation(teams, matches)
msg_matches = matches_to_bot(matches, 1) + separator(28)
group_itog = tables_sort(teams)
msg_tables = tables_to_bot(group_itog, 1) + separator(28)
msg_group1 = (table_group_to_bot(group_itog, 1, 1)+'\n'+
              matches_group_to_bot(matches, 1, 1)+separator(28))
msg_group2 = (table_group_to_bot(group_itog, 2, 1)+'\n'+
              matches_group_to_bot(matches, 2, 1)+separator(28))
msg_group3 = (table_group_to_bot(group_itog, 3, 1)+'\n'+
              matches_group_to_bot(matches, 3, 1)+separator(28))
msg_group4 = (table_group_to_bot(group_itog, 4, 1)+'\n'+
              matches_group_to_bot(matches, 4, 1)+separator(28))
msg_group5 = (table_group_to_bot(group_itog, 5, 1)+'\n'+
              matches_group_to_bot(matches, 5, 1)+separator(28))
msg_group6 = (table_group_to_bot(group_itog, 6, 1)+'\n'+
              matches_group_to_bot(matches, 6, 1)+separator(28))
finalists = finalists_from_group(group_itog) # формирование списка команд из групп прошедших в 1/8 финала
# 1/8 финала
matches_final = final_8_formation(finalists, matches_final) # занесение команд из списка финалистов в расписание игр 1/8 финала
finalists_8 = finalists_from_finals(matches_final, '1/8') # формирование списка команд победителей 1/8 финала прошедших в 1/4 финала
# 1/4 финала
matches_final = final_4_formation(finalists_8, matches_final) # занесение команд из сниска победителей 1/8 финала в расписание игр 1/4 финала
finalists_4 = finalists_from_finals(matches_final, '1/4') # формирование списка команд победителей 1/4 финала прошедших в 1/2 финала
# 1/2 финала
matches_final = final_2_formation(finalists_4, matches_final) # занесение команд из сниска победителей 1/4 финала в расписание игр 1/2 финала
finalists_2 = finalists_from_finals(matches_final, '1/2') # формирование списка команд победителей 1/2 финала прошедших в финал
# финал
matches_final = final_1_formation(finalists_2, matches_final)# занесение команд из сниска победителей 1/2 финала в расписание финала
# итоговая таблица
itog_table = itog_formation(matches_final) # формирование итоговой таблицы
msg_final = matches_final_to_bot(matches_final, 1)
msg_itog_table = itog_table_to_bot(itog_table, 1)
msg_matches_final = matches_final_to_bot(matches_final, 1)
