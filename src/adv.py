from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].go_North = room['foyer']
room['foyer'].go_South = room['outside']
room['foyer'].go_North = room['overlook']
room['foyer'].go_East = room['narrow']
room['overlook'].go_South = room['foyer']
room['narrow'].go_West = room['foyer']
room['narrow'].go_North = room['treasure']
room['treasure'].go_South = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayerObject = Player('player1', room['foyer'])
# print(newPlayerObject.room)
# print("\n You find yourself in the " + newPlayerObject + ".")
print('Sunlight streaming onto your face wakes up, your head hurts.  Where are you?')
# print("\n Enter a Cardinal Direction to move in that direction.")
choice = str(input('\n Press Enter to Begin \n'))
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
    print("\n You find yourself in the " + newPlayerObject.currentRoom.name + ".")
    choice = input("\n What Direction to go in? (N,S,E,W): \n").lower()
    print(newPlayerObject.currentRoom)

    # print("S "+str(hasattr(newPlayerObject.room, 'go_South')))
    # print("N "+str(hasattr(newPlayerObject.room, 'go_North')))
    # print("E "+str(hasattr(newPlayerObject.room, 'go_East')))
    # print("W "+str(hasattr(newPlayerObject.room, 'go_West')))

    if choice == 'n':
        if hasattr(newPlayerObject.currentRoom, 'go_North'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_North
            print('\n You walk to the north, and arrive at the ' + newPlayerObject.currentRoom.name + '. \n')
            print(newPlayerObject.currentRoom.description + '\n')
            print("What do we do now?")
        else:
            print('\n Nothing to see here. We should look elsewhere.')
    elif choice == 's':
        if hasattr(newPlayerObject.currentRoom, 'go_South'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_South
            print('\n You walk to the south, and arrive at the ' + newPlayerObject.currentRoom.name + '. \n')
            print(newPlayerObject.currentRoom.description + '\n')
        else:
            print('\n Nothing to see here. We should look elsewhere.')
    elif choice == 'e':
        if hasattr(newPlayerObject.currentRoom, 'go_East'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_East
            print('\n You walk to the east, and arrive at the ' + newPlayerObject.currentRoom.name+ '. \n')
            print(newPlayerObject.currentRoom.description + '\n')
        else:
            print('\n Nothing to see here. We should look elsewhere.')
    elif choice == 'w':
        if hasattr(newPlayerObject.currentRoom, 'go_West'):
            newPlayerObject.currentRoom = newPlayerObject.currentRoom.go_West
            print('\n You walk to the west, and arrive at the ' + newPlayerObject.currentRoom + '. \n')
            print(newPlayerObject.currentRoom.description + '\n')
        else:
            print('\n Nothing to see here. We should look elsewhere.')
    else:
        print("Please Enter a Valid Direction, or enter Q to Quit.")

print('\n Thanks for playing! \n')