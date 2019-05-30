from room import Room
from player import Player
from item import Item

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

item = {
    "torch" :       Item("torch", "This will help you see in the dark"),
    "key"   :       Item("key", "An old rusty key"),
    "sword" :       Item("sword", "Old but still sharp"),
    "coin"  :       Item("coin", "Shiny!"),
    "brass key":    Item("brass key", "A brass key"),
    "dagger":       Item("dagger", "small and pointy"),
    "empty chest":  Item("empty treasure chest", "Looks like there used to be treasure here"),
    "map":          Item("map", "A map to the next treasure")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Put items in rooms
room['outside'].items = [item["torch"]]
room['foyer'].items = [item["key"], item["sword"]]
room['overlook'].items = [item["coin"], item["brass key"]]
room['narrow'].items = [item["dagger"]]
room['treasure'].items = [item["coin"], item["coin"], item["map"]]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("James", room["outside"].name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
def loopRoom():
    for i in room:
        if player.current_room == room[i].name:
            print(room[i].name)
            print(room[i].description)
            for x in room[i].items:
                print(f"\nYou see a {x.name}: {x.description}")
            return room[i]

def loopMove(current_room, move):
    moving = move + "_to"
    next_room = getattr(current_room, moving)
    player.current_room = next_room.name
    print("Invalid Entry")
    return player

def start():
    while True:
        start_location = loopRoom()
        cmd = input("\n Choose a direction: [n] North, [e] East, [s] South, [w] West:  ")
        if cmd == "q":
            print("Game Over!")
            break
        elif cmd == "n" or cmd == "e" or cmd == "s" or cmd == "w":
            try:
                loopMove(start_location, cmd)
            except AttributeError:
                print("Cannot go that direction")
        elif cmd == "take":
            try:
                for x in ro
        else:
            print("Invalid Command")

start()

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
