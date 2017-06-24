
# Export functions

from reports import *


def export_all():
    exp_file = open("expfile.txt", "w")
    exp_file.write(str(decide(None, 2005)))
    exp_file.write(str(get_latest(None)))
    exp_file.write(str(count_by_genre(None, "RPG")))
    exp_file.write(str(get_line_number_by_title(None, "Counter-Strike")))
    exp_file.write(str(sort_abc(None)))
    exp_file.write(str(get_genres(None)))
    exp_file.write(str(when_was_top_sold_fps(None)))
    exp_file.write(str(count_games(None)))
    exp_file.close()


def main():
    export_all()


if __name__ == "__main__":
    main()
