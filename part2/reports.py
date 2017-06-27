
# Report functions

import csv
import operator


def import_data(file_name=None):
    if file_name is None:
        file_name = "game_stat.txt"
    with open(file_name, "r") as data:
        reader = csv.reader(data, delimiter="\t")
        game_data = []
        for row in reader:
            game_data.append(row)
        return game_data


def get_most_played(file_name):
    most_played, played = None, 0
    for game in import_data(file_name):
        if float(game[1]) > played:
            most_played, played = game[0], float(game[1])
    return most_played


def sum_sold(file_name):
    total = 0
    for game in import_data(file_name):
        total += float(game[1])
    return total


def get_selling_avg(file_name):
    return sum_sold(file_name) / len(import_data(file_name))


def count_longest_title(file_name):
    char, name = 0, None
    for game in import_data(file_name):
        if len(game[0]) > char:
            char, name = len(game[0]), game[0]

    return len(name)


def get_date_avg(file_name):
    rel_date = 0
    for game in import_data(file_name):
        rel_date += int(game[2])
    return round(rel_date / len(import_data(file_name)), 0)


def get_game(file_name, title):
    for game in import_data(file_name):
        if game[0] == title:
            return [str(game[0]), float(game[1]), int(game[2]), str(game[3]), str(game[4])]


def count_grouped_by_genre(file_name):
    answer = {}
    for game in import_data(file_name):
        if game[3] in answer:
            answer[game[3]] += 1
        else:
            answer[game[3]] = 1
    return answer


def get_date_ordered(file_name):
    answer = []
    for game in sorted(import_data(file_name), key=lambda x: (-int(x[2]), x[0])):
        answer.append(game[0])
    return answer


def main():
    print(get_date_ordered(None))
    pass


if __name__ == "__main__":
    main()
