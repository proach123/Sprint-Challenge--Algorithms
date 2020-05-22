'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    #first set up a base case
    if len(word) < 2: # two because th is two characters long
        return 0
    
    if word[0:2] == 'th': #uses slicing to grab the first and second value
        return count_th(word[1:]) + 1 #uses slicing to chop the front value off and push an int value up the recursion chain.
    else:
        return count_th(word[1:])


#This is the logic I want to make into recursion
    # counted = word.count('th')
    # return counted 

    # so we want to check two values and then increment them in the recursion to the next position.


