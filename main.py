from enum import Enum
import json
from location import Location
from locations import locs
from texthandler import Parser

class GameState(Enum):
    ALIVE = True
    DEAD = False


print("Welcome to Escape From Kontula. A text adventure game written in python.")
print("Type 'help' for guidance on how to play.")
print("")

gameState = GameState.ALIVE
cur_location = "ILANOTERRACE"
parser = Parser()

while gameState == GameState.ALIVE:
    sentence = input("What now? > ")
    vlist = parser.parse(sentence)

    if vlist:

        # process high-level pre-sentence things (todo:)

        # process sentence
        while True:

            # quit, load, save etc
            if vlist["QUIT"]:
                gameState = GameState.DEAD
                break

            if vlist["SAVE"]:
                with open('locs.json', 'w') as f:
                    f.write("[")
                    count = 0
                    for l in locs:
                        json.dump(locs[l].o, f)
                        count += 1
                        if count != len(locs): f.write(",")
                    f.write("]")
                break

            if vlist["LOAD"]:
                f = open('locs.json')
                tmplocs = json.load(f)
                #print(tmplocs)
                for l in tmplocs:
                    lcode = l["lcode"]
                    print(lcode)
                    #locs[lcode] = Location(lcode)
                    for attrib in l:
                        locs[lcode].o[attrib] = l[attrib]
                    print(locs[lcode])

            # check room-specifc rules (todo:)

            # generic look
            if vlist["LOOK"]:
                locs[cur_location].display_desc()
                break

            # generic movement
            if vlist["NORTH"] or vlist["EAST"] or vlist["SOUTH"] or vlist["WEST"] or vlist["UP"] or vlist["DOWN"] or vlist["INSIDE"] or vlist["OUTSIDE"]:
                rm = locs[cur_location].go_direction(vlist)
                if rm:
                    cur_location = rm
                    locs[cur_location].display_desc()
                else:
                    print("You can't go that way.")
                break

            # end processing sentence
            break

        # process after sentence things (todo:)

    else:
        print("I don't understand.")

print("Thanks for playing!")
