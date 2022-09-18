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
        for w in list_of_words:
            for v in verbs:
                to_return[v] = False 
                list_of_alts = verbs[v]
                if w in list_of_alts:
                    to_return[v] = True 
        return to_return

    def parse_objs(self,text,objs):
        to_return = {}
        list_of_words = self.parse_sentence(text)
        for w in list_of_words:
            for itm in objs:
                to_return[objs[itm].o["lcode"]]  = False 
                list_of_alts = objs[itm].o["alts"]
                if w in list_of_alts:
                    to_return[objs[itm].o["lcode"]] = True 
        print(to_return)
        return to_return

