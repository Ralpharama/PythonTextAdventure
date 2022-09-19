from ast import parse
import json
import filehandler
import funcs
from highlevel import do_high_level
from location import Location   # location class
from locations import locs
from lowlevel import do_low_level      # locations and their states
from objects import objs        # objects in the game
from gamestate import gm        # flags an in game state vars
from texthandler import Parser  # handles input and parsing verbs, nouns etc

print("Welcome to Escape From Tulakon. A text adventure game written in python.")
print("Type 'help' for guidance on how to play.")
print("")

playing = True
parser = Parser()
locs[gm["CURLOC"]].display_desc(gm,objs)

while playing:
    # process high-level pre-sentence things (todo:)
    do_high_level(gm,objs)

    # check if we died
    if not gm["ALIVE"]:
        playing = False
        funcs.do_death()
        break

    # get input and parse it
    sentence = input("What now? > ")
    vlist = parser.parse_verbs(sentence)
    olist = parser.parse_objs(sentence,objs)

    # if we have a verb
    if vlist:

        # low level (specifics in location) things
        cont = do_low_level(gm,vlist,olist,objs)

        # process sentence
        while cont:

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
                locs[gm["CURLOC"]].display_desc(gm,objs)
                break

            # check room-specifc rules (todo:)

            # generic movement
            if vlist["NORTH"] or vlist["EAST"] or vlist["SOUTH"] or vlist["WEST"] or vlist["UP"] or vlist["DOWN"] or vlist["INSIDE"] or vlist["OUTSIDE"]:
                rm = locs[gm["CURLOC"]].go_direction(vlist)
                if rm:
                    gm["CURLOC"] = rm
                    locs[gm["CURLOC"]].display_desc(gm,objs)
                else:
                    print("You can't go that way.")
                break

            # take
            if vlist["TAKE"]:
                funcs.take_obj(gm,olist,objs)
                break

            # drop
            if vlist["DROP"]:
                funcs.drop_obj(gm,olist,objs)
                break

            # examine
            if vlist["EXAMINE"]:
                funcs.examine_obj(gm,olist,objs)
                break

            # inv
            if vlist["INV"]:
                funcs.display_inv(gm,objs)
                break

            # generic look
            if vlist["LOOK"]:
                locs[gm["CURLOC"]].display_desc(gm,objs)
                break

            # end processing sentence
            print("I don't understand.")
            break

        # process after sentence things (todo:)

    else:
        print("I don't understand.")

print("Thanks for playing!")


