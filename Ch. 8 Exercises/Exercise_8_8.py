# Create a while loop that allows users to enter album info. Then call
# make_album() and print the dictionary created. Include a 'quit' value. 

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

flag = True
print("Hello, please tell me the information about the album you wish to store."
"\nYou may quit at any time by entering 'q'.")
while flag:
    title = input("What is the album title? ")
    if title.lower() == 'q':
        break
    artist = input("Who was the artist? ")
    if artist.lower() == 'q':
        break
    year = input("What year was the album released? ")
    if year.lower() == 'q':
        break
    status = input("What is the certification of the album? ")
    if status.lower() == 'q':
        break
    songs = input("How many tracks are on the album? ")
    if songs.lower() == 'q':
        break
    flag = False

    #### Add functionality to store multiple albums in a list
    # cont = input("Would you like to enter information about another album? "
    # "(y/n) ")
    # if cont.lower() == 'n':
    #     flag = False

album = make_album(title, artist, year, status, songs)
print(album)