# Task 1 - Write a program that generates 26 text files

import string
import random
import csv
from operator import itemgetter

letters_list = list(string.ascii_uppercase)

with open("lesson_10/text_files_task1/summary.txt", "w") as summary_file:
    for letter in letters_list:
        random_number = random.randint(1, 100)
        new_file = open(f"lesson_10/text_files_task1/{letter}.txt", "w+")
        new_file.write(str(random_number))
        new_file.close()
        summary_file.writelines(f'lesson_10/text_files_task1/{letter}.txt: ' + str(random_number) + ' \n')


# Task 2 - Create a file with some content.

content_to_write = 'Kerch Bridge on fire, your defence is terrified. \
                    Kerch Bridge on fire, your defence is terrified. \
                    Kerch Bridge on fire, your defence is terrified. \
                    Kerch Bridge on fire, your defence is terrified'

with open('lesson_10/original_chad_file.txt', 'w') as original_file:
    original_file.write(content_to_write)

with open('lesson_10/pathetic_duplicate.txt', 'w') as pathetic_duplicate:
    with open('lesson_10/original_chad_file.txt', 'r') as original_file:
        content_to_copy = original_file.read()
        pathetic_duplicate.write(content_to_copy.upper())


# Task 3 - Write a program that will simulate user scores in a game

players_names = ['Marvolo', 'Morfin', 'Merope', 'Noctua', 'Ominis']
players_results = []

counter = 0

while counter <= 100:
    for player in players_names:
        current_player_score = []
        score = random.randint(0, 1000)
        current_player_score.append(player)
        current_player_score.append(score)
        players_results.append(current_player_score)
    counter += 1

the_title = ['Player name', 'Score']

with open('lesson_10/game_results.csv', 'w', newline='') as game_results:
    results = csv.writer(game_results)
    results.writerow(the_title)
    results.writerows(players_results)


# Task 4 - Write a script creates a new file called high_scores.csv

with open('lesson_10/game_results.csv', 'r') as game_results_file:
    game_results_read = list(csv.reader(game_results_file, delimiter=","))

game_results_head = ['Player name', 'Highest score']
game_results_body = game_results_read[1:]

# I don't know is itemgetter() restricted for this task
# If yes I'll rebuild the code
game_results_body.sort(key=itemgetter(0, 1), reverse=True)

list_of_top_scores = []
for item in game_results_body:
    if item[0] not in [i[0] for i in list_of_top_scores]:
        list_of_top_scores.append(item)

list_of_top_scores.sort(key=itemgetter(1), reverse=True)

with open('lesson_10/high_scores.csv', 'w', newline='') as high_scores:
    top_scores = csv.writer(high_scores)
    top_scores.writerow(game_results_head)
    top_scores.writerows(list_of_top_scores)
