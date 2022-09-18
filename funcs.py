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
