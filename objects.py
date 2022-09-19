from object import Obj

objs = {}

# lcode, title = "", desc = "", location = "", alts = "", pickup = False

objs["LANTERN"] = Obj("LANTERN","Brass lantern",
    "An old brass lantern. Actually it's a cheap modern version, it required batteries and has a garish white LED glow.",
    "RIVERBANK",
    "lantern,brass lantern,lamp,test thing",
    True
)

objs["DARKRIVER"] = Obj("DARKRIVER","A dark river",
    "The river is deep and impossible to ford or swim.",
    "RIVERBANK",
    "river,dark river",
    False
)
