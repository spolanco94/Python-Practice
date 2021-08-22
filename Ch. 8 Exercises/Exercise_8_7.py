# Write a function called make_album() that builds a dictionary descirbing an
# album. Take in an artist name, title, and make 3 dictionaries representing
# different albums. Use 'None' to add an optional parameter for the # of songs

def make_album(title, artist, year, status, songs= None):
    """Creates a dictionary of an album"""

    album = {
        "title" : title,
        "artist" : artist,
        "year" : year,
        "status" : status,
    }
    if songs == None:
        album.setdefault("tracks", "N/A")

    return album

kod = make_album(title= "KOD", artist= "J. Cole", year= "2018", status=
"platinum")
yhlqmdlg = make_album(title= "YHLQMDLG", artist= "Bad Bunny", year= "2020",
status= "Gold", songs= "20")
blonde = make_album(title= "Blonde", artist= "Frank Ocean", year= "2016",
status= "Platinum", songs= "17")

print(kod)
print(yhlqmdlg)
print(blonde)
