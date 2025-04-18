def get_all_data():
    FILENAME = "Pink_Floyd_DB.txt"
    FIRST_EMPTY = 1
    MAX_USEFUL_DATA_INDEX = 4
    MIN_USEFUL_DATA_INDEX = 2
    FIRST_INDEX = 0

    file = open(FILENAME, "r")  # open file for reading
    file_data = file.read()  # read whole file to string
    file.close()

    albums_dict = {}
    song_dict = {}
    albums_amount = len(file_data.split("#"))

    # this loop goes through all the albums and puts them in a dict as key, and as value puts another dict, and in the
    # other dict the keys are the songs name from the album and the values are lists that includes the length and words
    for i in range(FIRST_EMPTY, albums_amount):
        album_songs_amount = len(file_data.split("#")[i].split("*"))
        current_album = (file_data.split("#")[i]).split("\n")[FIRST_INDEX].split("::")[FIRST_INDEX]
        for t in range(FIRST_EMPTY, album_songs_amount):
            song_name = file_data.split("#")[i].split("*")[t].split("\n")[FIRST_INDEX].split("::")[FIRST_INDEX]
            song_details = []
            for k in range(MIN_USEFUL_DATA_INDEX, MAX_USEFUL_DATA_INDEX):
                song_details.append(file_data.split("#")[i].split("*")[t].split("::")[k])
            song_dict[song_name] = song_details
        albums_dict[current_album] = song_dict
        song_dict = {}

    return albums_dict


def answer1():
    return ", ".join(get_all_data().keys())


def answer2(album_name):
    return ", ".join(get_all_data()[album_name].keys())


def answer3(song_name):
    song_len = 0

    # goes through the albums and finds the right song and saves its length
    for val in get_all_data().values():
        for song in val.keys():
            if song == song_name:
                song_len = val[song][0]

    return song_len


def answer4(song_name):
    song_lyrics = 0

    # goes through the albums and finds the right song and saves its lyrics
    for val in get_all_data().values():
        for song in val.keys():
            if song == song_name:
                song_lyrics = val[song][1]

    return song_lyrics


def answer5(song_name):
    song_album = 0

    # goes through the albums and finds the right song and saves its album
    for key, val in get_all_data().items():
        current_album = key
        for song in val.keys():
            if song == song_name:
                song_album = current_album

    return song_album


def answer6(word):
    songs_word = []

    # goes through the albums and checks if the word appears in the song name and appends to a list if it does
    for val in get_all_data().values():
        for song in val.keys():
            if word.lower() in song.lower():
                songs_word.append(song)

    if len(songs_word) > 1:
        return ", ".join(songs_word)
    else:
        return "".join(songs_word)


def answer7(word):
    songs_lyrics_word = []

    # goes through the albums and checks if the word appears in the song lyrics and appends the song name to a list if they does
    for val in get_all_data().values():
        for song, details in val.items():
            if word.lower() in details[1].lower():
                songs_lyrics_word.append(song)

    if len(songs_lyrics_word) > 1:
        return ", ".join(songs_lyrics_word)
    else:
        return "".join(songs_lyrics_word)
