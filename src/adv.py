from room import Room
from player import Player

# Declare all the rooms

room = {
    '1':  Room("in the center of the room", """A tattered rug adorns the floor.  I clasp my throbbing head.  Where am I?  What happened?  I can't remember.  This is scaring me, where am I, Where am I, WHERE AM I?"""),

    '2':  Room("by a dresser", """Dim light filters in from the east. You pull open the dresser drawers."""),

    '3':  Room("by a window", """In the bottom half of the window: the city at night-- twinkling lights flickering in the darkness. The tops of buildings. I'm on a high floor, but how did I get here? All I remember is being back at the diner and sipping my coffee.  How did I even get here?"""),

    '4':   Room("at the bed", """A soft spot for someone to rest their weary eyes, but not me.  I have to find out why I am here, and how to get back to where I came from."""),

    '5':   Room("by a black backpack leaning against the wall", """A black, open-mouthed Jansport is propped up, leaning against the wall.  I wonder what's inside."""),

    '6':   Room("by a desk", """The bright shine of a login screen on a laptop illuminates the black Ikea desk in front of you.  The text screen on the screen says that this is Mr_Robot's MacBook.  Mr_Robot.  I wonder who that is."""),

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
# room['8'].go_North = NONE
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
newPlayerObject = Player('player1', room['1'])
# print(newPlayerObject.room)
# print("\n You find yourself in the " + newPlayerObject + ".")
print('Sunlight streaming onto your face wakes up, your head hurts.  Where are you?')
# print("\n Enter a Cardinal Direction to move in that direction.")
choice = str(input('Press Enter to Begin'))
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
while choice != "q":
    print("You are " + newPlayerObject.currentRoom.name + ".")
    choice = input("What Direction to go in? (N,S,E,W): ").lower()
    # print(newPlayerObject.currentRoom)

    # print("S "+str(hasattr(newPlayerObject.room, 'go_South')))
    # print("N "+str(hasattr(newPlayerObject.room, 'go_North')))
    # print("E "+str(hasattr(newPlayerObject.room, 'go_East')))
    # print("W "+str(hasattr(newPlayerObject.room, 'go_West')))

    if choice == 'n':
        if hasattr(newPlayerObject.currentRoom, 'go_North'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_North
            print('You walk to the north.')
            print(newPlayerObject.currentRoom.description)
        else:
            print("""Can't go North. There's a wall in my way.""")
    elif choice == 's':
        if hasattr(newPlayerObject.currentRoom, 'go_South'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_South
            print('You walk to the south.')
            print(newPlayerObject.currentRoom.description)
        else:
            print("""Can't go South. There's a wall in my way.""")
    elif choice == 'e':
        if hasattr(newPlayerObject.currentRoom, 'go_East'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_East
            print('You walk to the east.')
            print(newPlayerObject.currentRoom.description)
        else:
            print("""Can't go East. There's a wall in my way.""")
    elif choice == 'w':
        if hasattr(newPlayerObject.currentRoom, 'go_West'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_West
            print('You walk to the west.')
            print(newPlayerObject.currentRoom.description)
        else:
            print("""Can't go West. There's a wall in my way.""")
    else:
        print("Please Enter a Valid Direction, or enter Q to Quit.")

print('\n Thanks for playing! \n')