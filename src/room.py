# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.go_North = None
        self.go_South = None
        self.go_East = None
        self.go_West = None
    def __str__(self):
        return '\n Room Name: ' + self.name + '\n Description: ' + self.description