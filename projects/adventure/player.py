class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
        self.done=[]
    def travel(self, direction, path, showRooms = False):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        print(f"from {self.currentRoom.id} to {nextRoom.id if nextRoom else 'None'}")
        if nextRoom is not None:
            self.done.append(direction)
            self.currentRoom = nextRoom
            if (showRooms):
                nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")
            print(f"data {self.currentRoom.id} heading {direction}")
            print(self.done)
            print(path)
            
