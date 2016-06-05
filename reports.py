import math


def count_games(file_name):

    opened_file = open(file_name, 'r')
    how_many_games = len(opened_file.readlines())
    opened_file.close

    return how_many_games


def decide(file_name, year):

    opened_file = open(file_name, 'r')

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        if list_with_all[2] == str(year):
            return True

    return str(False)


def get_latest(file_name):

    opened_file = open(file_name, 'r')

    list_of_years = []

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        list_of_years.append(int(list_with_all[2]))

    opened_file.close
    opened_file = open(file_name, 'r')

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        if int(list_with_all[2]) == max(list_of_years):
            return list_with_all[0]


def count_by_genre(file_name, genre):

    opened_file = open(file_name, 'r')

    count = 0

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        if list_with_all[3] == genre:
            count += 1

    return count


def get_line_number_by_title(file_name, title):

    opened_file = open(file_name, 'r')

    which_line = 0
    game_found_in_list = False

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        which_line += 1
        if list_with_all[0] == title:
            return which_line

    if not game_found_in_list:
        # raise ValueError("No game found in list with this title!")
        # The value error above can not be handled during the report writing.
        # Instead of value error, I return something.
        return "...wait a sec...It is not even in the list"


def get_most_played(file_name):

    opened_file = open(file_name, 'r')

    list_of_sells = []

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        list_of_sells.append(float(list_with_all[1]))

    opened_file.close
    opened_file = open(file_name, 'r')

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        if float(list_with_all[1]) == max(list_of_sells):
            return list_with_all[0]


def sum_sold(file_name):

    opened_file = open(file_name, 'r')

    list_of_sells = []

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        list_of_sells.append(float(list_with_all[1]))

    opened_file.close

    return sum(list_of_sells)


def get_selling_avg(file_name):

    opened_file = open(file_name, 'r')

    list_of_sells = []

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        list_of_sells.append(float(list_with_all[1]))

    opened_file.close

    return sum(list_of_sells)/len(list_of_sells)


def count_longest_title(file_name):

    opened_file = open(file_name, 'r')

    length_of_titles = []

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        length_of_titles.append(int(len(list_with_all[0])))

    return max(length_of_titles)


def get_date_avg(file_name):

    opened_file = open(file_name, 'r')

    list_of_releases = []

    for all_info in opened_file.readlines():
        list_with_all = all_info.split('\t')
        list_of_releases.append(float(list_with_all[2]))

    opened_file.close

    return int(math.ceil(sum(list_of_releases)/len(list_of_releases)))


def get_game(file_name, title):

        opened_file = open(file_name, 'r')

        for all_info in opened_file.readlines():
            list_with_all = all_info.split('\t')
            if list_with_all[0] == title:
                return list_with_all[:]

        return "There is no game with this title in this list"


def count_grouped_by_genre(file_name):

    opened_file = open(file_name, 'r')
    all_infos = opened_file.readlines()
    opened_file.close

    list_of_genres = []

    for all_info in all_infos:
        list_with_all = all_info.split('\t')
        list_of_genres.append(list_with_all[3])

    list_of_genres = list(set(list_of_genres))

    dict_of_genres = []

    for genre in list_of_genres:
        dict_of_genres.append((genre, 0))

    dict_of_genres = dict(dict_of_genres)

    for all_info in all_infos:
        list_with_all = all_info.split('\t')
        for key in dict_of_genres:
            if key == list_with_all[3]:
                dict_of_genres[key] += 1

    return dict_of_genres


def get_date_ordered(file_name):

    opened_file = open(file_name, 'r')
    all_infos = opened_file.readlines()
    opened_file.close

    for all_info in all_infos:
        list_with_all = all_info.split('\t')
