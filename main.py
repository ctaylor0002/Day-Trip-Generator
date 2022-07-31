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


locations = ["Boston", "New York City", "Pittsburgh", "Washington DC", "Salem", "Hartford", "Portland"]
transportation = ["Train", "Plane", "Car", "Bus", "Uber", "Boat"]

#The list of resturants will have a list of lists
#I will add 3 locations to each list. If the user declines all three I will have a basic Fast Food list to accomadate
resturants = [["Maggiano's Little Italy", "Bostonia Public House", "Boston Sail Loft"],
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
