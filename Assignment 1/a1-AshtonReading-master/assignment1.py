"""
Replace the contents of this module docstring with your own details.
"""


def main():
    print("Songs To Learn 1.0 - by Ashton Reading")

    songs_file = open("songs.csv", "r")
    print("{} songs loaded".format(len(songs_file.readlines())))

    print("Menu")
    print("L - List songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            song_list = songs_file.readlines()
            print(song_list)




# if __name__ == '__main__':
main()
