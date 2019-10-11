'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # first split the word
    array = list(word)
    print(array)
    # initialise number of movements across the array and the count
    number = 0
    count = 0
    # set base case to when it has moved through the whole array to stop

    if number == len(array):
        return count
    if(array[number] == 't' and  array[number + 1] == 'h'):
       count +=1
    number +=1
    print(number)

    count_th(array[number : len(array)+1])

    

    #then  get the index of the first t

    # TBC
    
print(count_th('abcthxyz'))