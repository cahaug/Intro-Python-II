class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return 'Item Name: ' + self.name + '\n Item Description: ' + self.description
    def examine(self):
        return f'You see the {self.name}.  It is {self.description}'