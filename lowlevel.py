# things that happen specifc to a room

def do_low_level(gm,vlist,olist,objs):
    cont = True
    rm = gm["CURLOC"]

    if rm == "RIVERBANK":
        if (vlist["CROSS"] or vlist["SWIM"]) and olist["DARKRIVER"]:
            print("You drowned.")
            gm["ALIVE"] = False
            cont = False

    return cont
