def song_decoder(song):
    song=song.replace("WUB"," ")
    song=song.split(" ")
    song[:]=[x for x in song if x!=""]
    return " ".join(song)