from ast import parse
import json
import filehandler
from location import Location   # location class
from locations import locs      # locations and their states
from objects import objs        # objects in the game
from gamestate import gm        # flags an in game state vars
from texthandler import Parser  # handles input and parsing verbs, nouns etc

print("Welcome to Escape From Tulakon. A text adventure game written in python.")
print("Type 'help' for guidance on how to play.")
print("")

playing = True
parser = Parser()

while playing:
    sentence = input("What now? > ")
    vlist = parser.parse_verbs(sentence)
    olist = parser.parse_objs(sentence,objs)

    if vlist:

        # process high-level pre-sentence things (todo:)

        # process sentence
        while True:

            # quit
            if vlist["QUIT"]:
                playing = False
                break

            # save
            if vlist["SAVE"]:
                filehandler.save_class("locs",locs)
                filehandler.save_class("objs",objs)
                filehandler.save_dict("gm",gm)
                print("Game saved.")
                break

            # load
            if vlist["LOAD"]:
                filehandler.load_class("locs",locs)
                filehandler.load_class("objs",objs)
                filehandler.load_dict("gm",gm)
                print(gm)
                locs[gm["CURLOC"]].display_desc()
                break

            # check room-specifc rules (todo:)

            # generic look
            if vlist["LOOK"]:
                locs[gm["CURLOC"]].display_desc(objs)
                break

            # generic movement
            if vlist["NORTH"] or vlist["EAST"] or vlist["SOUTH"] or vlist["WEST"] or vlist["UP"] or vlist["DOWN"] or vlist["INSIDE"] or vlist["OUTSIDE"]:
                rm = locs[gm["CURLOC"]].go_direction(vlist)
                if rm:
                    gm["CURLOC"] = rm
                    locs[gm["CURLOC"]].display_desc(objs)
                else:
                    print("You can't go that way.")
                break

            # generic take
            if vlist["TAKE"]:
                for ob in olist:
                    if olist[ob]:
                        if objs[ob].o["location"] == gm["CURLOC"]:
                            if objs[ob].o["pickup"]:
                                objs[ob].o["location"] = "SELF"
                                print("You pick up the %s." % objs[ob].o["title"])
                            else:
                                print("You can't take that.")
                        else:
                            print("I can't see that here.")
                break

            # end processing sentence
            print("I don't understand.")
            break

        # process after sentence things (todo:)

    else:
        print("I don't understand.")

print("Thanks for playing!")
