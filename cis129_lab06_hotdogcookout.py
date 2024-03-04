DOGS = 10
BUNS = 8

attendees = int( input( "Please enter the number of people attending the cookout" ))

hotDogsEach = int( input( "Please enter the number of hot dogs each of the " + str( attendees ) +  
" people is going to get" ) )

DOGSNeeded = attendees * hotDogsEach
BUNSNeeded = DOGSNeeded

exactHotDog = DOGSNeeded / DOGS
exactHotDogBun = BUNSNeeded / BUNS

hotDogRemainder = DOGSNeeded % DOGS
BunsRemainder = BUNSNeeded % BUNS

if hotDogRemainder > 0:
    minDogs = int( exactHotDog + 1 )
else: 
    minDogs = exactHotDog

    if BunsRemainder > 0:minBuns = int( exactHotDogBun + 1 )
    else: minBuns = exactHotDog

    dogsLeft = minDogs - exactHotDog
    bunsLeft = minBuns - exactHotDogBun

    print( "\nMininum number of packages of hot dogs required" + str( minDogs ) + "\nMininum number of packages of hot dogs buns required" \
    " of hot dogs buns required: " + str( minBuns) + "\nHot dogs left over: " + str( dogsLeft ) + "\nThe number of hot dog buns that will be left over: "+ str( bunsLeft) )
