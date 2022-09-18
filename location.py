class Location:

    def __init__(self, lcode, title = "", desc = "", north = "", east = "", south = "", west = "", up = "", down = "", inside = "", outside = ""):
        self.o = {}
        self.o["lcode"] = lcode
        self.o["title"] = title
        self.o["desc"] = desc
        self.o["north"] = north
        self.o["east"] = east
        self.o["south"] = south
        self.o["west"] = west
        self.o["up"] = up
        self.o["down"] = down
        self.o["inside"] = inside
        self.o["outside"] = outside
        
    def display_title(self):
        print(self.o["title"])

    def display_desc(self):
        print(self.o["title"])
        print(self.o["desc"])
        print(self.display_exits())

    def display_exits(self):
        exit_text = ""
        if self.o["north"]: exit_text += "north, "
        if self.o["east"]: exit_text += "east, "
        if self.o["south"]: exit_text += "south, "
        if self.o["west"]: exit_text += "west, "
        if self.o["up"]: exit_text += "up, "
        if self.o["down"]: exit_text += "down, "
        if self.o["inside"]: exit_text += "inside, "
        if self.o["outside"]: exit_text += "outside, "
        if exit_text:
            if exit_text[-2:] == ", ": exit_text = exit_text[:-2]
            exit_text = "There are exists to the " + exit_text + "."
        return exit_text

    def go_direction(self,vlist):
        if vlist["NORTH"] :
            return self.o["north"]
        elif vlist["EAST"]:
            return self.o["east"]
        elif vlist["SOUTH"]:
            return self.o["south"]
        elif vlist["WEST"]:
            return self.o["west"]
        elif vlist["UP"]:
            return self.o["up"]
        elif vlist["DOWN"]:
            return self.o["down"]
        elif vlist["INSIDE"]:
            return self.o["inside"]
        elif vlist["OUTSIDE"]:
            return self.o["outside"]
        return False
