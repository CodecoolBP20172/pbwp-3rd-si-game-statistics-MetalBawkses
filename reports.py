
# Report functions
import csv
from collections import OrderedDict


def import_data(file_name=None):
    if file_name is None:
        file_name = "game_stat.txt"
    with open(file_name, "r") as data:
        reader = csv.reader(data, delimiter="\t")
        game_data = []
        for row in reader:
            game_data.append(row)
        return game_data


def decide(file_name, year):
    for game in import_data(file_name):
        if int(game[2]) == year:
            return True
    return False


def get_latest(file_name):
    latestyear, latestgame = 0, None
    for game in import_data(file_name):
        if int(game[2]) > latestyear:
            latestyear, latestgame = int(game[2]), game[0]
    return latestgame


def count_by_genre(file_name, genre):
    genre_number = 0
    for game in import_data(file_name):
        if game[3] == genre:
            genre_number += 1
    return genre_number


def get_line_number_by_title(file_name, title):
    n = 0
    for game in import_data(file_name):
        if game[0] == title:
            return n + 1
        else:
            n += 1


def sort_abc(file_name):  # Gnome_sort (https://en.wikipedia.org/wiki/Gnome_sort)
    names = []
    for name in import_data(file_name):
        names.append(name[0])
    pos = 0
    while pos < len(names):
        if pos == 0 or names[pos] >= names[pos - 1]:
            pos += 1
        else:
            a, b = names[pos], names[pos - 1]
            names[pos], names[pos - 1] = b, a
            pos -= 1
    return names


def get_genres(file_name):
    genres = []
    for name in import_data(file_name):
        genres.append(name[3])
    genres = list(set(genres))
    genres.sort(key=lambda v: v.upper())
    return genres


def when_was_top_sold_fps(file_name):
    year, copies_sold = None, 0

    for name in import_data(file_name):
        if name[3] == "First-person shooter":
            if float(name[1]) > copies_sold:
                year, copies_sold = int(name[2]), float(name[1])

    if year is None:
        raise ValueError
    else:
        return year


# returns the number of the games in the input file


def count_games(file_name):
    return len(import_data(file_name))


def main():
    pass


if __name__ == "__main__":
    main()
