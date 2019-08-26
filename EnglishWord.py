from itertools import  permutations
import enchant

d = enchant.Dict("en_US")   # Dict object defined in  enchant module
list_a = list(input("please input a shuffled word:"))
a_length = len(list_a)
list_copy=[]
for permu in list(permutations(range(a_length), a_length)):
    for i in permu:
        list_copy.append(list_a[i])
    maybe_word = "".join(list_copy)
    if d.check(maybe_word):   # if this is a valid English word, then return
        print("This is a possible valid word : "+ maybe_word)
        break
    list_copy = []
if list_copy == []:
    print("There is no valid word for the shuffled characters")

