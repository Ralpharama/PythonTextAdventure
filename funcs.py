# useful things

# inv
def display_inv(gm,objs):
    inv_text = ""
    for ob in objs:
        if objs[ob].o["location"] == "SELF":
            inv_text += objs[ob].o["title"]
    if inv_text:
        if inv_text[-2:] == ", ": inv_text = inv_text[:-2]
        inv_text = "You are carrying " + inv_text + "."
    else:
        inv_text = "You have nothing."
    print(inv_text)

# take
def take_obj(gm,olist,objs):
    for ob in olist:
        if olist[ob]:
            if objs[ob].o["location"] == gm["CURLOC"]:
                if objs[ob].o["pickup"]:
                    objs[ob].o["location"] = "SELF"
                    print("You pick up the %s." % objs[ob].o["title"])
                else:
                    print("You can't take that.")
            elif objs[ob].o["location"] == "SELF":
                print("You already have that.")
            else:
                print("I can't see that here.")

# drop
def drop_obj(gm,olist,objs):
    for ob in olist:
        if olist[ob]:
            if objs[ob].o["location"] == "SELF":
                objs[ob].o["location"] = gm["CURLOC"]
                print("You drop the %s." % objs[ob].o["title"])
            else:
                print("You don't have that.")

# examine
def examine_obj(gm,olist,objs):
    for ob in olist:
        if olist[ob]:
            if objs[ob].o["location"] == "SELF" or objs[ob].o["location"] == gm["CURLOC"]:
                print("%s" % objs[ob].o["desc"])
            else:
                print("I don't see that.")





# death
def do_death():
    print("You are dead. Thanks for playing.")
