import re
from verbs import verbs

class Parser():

    def __init__(self) -> None:
        pass

    # list of words
    def parse_sentence(self,text):
        return re.findall(r'[\w]+', text.lower())

    def parse_verbs(self,text):
        to_return = {}
        list_of_words = self.parse_sentence(text)

        # single word things
        for w in list_of_words:
            for v in verbs:
                to_return[v] = False 
                list_of_alts = verbs[v].split(",")
                if w in list_of_alts:
                    to_return[v] = True                  

        # two word things
        count = 0
        for tmpw in list_of_words[::2]:
            if count+1 < len(list_of_words):
                w = list_of_words[count] + " " + list_of_words[count+1]
                count += 1
                for v in verbs:
                    list_of_alts = verbs[v].split(",")
                    if w in list_of_alts:
                        to_return[v] = True                  

        return to_return

    def parse_objs(self,text,objs):
        to_return = {}
        list_of_words = self.parse_sentence(text)

        # single word things
        for w in list_of_words:
            for itm in objs:
                to_return[objs[itm].o["lcode"]]  = False 
                list_of_alts = objs[itm].o["alts"].split(",")
                if w in list_of_alts:
                    to_return[objs[itm].o["lcode"]] = True 
        # two word things
        count = 0
        for tmpw in list_of_words[::2]:
            if count+1 < len(list_of_words):
                w = list_of_words[count] + " " + list_of_words[count+1]
                count += 1
                for itm in objs:
                    list_of_alts = objs[itm].o["alts"].split(",")
                    if w in list_of_alts:
                        to_return[objs[itm].o["lcode"]] = True 

        return to_return

