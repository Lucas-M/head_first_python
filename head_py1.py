# Chapter 1

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


movies = ["The Holy Grail", 1975, "Terry Jones", 91,
             ["Graham Chapman", ["Michail Palin", "John Cleese",
                   "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print (movies)
print_lol(movies)
