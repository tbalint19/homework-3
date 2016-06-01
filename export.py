from reports import *


# This can be modified, if Judy changes her mind, and wants other info.
list_to_observe = 'game_stat.txt'
year_to_observe = 2008
genre_to_count = 'RPG'
game_to_find = 'The Sims'


# These are the imported functions. The arguments are given above.
number_of_games = count_games(list_to_observe)
is_there_a_game = decide(list_to_observe, year_to_observe)
latest_game_from_list = get_latest(list_to_observe)
how_many_by_genre = count_by_genre(list_to_observe, genre_to_count)
line_number = get_line_number_by_title(list_to_observe, game_to_find)


# The report is written here from the data generated above.
report = open('Report to Judy', 'w')

report.write("Dear Judy\nThere are " + str(number_of_games) +
 " games in this list.\nYou asked if there is a game in this list from " +
 str(year_to_observe) + ". It is " + str(is_there_a_game) +
 ".\nThe latest game from this list is " + str(latest_game_from_list) +
 ".\nThere are " + str(how_many_by_genre) + " " + str(genre_to_count) +
 " games in this list.\nYou wanted to find " + str(game_to_find) +
 ". It is in line " + str(line_number) + ".")

report.close
