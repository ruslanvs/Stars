x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars( incomingList ):
    for i in incomingList:
        accumulatedString = ""
        for j in range ( i ):
            accumulatedString += "*"
        print accumulatedString

draw_stars( x )

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

print"        -         "
print"----separation----"
print"        -         "

def draw_stars_and_characters( incomingList ):
    for i in incomingList:
        accumulatedString = ""
        if isinstance( i, int ):
            for j in range ( i ):
                accumulatedString += "*"
        elif isinstance( i, str ):
            for j in range( len( i ) ):
                accumulatedString += i[0].lower()
        print accumulatedString

draw_stars_and_characters( x )