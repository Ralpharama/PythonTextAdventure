# things that happen specifc to a room

def do_low_level(gm,vlist,olist,objs):
    cont = True

    # lamp
    if vlist["ON"] and olist["LANTERN"]:
        if objs["LANTERN"].o["location"] == "SELF":
            if objs["LANTERN"].o["on"]:
                print("The lantern is already on.")
            else:
                objs["LANTERN"].o["on"] = True
                objs["LANTERN"].o["desc"] = objs["LANTERN"].o["desc"].replace("It is off","It is on")                
                print("You turn on the lantern.")
        else:
            print("Sadly, you don't have the lantern.")
        cont = False

    # rooms
    rm = gm["CURLOC"]

    if rm == "RIVERBANK":
        if (vlist["CROSS"] or vlist["SWIM"]) and olist["DARKRIVER"]:
            print("You drowned.")
            gm["ALIVE"] = False
            cont = False

    return cont
