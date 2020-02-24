# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description, items=[Item('E-Corp Employee RFID Keycard', """An identification card belonging to an Angela Moss.  I wonder who that is!""")]):
        self.name = name
        self.description = description
        self.items = items
        # self.go_North = None
        # self.go_South = None
        # self.go_East = None
        # self.go_West = None
    def __str__(self):
        output = f'Room Name: {self.name} \n Description: {self.description} Items: '
        for thing in enumerate(self.items):
            # output += f'{thing.name}, {thing.description}, '
            output += f'{thing[1]}, '
        return output