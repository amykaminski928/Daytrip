destination_list=["Vancouver, British Columbia", "Tucson, AZ", "Kalamazoo, MI", "Eugene, OR", "Edinburgh, Scotland","Rome, Italy"]
transportation_list=["Greyhound Bus", "Flying Car", "Comercial Flight", "Private Jet", "Personal vehicle", "Motorcycle", "RV", "Rental Car", "Teleportation", "Train"]
activities_list=["playing golf", "visiting the art museum", "taking a bus tour", "skiing", "hiking", "shopping", "visiting the zoo", "watching a play", "watching a sporting event", "taking a photo safari"]
dining_list=["McDonald's", "Seafood", "Steak", "Mexican", "Italian", "Diner", "Sushi", "Pizza"]
# vancouver_activities=["whale watching", "hiking Grouse Mountain", "taking a seaplane tour", "touring Victoria Gardens", "skiing or snowborading Whistler", "shopping at Granville Island Market", "visiting Vancouver Aquarium", "viewing the Museum of Anthropology at the University of British Columbia", "playing golf at Stanley Park", "browsing local art at Pacific Arts Market", "going to a Canucks game at Rogers Arena"]
# tucson_activities=["hiking Sabino Canyon", "visiting the Sonoran Desert Museum", "visiting Pima Air and Space Museum", "feeding giraffes at Tucson Zoo", "travelling back in time at Old Tucson Studios", "watch a production at University of Arizona", "renting videos at Casa Video", "watching a play at Little Anthony's Diner", "touring San Xavier del Bac Mission", "golfing at a top resort"]
# Kalamazoo_activities=["touring Western Michigan University", "visiting Kalamazoo Valley Museum", "watching a concert at Kalamazoo State Theater", "watching a Kalamazoo Growlers baseball game", "picking apples at Verhage Fruit Farm and Cider Mill", "plant shopping at River Street Flowerland"]
# Eugene_activities=["visiting Cascades Raptor Center", "watching an opera at the Hult Center", "shopping at the Saturday Market", "hiking the Skinner Butte", "viewing the Owen Rose Garden", "listening to a concert at the Cuthbert Ampitheater", "shopping at the Fifth Street Public Market", "viewing at Maude Kerns Art Center", "visiting Cascades Raptor Center"]
# Edinburgh_activities=["following a guided tour of Edinburgh Castle", "visiting National Museum of Scotland", "walking Edinburgh Old Town", "watching the Royal Edinburgh Tatoo", "touring the Incholm Abbey and Island", "taking high tea at Royal Gardens", "golfing at St.Andrews"]
# Rome_activities=["kissing the Pope's ring", "touring the Vatican", "breaking the DaVinici code", "fighting tigers in the Colosseum", "learning to make pasta", "visiting Pompei", "throwing coins in Trevi Fountain", "driving a Vespa on a tour"]
# vancouver_dining_list=["Elisa (Steakhouse)","Miku (Sushi)", "Savio Volpe (Italian)", "Le Crocodile (French)", "Joe Fortes (Seafood)", "Cioppino's (Italian)", "Botanist (Sustainable)", "Loula's (Greek)","The Templeton (Diner)", "Pho Goodness (Vietnamese)"]
# tucson_dining_list=["El Nidito (Mexican)","El Charo (Mexican)", "Kingfisher (Cajun)","Zemam's Too (Ethiopian)", "Ruiz Hot Dogs Los Chipilones (Sonoran Hot Dogs)", "El Corral (Steakhouse)", "Tumerico (Vegan Mexican)", "Tooley's Cafe (American)", "PY Steakhouse (Steakhouse)", "Little Anthony's Diner (Diner)"]
# kalamazoo_dining_list=["Hop Cat (Brewpub)", "Zooroona (Middle Eastern)", "Kalamazoo Beer Exchange (Brewpub)","Food Dance Cafe (Cafe)","Bell's Eccentric Cafe (Brewpub)", "Principle Food and Drink (Farm to table)", "Theo and Stacy's (American/Greek/Vegan)", "Bold (Seafood and Steak)"]
# eugene_dining_list=["Cornbread Cafe (Vegan)","Sweet Life Patisserie (Cafe)", "Ambrosia (wood-fired)", "Hot Mamas Wings (BBQ)", "Chapala Mexican Restaurant", "Cornucopia (Pub)", "Ninkasi Brewing Company (Brewpub)"]
# edinburgh_dining_list=["Aizle (Bistor)", "Fhior (Scandi)", "Aurora (Bistro)", "Timberyard (local)", "The Little Chartroom (Bistro)", "Cafe St Honore (French)", "LeftField (neighborhood)", "The Table (exclusive)"]
# rome_dining_list=["DOC Crudeteria Eno Bistro (Pizza)", "El Pizzicarlo (Itialian)", "Stephano of Rome (Italian)","Bono Bottega Nostrana - San Pietro (Bar)", "Assunta Madre (Seafood)", "Vulio (Sandwiches)"
# "Bufalero (Italian-American)", "That's Amore Barbecue Boccea (American Brew Pub)", "Rame Sushi Naturale Italiano (Seafood Fusion)"]
print ("Not sure where to go on your next vacation? Perfect, you have landed exactly where you need to be.")
import random

def random_destination (destination_list):
    global question
    global random_destination_choice
    random_destination_choice = random.choice(destination_list)
    print('Would you like to visit {}?'.format(random_destination_choice))
    question= input ("Please answer y or n")
random_destination_picked=random_destination(destination_list)
user_input = True
affirm= "Wonderful choice. Let's continue planning your trip."
negative= "No problem, let's try again."

#destination selection loop:
def user_prompt(): 
    global random_destination_picked
    global random_destination_choice
    global user_input
    global question    
    while user_input == True:
        if question == 'y':
            user_input =False
            print (f"Wonderful choice, you will be traveling to {random_destination_choice}")
        else:
            user_input= True
            print(negative)
            random_destination_picked=random_destination(destination_list)
            
           
destination_confirm=user_prompt()

#transportation selection loop   
def random_transporation (transportation_list):
    global question
    global random_transportation_choice
    random_transportation_choice = random.choice(transportation_list)
    print(f"Would you like to travel by {random_transportation_choice}?")
    question= input ("Please answer y or n")
random_transportation_picked=random_transporation (transportation_list)

user_input = True
       
def choose_transport():
    global random_transportation_choice
    global random_transportation_picked
    global user_input
    global question
    while user_input == True:
        if question == 'y':
            user_input =False
            print (f"Wonderful, you will be traveling by {random_transportation_choice}.")
        else:
            user_input= True
            print(negative)
            random_transportation_picked=random_transporation(transportation_list)

transport_confirmed=choose_transport()
#activity selection loop
def random_activity (activities_list):
    global random_activity_choice
    global question
    random_activity_choice = random.choice(activities_list)
    print(f"Would you like to spend your day {random_activity_choice}?")
    question= input ("Please answer y or n")

random_activity_picked=random_activity (activities_list)

user_input = True
       
def choose_activity():
    global random_activity_choice
    global random_activity_picked
    global user_input
    global question
    while user_input == True:
        if question == 'y':
            user_input =False
            print (f"You will have fun all day while {random_activity_choice}.")
        else:
            user_input= True
            print(negative)
            random_activity_picked=random_activity (activities_list)

activity_confirmed=choose_activity()
#Dining selection loop
def random_dining (dining_list):
    global random_dining_choice
    global question
    random_dining_choice = random.choice(dining_list)
    print(f"Would you like to have {random_dining_choice} for dinner?")
    question= input ("Please answer y or n")

random_dinner_picked=random_dining (dining_list)

user_input = True
       
def choose_dinner():
    global random_dining_choice
    global random_dinner_picked
    global user_input
    global question
    while user_input == True:
        if question == 'y':
            user_input =False
            print (f"You have planned a wonderful day trip that will end with a {random_dining_choice} dinner.")
        else:
            user_input= True
            print(negative)
            random_dinner_picked=random_dining (dining_list)

dinner_confirmed=choose_dinner()
#review choices
print("As a last step please review your options: ")
print(f"Your adventure awaits as you travel by {random_transportation_choice} to {random_destination_choice}.  Once you arrive you will enjoy a day of {random_activity_choice} and end your day with a delicious {random_dining_choice} dinner!  Bon Voyage!")

