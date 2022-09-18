import json

# we loop through each dictionary sand dump them one by one
def save_class(fname, dict_to_save):
    with open('savedata/'+fname+'.json', 'w') as f:
        f.write("[")
        count = 0
        for l in dict_to_save:
            json.dump(dict_to_save[l].o, f)
            count += 1
            if count != len(dict_to_save): f.write(",")
        f.write("]")

# we loop through the list and set each locs entry with the matching index values
# note as dict_to_update is mutable this updates the existing, passed dictionary
def load_class(fname, dict_to_update):
    f = open('savedata/'+fname+'.json')
    tmplocs = json.load(f)
    for l in tmplocs:
        lcode = l["lcode"]
        for attrib in l:
            dict_to_update[lcode].o[attrib] = l[attrib]

# simple json save
def save_dict(fname, dict_to_save):
    with open('savedata/'+fname+'.json', 'w') as f:
        json.dump(dict_to_save, f)

# simple json load
def load_dict(fname, dict_to_update):
    f = open('savedata/'+fname+'.json')
    tmplocs = json.load(f)
    for l in tmplocs:
        dict_to_update[l] = tmplocs[l]
