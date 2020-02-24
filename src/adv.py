from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    '1':  Room("in the center of the room", """A tattered rug adorns the floor.  I clasp my throbbing head.  Where am I?  What happened?  I can't remember.  This is scaring me, where am I, Where am I, WHERE AM I?""", [Item('dirty_shirt', 'Laundry that is dirty lying on the floor'), Item('black_hoodie', 'a standard black hoodie')]),

    '2':  Room("by a dresser", """Dim light filters in from the east. I wonder what is in this sleek chest of drawers here."""),

    '3':  Room("by a window", """In the bottom half of the window: the city at night-- twinkling lights flickering in the darkness. The tops of buildings. I'm on a high floor, but how did I get here? All I remember is being back at the diner and sipping my coffee.  How did I even get here?"""),

    '4':   Room("at the bed", """A soft spot for someone to rest their weary eyes, but not me.  I have to find out why I am here, and how to get back to where I came from."""),

    '5':   Room("by a black backpack leaning against the wall", """A black, open-mouthed Jansport is propped up, leaning against the wall.  I wonder what's inside."""),

    '6':   Room("by a desk", """The bright shine of a login screen on a laptop illuminates the black Ikea desk in front of you.  The text screen on the screen says that this is Mr_Robot's MacBook.  Mr_Robot.  I wonder who that is.""", [Item('doorkey', 'The key that opens the door to end the simulation')]),

    '7':   Room("at the refrigerator", """Wow.  A refrigerator, and it's full.  What is going on here?"""),

    '8':   Room("at the door", """Amazing.  A door.  Curses! It's locked, and a deadbolt at that. This will take a key to open.  A key, I wonder where I could find one?"""),

    '9':   Room("in the kitchen", """A very modern stove, marble countertops.  Rent on this place must cost a fortune! There's a bowl on the counter."""),

    '10':   Room("outside", """The key successfully opened the door. I escaped, and now am free.  Congratulations, I have won the game. And you player, you have just lost the game."""),
}

# Map of all of the rooms/possible moves
#  -------------------------------- DOOR (10) ------
# |    9    <->       7        <->        8         |
# | kitchen          <->                 <->        |
# |   5 bp  <->       1        <->        6   desk  |
# |  <->             <->                 <->        |
# |   4     <->       2        <->        3         |
# |  bed           dresser              window      |
#  -------------------------------------------------

# Link rooms together
room['1'].go_North = room['7']
room['1'].go_South = room['2']
room['1'].go_East = room['6']
room['1'].go_West = room['5']
room['2'].go_North = room['1']
# room['2'].go_South = NONE
room['2'].go_East = room['3']
room['2'].go_West = room['4']
room['3'].go_North = room['6']
# room['3'].go_South = NONE
# room['3'].go_East = NONE
room['3'].go_West = room['2']
room['4'].go_North = room['5']
# room['4'].go_South = NONE
room['4'].go_East = room['2']
# room['4'].go_West = NONE
room['5'].go_North = room['9']
room['5'].go_South = room['4']
room['5'].go_East = room['1']
# room['5'].go_West = NONE
room['6'].go_North = room['8']
room['6'].go_South = room['3']
# room['6'].go_East = NONE
room['6'].go_West = room['1']
# room['7'].go_North = NONE
room['7'].go_South = room['1']
room['7'].go_East = room['8']
room['7'].go_West = room['9']
# room['8'].go_North = room['10']
room['8'].go_South = room['6']
# room['8'].go_East = NONE
room['8'].go_West = room['7']
# room['9'].go_North = NONE
room['9'].go_South = room['5']
room['9'].go_East = room['7']
# room['9'].go_West = NONE


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayerObject = Player('player1', room['1'], [Item('id card', '''a New York state issued identification card for Elliot Alderson.  Maybe that's my name.'''), Item('money roll', '''A roll of $100 bills, almost an inch in diameter.  What have I been up to?''')])
# print(newPlayerObject.currentRoom)
# print("\n You find yourself in the " + newPlayerObject + ".")
print('Sunlight streaming onto your face wakes up, your head hurts.  Where are you?')
# print("\n Enter a Cardinal Direction to move in that direction.")
choice = str(input('Press Enter to Begin')).lower().split()
# print(choice)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while choice != ['q']:
    print("You are " + newPlayerObject.currentRoom.name + ".")
    choice = input("What Direction to go in? (N,S,E,W, help): ").lower().split()
    # print(newPlayerObject.currentRoom)
    # print(choice)

    # print("S "+str(hasattr(newPlayerObject.room, 'go_South')))
    # print("N "+str(hasattr(newPlayerObject.room, 'go_North')))
    # print("E "+str(hasattr(newPlayerObject.room, 'go_East')))
    # print("W "+str(hasattr(newPlayerObject.room, 'go_West')))

    if choice[0] == 'n' and newPlayerObject.currentRoom == room['8']:
        print("""There's a door here, but it's locked.  It looks like I need to use a key.""")
    elif choice[0] == 'unlock' and choice[1] == 'door' and newPlayerObject.currentRoom == room['8']:
        for item in newPlayerObject.items:
            if item.name == 'doorkey':
                print('This key fits like a glove.  The lock begins to turn.')
                newPlayerObject.currentRoom = room['10']
                print('The door opens.')
                print('You are ' + newPlayerObject.currentRoom.name)
                print(newPlayerObject.currentRoom.description)
                choice = ['q']
            elif item.name != 'doorkey':
                print('')
            else:
                print("""I can't open this door without a key.""")
    elif choice[0] == 'n':
        if hasattr(newPlayerObject.currentRoom, 'go_North'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_North
            print('You walk to the north.')
            print(newPlayerObject.currentRoom.description)
        else:
            print("""Can't go North. There's a wall in my way.""")
    elif choice[0] == 's':
        if hasattr(newPlayerObject.currentRoom, 'go_South'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_South
            print('You walk to the south.')
            print(newPlayerObject.currentRoom.description)
        else:
            print("""Can't go South. There's a wall in my way.""")
    elif choice[0] == 'e':
        if hasattr(newPlayerObject.currentRoom, 'go_East'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_East
            print('You walk to the east.')
            print(newPlayerObject.currentRoom.description)
        else:
            print("""Can't go East. There's a wall in my way.""")
    elif choice[0] == 'w':
        if hasattr(newPlayerObject.currentRoom, 'go_West'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_West
            print('You walk to the west.')
            print(newPlayerObject.currentRoom.description)
        else:
            print("""Can't go West. There's a wall in my way.""")
    elif choice[0] == 'check' and choice[1] == 'pockets':
        # maps through all the items that the user is carrying
        for thing in newPlayerObject.items:
            print(thing.examine())
    elif choice[0] == 'look' and choice[1] == 'around':
        # maps through the items in a room using the Item(name, description).examine() method on the class
        for thing in newPlayerObject.currentRoom.items:
            # print(thing)
            print(thing.examine())
    elif choice[0] == 'pickup' or choice[0] == 'take' or choice[0] == 'get':
        for thing in newPlayerObject.currentRoom.items:
            if choice[1] == thing.name:
                # print(thing)
                newPlayerObject.items.append(thing)
                newPlayerObject.currentRoom.items.remove(thing)
                print(f'Successfully put {thing.name} in your pocket.')
            else:
                # print("Requested object not found in current room.")
                print('')
    elif choice[0] == "drop" or choice[0] == "remove":
        for thing in newPlayerObject.items:
            if choice[1] == thing.name:
                # print(thing)
                newPlayerObject.currentRoom.items.append(thing)
                newPlayerObject.items.remove(thing)
                print(f'Set down the {thing.name} in the {newPlayerObject.currentRoom.name}')
            elif choice[1] != thing.name:
                print('')
            else:
                print("An unheld object cannot be dropped.")
    elif choice[0] == 'examine':   
        for thing in newPlayerObject.items:
            if choice[1] == thing.name:
                print('This is '+ thing.name + ', ' + thing.description)
            elif choice[1] != thing.name:
                print('')
            else:
                print('')
    elif choice[0] == 'help': 
        print('\n \n \n Welcome to the Room. \n \n In this game, you will try to find the doorkey hidden somewhere and use it to escape this room. \n \n You can move directionally with the cardinal directions, "look around", "check pockets", "pickup/take/get [item]" to add an item \n to your pocket, "drop/remove [item]" from your pocket, and "examine [item]" to see the details on an item from your pocket. \n \n')
    else:
        print("Please Enter a Valid Direction, or enter Q to Quit.")

print('\n Thanks for playing! \n')