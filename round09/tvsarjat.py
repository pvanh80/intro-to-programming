# TIE-02100 Johdatus ohjelmointiin
# Read genres and tv-series from a file into a dict. Print a list of the genres in 
# alphabetical order and list tv-series by given genre on user's command.
# Phan Viet anh
# 256296

def read_file(filename):
    # reads and saves the series and their genres from the file

    # TODO initialize a new data structure
    tv_show = []
    try:
        file = open(filename, "r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            # TODO add the info to the data structure
            tv_show.append(name)
            tv_show.append(genres)

        file.close()
        return  tv_show # TODO return the data structure

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():

    filename = input("Enter the name of the file: ")
    tv_show = read_file(filename)
    genre_group = []
    unique_genre = []
    # TODO print the genres
    for genre_collection in tv_show[1::2]:
        for genre in genre_collection:
            genre_group.append(genre)
    genre_group.sort()
    for index in range(len(genre_group)):

        if genre_group[index] != genre_group[index-1]:
            unique_genre.append(genre_group[index])

        if index == len(genre_group):
            break

    genre_print = ', '.join(element for element in unique_genre)

    print('Available genres are: ' + genre_print)

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        # TODO print the series ...
        temp = []
        for index in range(len(tv_show)):

            if index % 2 == 1:

                if genre in tv_show[index]:

                    temp.append(tv_show[index-1])
        for element in sorted(temp):
            print(element)
        temp = []

main()
