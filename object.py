class Obj:

    def __init__(self, lcode, title = "", desc = "", location = "", alts = ""):
        self.o = {}
        self.o["lcode"] = lcode
        self.o["title"] = title
        self.o["desc"] = desc
        self.o["location"] = "RIVERBANK"
        self.o["alts"] = "lantern,brass lantern,lamp"

    def display_title(self):
        print(self.o["title"])

    def display_desc(self):
        print("%s\n%s" % (self.o["title"], self.o["desc"]))
