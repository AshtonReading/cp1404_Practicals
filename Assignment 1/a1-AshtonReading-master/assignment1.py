"""
Replace the contents of this module docstring with your own details.
"""


def main():
    print("Songs To Learn 1.0 - by Ashton Reading")

    songs_file = open("songs.csv", "r")
    number_of_songs = len(songs_file.readlines())
    print("{} songs loaded".format(number_of_songs))
    songs_file.close()

    songs_file = open("songs.csv", "r")
    song_master_list = songs_file.readlines()

    print(song_master_list)
    songs_file.close()
    print(song_master_list[0])

    song1 = song_master_list[0].split(",")

    print(song1[3])

    song_name, song_artist, song_year, completed = song_master_list[0].split(",")
    print(song_name, song_artist, song_year, completed)




    MENU = """
    Menu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            print(song_master_list)
            print(MENU)
            choice = input(">>> ").upper()




# if __name__ == '__main__':
main()
