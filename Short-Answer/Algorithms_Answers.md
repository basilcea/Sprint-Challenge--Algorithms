#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) o(n^3-1)


b) o(n^2)


c) o(bunnies) ===> o(n)

## Exercise II

## Using Polya

### get the pivot floor and the number of story 
def(getOptimalFloor(n)):
    eggs = number of eggs
    dropped = number of eggs dropped
    brokenEggs = 0
    f = math.ceil(n/2)
    for floor in range(f , n+1): ====> 0(n)
        brokenEggs = sum(getBrokenEggs) ===> o(1)
    notBrokenEggs = dropped - brokenEggs =====> o(1)
    if(notBrokenEggs > brokenEggs): =====> o(1)
        return f ====> o(1)
    getOptimalFloor(f+1) =====> o(n)
    
    
### if the number of eggs dropped minus the number of eggs broken is less than  number of broken eggs, move f above


## for each 


    
### get floorThatBreaksEggs 

### get floorsThatDoesNotBreakEggs



