class Playlist:

    def __init__(self):
        self.songs = []   

    def add_song(self):
        song = input("Enter song name to add: ")
        self.songs.append(song)
        print(f"'{song}' added to playlist.\n")

    def remove_song(self):
        song = input("Enter song name to remove: ")
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed from playlist.\n")
        else:
            print("Song not found in playlist.\n")

    def show_songs(self):
        if len(self.songs) == 0:
            print("Playlist is empty.\n")
        else:
            print("\n🎶 Your Playlist:")
            for i, song in enumerate(self.songs, start=1):
                print(f"{i}. {song}")
            print()


def main():
    my_playlist = Playlist()  

    while True:
        print("===== PLAYLIST MENU =====")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. Show Songs")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            my_playlist.add_song()
        elif choice == '2':
            my_playlist.remove_song()
        elif choice == '3':
            my_playlist.show_songs()
        elif choice == '4':
            print("Exiting playlist... 🎧")
            break
        else:
            print("Invalid choice! Try again.\n")


main()