#!/usr/bin/env python3

def return_evens(num_list):
    even_list= [ x for x in num_list if x %2==0]
    return even_list
#this is just an example of how to use 

numbers=[2,3,7,8,5,3,67,]
evens=return_evens(numbers)
print (evens)

def make_exclamation(sentence_list):
    addition=[sentence + "!" for sentence in sentence_list]
    return addition
#another example of how to use thef function above
the_words=["I am ","a very very happy girl","i am into","that adrenaline","shit"]
applied=make_exclamation(the_words)
print(applied)