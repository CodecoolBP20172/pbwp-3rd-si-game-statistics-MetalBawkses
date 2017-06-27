
# Export functions

from reports import *


def export_all():

    exp_file = open("expfile.txt", "w")
    exp_file.writelines(str(get_most_played(None)) + "\n")
    exp_file.writelines(str(sum_sold(None)) + "\n")
    exp_file.writelines(str(get_selling_avg(None)) + "\n")
    exp_file.writelines(str(count_longest_title(None)) + "\n")
    exp_file.writelines(str(get_date_avg(None)) + "\n")
    exp_file.writelines(str(get_game(None, "Counter-Strike")) + "\n")
    exp_file.writelines(str(count_grouped_by_genre(None)) + "\n")
    exp_file.writelines(str(get_date_ordered(None)) + "\n")
    exp_file.close()


def main():
    export_all()


if __name__ == "__main__":
    main()
