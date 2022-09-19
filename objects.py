from object import Obj

objs = {}

# lcode, title = "", desc = "", location = "", alts = "", pickup = False

objs["LANTERN"] = Obj("LANTERN","Brass lantern",
    "An old brass lantern. Actually it's a cheap modern version, it requires batteries and has a garish white LED glow. It is off.",
    "RIVERBANK",
    "lantern,brass lantern,lamp,test thing",
    True
)
objs["LANTERN"].o["on"] = False

objs["DARKRIVER"] = Obj("DARKRIVER","A dark river",
    "The river is deep and impossible to ford or swim.",
    "RIVERBANK",
    "river,dark river",
    False
)
