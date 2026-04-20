playlist = {}

while True:
    print("\n your playlist manager: \n")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. View Playlist")
    print("4. Search Song")
    print("5. Exit")

    choice = input(" Enter your choice: ")

    if choice == "1":
        title = input("Enter the song title: ").strip()
        artist = input("Enter the artish name: ").strip()
        if title in playlist:
            print("Song already exist in playlist: ")
        else:
            playlist[title] = artist
            print(f"added {title} of {artist} in playlist")
    elif choice == '2':
        title = input("Enter the song title to delete: ").strip()
        if title in playlist:
            del playlist[title]
        else:
            print("Song not present in playlist")
    elif choice == '3':
        if playlist:
            for song,artist in playlist.items():
                print(f"- {song} by {artist}")
        else:
            print("Playlist Empty")
    elif choice == '4':
        title = input("Enter the song title : ").strip()
        if title in playlist:
            print(f"{title} present in playlist", playlist[title])
        else:
            print("Song not available")
    elif choice == '5':
        print("Serch is over, Thanks for Playlist search, bye bye ")
        break
    else:
        print("Press valid key, please enter number tetween 1 to 5")

    


