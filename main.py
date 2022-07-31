#(5 points): As a developer, I want to make at least three commits with descriptive messages.

#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists.

#(5 points): As a user, I want a destination to be randomly selected for my day trip.

#(5 points): As a user, I want a restaurant to be randomly selected for my day trip.

#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

#(10 points): As a user, I want to display my completed trip in the console.

#(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

#My first step will be to create 4 lists that will have pre determined locations, resturants, entertainment and transportation
#As well as establish a current location. This will just be a random location I pick
#I will be utilizing this information to help determine if certain methods of transportation are improbable and remove them from the current list


#startingLocation = "Springfield MA" This is probably unneccessary

import random
from tkinter.messagebox import YES
locations = ["Boston", "New York City", "Pittsburgh", "Washington DC", "Salem", "Hartford", "Portland"]
transportation = ["Train", "Plane", "Rental car", "Bus", "Uber"]

#The list of restaurants will have a list of lists
#I will add 3 locations to each list. If the user declines all three I will have a basic Fast Food list to accomadate
restaurants = [["Maggiano's Little Italy", "Bostonia Public House", "Boston Sail Loft"],
                ["STK Steakhouse Downtown NYC", "Boucherie Union Square", "Le Coucou"],
                ["Morton's The Steakhouse", "Eddie V's Prime Seafood", "The Capital Grille"],
                ["Benihana", "Founding Farmers DC", "Estadio"],
                ["Jade's Restaurant","Bambolina", "Adriatc Restaurant"],
                ["Bear's Smokehouse Barbecue", "Black-Eyed Sally's Southern Kitchen and Bar", "Vaughan's Public House"],
                ["Rick's Cafe", "Duckfat","Hot Suppa"]
]

entertainment = [["New England Aquarium", "Museum of Fine Arts", "Fenway Park"],
                    ["Central Park", "The Metropolitan Museum of Art", "Statue of Liberty"],
                    ["The Andy Warhol Museum", "Phipps Conservatory and Botanical Gardens", "Pittsburgh Zoo and PPG Aquarium"],
                    ["The White House", "Library of Congress","United States Capitol"],
                    ["Salem Witch Museum", "Salem Witch Trials Memorial","Salem Maritime National Historic Site"],
                    ["Connecticut Science Center", "The Mark Twain House and Museum", "Wadsworth Athenum Museum of Art"],
                    ["Portland Head Light", "Portland Museum of Art", "Peaks Island"]
]

def pickedLocation():
    acceptableLocation = False
    locationIndex = random.randrange(0,len(locations),1)
    location = locations[locationIndex]
    question = ''

    while acceptableLocation == False:
        if question == '':
            question = input(f"Your picked location for today is {location}. Is it okay? yes/no ")
        
        if question == 'yes':
            print(f"Awesome! Hope you have fun at {location}!")
            acceptableLocation == True
            return location
        elif question =='no':
            locations.pop(locationIndex)
            restaurants.pop(locationIndex)
            entertainment.pop(locationIndex)
            locationIndex = random.randrange(0,len(locations),1)
            location = locations[locationIndex]
            question = input(f"How about {location}? yes/no ")
        else:
            question = input('Invalid response. Try again. yes/no ')

def pickedTransportation():
    acceptableTransportation = False
    transportationIndex = random.randrange(0,len(transportation),1)
    transportationChk = transportation[transportationIndex]
    question = ''
    while acceptableTransportation == False:
        if question == '':
            question = input(f"Your picked method of transportation for today is {transportationChk}. Is this okay? yes/no ")
        
        if question == 'yes':
            print(f"Fantastic! Enjoy your {transportationChk} ride!")
            return transportationChk
        elif question == 'no': 
            transportation.remove(transportationChk)
            transportationIndex = random.randrange(0,len(transportation),1)
            transportationChk = transportation[transportationIndex]
            question = input(f"How about taking a {transportationChk}? yes/no ")
        else:
            question = input('Invalid response. Try again. yes/no ')


def pickedEntertainment(tripLocation):
    srchIndex = locations.index(tripLocation)
    entertainmentOptions = entertainment[srchIndex]
    entertainmentOption = random.randrange(0,len(entertainmentOptions),1)
    theEntertainmentOption = entertainmentOptions[entertainmentOption]
    question = ''
    acceptableEntertainment = False
   
    while acceptableEntertainment == False:
        if question == '':
            question = input(f"Your picked entertainment for the day is touring {theEntertainmentOption}. Is this okay? yes/no ")
        
        if question == 'yes':
            print(f"Perfect! Enjoy touring {theEntertainmentOption}!")
            return theEntertainmentOption
        elif question == 'no':
            entertainmentOptions.remove(theEntertainmentOption)
            srchIndex = random.randrange(0,len(entertainmentOptions),1)
            theEntertainmentOption = entertainmentOptions[srchIndex]
            question = input(f"How about touring {theEntertainmentOption}? yes/no ")
        else:
            question = input('Invalid response. Try again. yes/no ')

        
def pickedRestaurant(tripLocation):
    srchIndex = locations.index(tripLocation)
    restaurantOptions = restaurants[srchIndex]
    restaurantOption = random.randrange(0,len(restaurantOptions),1)
    theRestaurantOption = restaurantOptions[restaurantOption]
    question = ''
    acceptableRestaurant = False
    
    while acceptableRestaurant == False:
        if question == '':
            question = input(f"Your picked restaurant for the day is {theRestaurantOption}. Is this okay? yes/no ")
        
        if question == 'yes':
            print(f"Perfect! Enjoy eating at {theRestaurantOption}!")
            return theRestaurantOption
        elif question == 'no':
            restaurantOptions.remove(theRestaurantOption)
            srchIndex = random.randrange(0,len(restaurantOptions),1)
            theRestaurantOption = restaurantOptions[srchIndex]
            question = input(f"How about eating at {theRestaurantOption}? yes/no ")
        else:
            print("Invalid Response. Try again,")

def tripGeneration():
    locations = ["Boston", "New York City", "Pittsburgh", "Washington DC", "Salem", "Hartford", "Portland"]
    transportation = ["Train", "Plane", "Rental car", "Bus", "Uber"]

    #The list of restaurants will have a list of lists
    #I will add 3 locations to each list. If the user declines all three I will have a basic Fast Food list to accomadate
    restaurants = [["Maggiano's Little Italy", "Bostonia Public House", "Boston Sail Loft"],
                    ["STK Steakhouse Downtown NYC", "Boucherie Union Square", "Le Coucou"],
                    ["Morton's The Steakhouse", "Eddie V's Prime Seafood", "The Capital Grille"],
                    ["Benihana", "Founding Farmers DC", "Estadio"],
                    ["Jade's Restaurant","Bambolina", "Adriatc Restaurant"],
                    ["Bear's Smokehouse Barbecue", "Black-Eyed Sally's Southern Kitchen and Bar", "Vaughan's Public House"],
                    ["Rick's Cafe", "Duckfat","Hot Suppa"]
    ]

    entertainment = [["New England Aquarium", "Museum of Fine Arts", "Fenway Park"],
                        ["Central Park", "The Metropolitan Museum of Art", "Statue of Liberty"],
                        ["The Andy Warhol Museum", "Phipps Conservatory and Botanical Gardens", "Pittsburgh Zoo and PPG Aquarium"],
                        ["The White House", "Library of Congress","United States Capitol"],
                        ["Salem Witch Museum", "Salem Witch Trials Memorial","Salem Maritime National Historic Site"],
                        ["Connecticut Science Center", "The Mark Twain House and Museum", "Wadsworth Athenum Museum of Art"],
                        ["Portland Head Light", "Portland Museum of Art", "Peaks Island"]
    ]
    tripLocation = pickedLocation()
    tripTransportation = pickedTransportation()
    tripEntertainment = pickedEntertainment(tripLocation)
    tripRestaurant = pickedRestaurant(tripLocation)
    returnData = (tripLocation,tripTransportation,tripEntertainment,tripRestaurant)
    return returnData

generatedTrip = tripGeneration()
confirmation = False
print(f"The trip we have generated for you is as follows:\n Location: {generatedTrip[0]}\n Transportation: {generatedTrip[1]}\n Entertainment: {generatedTrip[2]}\n Restaurant: {generatedTrip[3]}")

while confirmation == False:
    question = input("Is this trip to your liking? yes/no ")
    if question == 'yes':
        print("Have fun at your trip today!!!")
        confirmation = True
    elif question == 'no':
        generatedTrip = tripGeneration()


