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

    return False


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

    if game_found_in_list == False:
        # raise ValueError("No game found in list with this title!")
        # The value error above can not be handled during the report writing.
        # Instead of value error, I return something.
        return "...wait a sec...It is not even in the list"
