
# Export functions

from reports import *


def export_all():

    exp_file = open("expfile.txt", "w")
    exp_file.writelines(str(decide(None, 2005))+"\n")
    exp_file.writelines(str(get_latest(None))+"\n")
    exp_file.writelines(str(count_by_genre(None, "RPG"))+"\n")
    exp_file.writelines(str(get_line_number_by_title(None, "Counter-Strike"))+"\n")
    exp_file.writelines(str(sort_abc(None))+"\n")
    exp_file.writelines(str(get_genres(None))+"\n")
    exp_file.writelines(str(when_was_top_sold_fps(None))+"\n")
    exp_file.writelines(str(count_games(None))+"\n")
    exp_file.close()


def main():
    export_all()


if __name__ == "__main__":
    main()
