'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # first split the word
    # initialise number of movements across the array and the count
    # set base case to when it has moved through the whole array to stop
    if word == '':
        return 0
    if word[:2] == 'th':
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])

    #then  get the index of the first t

    # TBC
    