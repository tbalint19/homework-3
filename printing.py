from reports import *

print("All games: " + str(count_games('game_stat.txt')))
print("Is there a game?: " + str(decide('game_stat.txt', 2009)))
print("Latest game: " + str(get_latest('game_stat.txt')))
print("How many from a genre?: " + str(count_by_genre('game_stat.txt', 'RPG')))
print("Which line: " + str(get_line_number_by_title('game_stat.txt', 'Diablo II')))
print("Most played: " + str(get_most_played('game_stat.txt')))
print("All sold: " + str(sum_sold('game_stat.txt')))
print("Average of sells: " + str(get_selling_avg('game_stat.txt')))
print("Longest name: " + str(count_longest_title('game_stat.txt')))
print("Average of releases: " + str(get_date_avg('game_stat.txt')))
print("All about a game:\n" + str(get_game('game_stat.txt', 'Diablo III')))
print(count_grouped_by_genre('game_stat.txt'))

# according to this test, it works fine
