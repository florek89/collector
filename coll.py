import csv
from datetime import date
import sys
import random


def read_the_file(albums):
    with open("music.csv") as musicfile:
        read = csv.reader(musicfile, delimiter='|')
        tup1 = ()
        tup2 = ()
        try:
            for row in read:
                tup1 = row[0].strip(), row[1].strip()
                tup2 = int(row[2].strip()), row[3].strip(), row[4].strip()
                albums.append((tuple(tup1), tuple(tup2)))
        except IndexError:
            pass
    return albums


def add_album(albums):  # 1
    author = input("Author: ")
    tittle = input("Album name: ")
    year = input("From year: ")
    genre = input("Genre: ")
    lenght = input("Lenght, in format min:sec: ")
    tup1 = ()
    tup2 = ()
    tup1 = author, tittle
    tup2 = year, genre, lenght
    albums.append((tup1, tup2))
    with open("music.csv", 'w', newline='') as musicfile:
        spamwriter = csv.writer(musicfile, delimiter='|')
        for row in albums:
            spamwriter.writerow([row[0][0]]+[row[0][1]]+[row[1][0]]+[row[1][1]]+[row[1][2]])
    print("""Added a new album.
                                """)


def find_by_artist(albums):  # 2
    Find = False
    artist_name = input("Write artist: ")

    for row in albums:
        if artist_name.lower() in row[0][0].lower():
            Find = True
            break
    if Find is True:
            print('Author:', row[0][0])
            print('Album:', row[0][1])
            print(" ")
    else:
        print("There is no albums with artist: ", artist_name)
        print(" ")


def find_by_year(albums):  # 3

    Find = False
    while True:
        try:
            year = int(input("Write year of album: "))
            break
        except ValueError:
            print("Enter a number only! ")

    for row in albums:
        if year == row[1][0]:
            Find = True
    if Find is True:
        print('Author:', row[0][0])
        print('Album:', row[0][1])
        print('Year: ', row[1][0])
        print('Genre: ', row[1][1])
        print('Lenght: ', row[1][2])
        print('')
    else:
        print("There is no albums from year: ", year)
        print(" ")


def find_author_by_album(albums):  # 4
    Find = False
    alboom = input("Enter a album: ")
    for row in albums:
        if alboom.lower() == row[0][1].lower():
            Find = True
            break
    if Find is True:
        print("Author: ", row[0][0])
        print('Album: ', row[0][1])
        print(" ")
    else:
        print("There is no author. Try again ")
        print(" ")


def find_by_letter(albums):  # 5
    album_names = []
    Find = False
    letter = input("Enter a first letter: ")
    for row in albums:
        if letter in row[0][1]:
            album_names.append(row)
            Find = True
            break
    if Find is True:
        print("Author: ", row[0][0])
        print("Album: ", row[0][1])
        print(" ")
    else:
        print("There is no albums with: ", letter)


def find_by_genre(albums):  # 6
    Find = False
    genre = input("Enter a genre: ")
    for row in albums:
        if genre == row[1][1]:
            Find = True
            break
    if Find is True:
        print("Author: ", row[0][0])
        print("Album: ", row[0][1])
        print(" ")
    else:
        print("Not found genre: ", genre)
        print(" ")


def count_the_years(albums):  # 7
    year = date.today().year
    for row in albums:
        calc_year = year - int(row[1][0])
        print('Album name: ', row[0][1], ",", end=' ')
        print('Years:', calc_year)


def random_album_by_genre(albums):  # 8
    list_of_genre = []
    Find = False
    genre = input("Enter a genre: ")
    for row in albums:
        if genre.lower() == row[1][1].lower():
            name_album = row[0][1]
            list_of_genre.append(name_album)
            Find = True
    if Find is True:
        random_alboom = random.choice(list_of_genre)
        print(random_alboom)
        print(" ")
    else:
        print("Not found genre: ", genre)
        print(" ")


def main():

    while True:
        print("""Welcome in the CoolMusic! Choose the action:
1. Add new album
2. Find albums by artist
3. Find albums by year
4. Find musician by album
5. Find albums by letter(s)
6. Find albums by genre
7. Calculate the age of all albums
8. Choose a random album by genre""")

        main_answer = input("Type your actions, from 1 to 10: ")

        list_actions = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

        albums = []
        read_the_file(albums)

        if main_answer == "1":
            add_album(albums)
        if main_answer == "2":
            find_by_artist(albums)
        if main_answer == "3":
            find_by_year(albums)
        if main_answer == "4":
            find_author_by_album(albums)
        if main_answer == "5":
            find_by_letter(albums)
        if main_answer == "6":
            find_by_genre(albums)
        if main_answer == "7":
            calculate_year(albums)
        if main_answer == "8":
            random_album_by_genre(albums)


if __name__ == '__main__':
    main()
