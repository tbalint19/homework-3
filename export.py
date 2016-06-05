from reports import *


# This can be modified, if Judy changes her mind, and wants other info.
list_to_observe = 'game_stat.txt'
year_to_observe = 2009
genre_to_count = 'RPG'
game_to_find = 'Minecraft'
game_to_observe = 'Diablo III'


# These are the imported functions. The arguments are given above.
number_of_games = str(count_games(list_to_observe))
is_there_a_game = str(decide(list_to_observe, year_to_observe))
latest_game_from_list = str(get_latest(list_to_observe))
how_many_by_genre = str(count_by_genre(list_to_observe, genre_to_count))
line_number = str(get_line_number_by_title(list_to_observe, game_to_find))
most_played = str(get_most_played(list_to_observe))
sum_of_sold = str(sum_sold(list_to_observe))
avg_of_sold = str(get_selling_avg(list_to_observe))
longest_name_char_num = str(count_longest_title(list_to_observe))
avg_of_releases = str(get_date_avg(list_to_observe))
all_about_a_game = (str(get_game(list_to_observe, game_to_observe)[1:]))[1:-4]


# The report is written here from the data generated above.
report = open('Report to Judy', 'w')

report.write("Dear Judy\nHere you can see all the info you needed:\nNumber of "
"games in this game: " + number_of_games + "\nIs there a game from "
+ str(year_to_observe) + "? It is " + is_there_a_game + "\nThe latest game"
" from the list is: " + latest_game_from_list + "\nNumber of " +
genre_to_count + " games: " + how_many_by_genre + "\n" + game_to_find +
" can be found in line " + line_number + "\nThe most played game is " +
most_played + "\nAlltogether " + sum_of_sold + " millions of copies were sold" +
"\nThis gives us an average of " + avg_of_sold + " per game\nThe game with"
 + "the longest name is made from " + longest_name_char_num + " characters"
 "\nThe average of the years when the games were released: " +
 avg_of_releases + " (rounded up)\nAll data about " + game_to_observe +
 ": " + all_about_a_game)

report.close
